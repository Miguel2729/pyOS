#!/usr/bin/env python3
"""
Instalador de Apps para pyOS
Suporta pacotes .ppk e repositórios
"""

import os
import sys
import json
import shutil
import zipfile
import tempfile
import subprocess
from pathlib import Path
from datetime import datetime
import hashlib
import time
import requests

# Cores para terminal
try:
    from colorama import Fore, Style, init
    init()
except:
    class Fore:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        MAGENTA = '\033[95m'
        CYAN = '\033[96m'
        RESET = '\033[0m'
    Style = type('Style', (), {'RESET_ALL': '\033[0m'})

class PPKInstaller:
    def __init__(self):
        self.workspace_dir = os.getcwd()
        self.apps_dir = Path(os.getcwd()).parent.parent / "apps"
        self.wdir = Path(os.getcwd()).parent.parent / 'workspace'

        self.repos_file = os.path.join(self.workspace_dir, "ppk_repos.json")
        os.system(f"touch '{self.repos_file}'")
        with open(self.repos_file, "r+") as f:
            if not f.read():
                f.write("{\"repositorios\": []}")
        self.repos = self.carregar_repositorios()

    def carregar_repositorios(self):
        """Carrega lista de repositórios"""
        if os.path.exists(self.repos_file):
            with open(self.repos_file, 'r') as f:
                return json.load(f)
        return {
            "repositorios": []
        }

    def salvar_repositorios(self):
        """Salva lista de repositórios"""
        with open(self.repos_file, 'w') as f:
            json.dump(self.repos, f, indent=2)

    def limpar_tela(self):
        """Limpa a tela"""
        os.system('clear' if os.name == 'posix' else 'cls')

    def mostrar_cabecalho(self):
        """Mostra cabeçalho do instalador"""
        print(f"{Fore.CYAN}{'='*60}{Fore.RESET}")
        print(f"{Fore.GREEN}📦 PPK INSTALLER - Gerenciador de Apps pyOS{Fore.RESET}")
        print(f"{Fore.CYAN}{'='*60}{Fore.RESET}")
        print()

    def instalar_ppk(self, arquivo_ppk):
        """
        Instala um pacote .ppk
        """
        if not os.path.exists(arquivo_ppk):
            print(f"{Fore.RED}❌ Arquivo não encontrado: {arquivo_ppk}{Fore.RESET}")
            return False

        print(f"{Fore.YELLOW}📦 Instalando: {os.path.basename(arquivo_ppk)}{Fore.RESET}")

        # Criar diretório temporário
        with tempfile.TemporaryDirectory() as tmpdir:
            try:
                # Extrair pacote
                with zipfile.ZipFile(arquivo_ppk, 'r') as zip_ref:
                    zip_ref.extractall(tmpdir)

                # Verificar manifest.json
                manifest_path = os.path.join(tmpdir, "manifest.json")
                if not os.path.exists(manifest_path):
                    print(f"{Fore.RED}❌ Pacote inválido: manifest.json não encontrado{Fore.RESET}")
                    return False

                with open(manifest_path, 'r') as f:
                    manifest = json.load(f)

                # Validar campos obrigatórios
                if 'nome' not in manifest:
                    print(f"{Fore.RED}❌ manifest.json sem campo 'nome'{Fore.RESET}")
                    return False

                nome_app = manifest['nome']
                versao = manifest.get('versao', '1.0')
                autor = manifest.get('autor', 'Desconhecido')
                descricao = manifest.get('descricao', 'Sem descrição')
                os.makedirs(self.wdir / nome_app / "cache", exist_ok=True)

                print(f"\n📋 Informações do pacote:")
                print(f"   Nome: {Fore.GREEN}{nome_app}{Fore.RESET}")
                print(f"   Versão: {versao}")
                print(f"   Autor: {autor}")
                print(f"   Descrição: {descricao}")

                # Verificar se app já existe
                app_path = os.path.join(self.apps_dir, nome_app)
                if os.path.exists(app_path):
                    print(f"\n{Fore.YELLOW}⚠️  App já instalado!{Fore.RESET}")
                    opcao = input("Deseja reinstalar? (s/N): ").strip().lower()
                    if opcao != 's':
                        print(f"{Fore.BLUE}❌ Instalação cancelada.{Fore.RESET}")
                        return False
                    # Backup do workspace
                    workspace_path = os.path.join(self.wdir, nome_app)
                    if os.path.exists(workspace_path):
                        backup_path = workspace_path + ".backup"
                        if os.path.exists(backup_path):
                            shutil.rmtree(backup_path)
                        shutil.copytree(workspace_path, backup_path)
                        print(f"{Fore.GREEN}✅ Backup do workspace criado{Fore.RESET}")
                    # Remover app antigo
                    shutil.rmtree(app_path)

                # Criar diretório do app
                os.makedirs(app_path, exist_ok=True)

                # Copiar arquivos do app
                # main.py
                main_src = os.path.join(tmpdir, "main.py")
                if os.path.exists(main_src):
                    shutil.copy2(main_src, os.path.join(app_path, "main.py"))
                else:
                    print(f"{Fore.RED}❌ main.py não encontrado no pacote{Fore.RESET}")
                    shutil.rmtree(app_path)
                    return False

                # Copiar handlers (para dentro do diretório do app, não como subpasta)
                handlers_src = os.path.join(tmpdir, "handlers")
                if os.path.exists(handlers_src):
                    for item in os.listdir(handlers_src):
                        src_path = os.path.join(handlers_src, item)
                        dst_path = os.path.join(app_path, item)
                        if os.path.isdir(src_path):
                            # Se for subpasta, copia recursivamente
                            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
                        else:
                            shutil.copy2(src_path, dst_path)
                # Copiar bibliotecas .so
                lib_src = os.path.join(tmpdir, "lib")
                if os.path.exists(lib_src):
                    lib_dst = os.path.join(app_path, "lib")
                    shutil.copytree(lib_src, lib_dst)

                # Copiar dados iniciais do workspace
                workspace_src = os.path.join(tmpdir, "workspace")
                workspace_dst = os.path.join(self.workspace_dir, nome_app)
                if os.path.exists(workspace_src):
                    os.makedirs(workspace_dst, exist_ok=True)
                    for item in os.listdir(workspace_src):
                        src_path = os.path.join(workspace_src, item)
                        dst_path = os.path.join(workspace_dst, item)
                        if os.path.isdir(src_path):
                            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
                        else:
                            shutil.copy2(src_path, dst_path)
                else:
                    # Criar workspace básico
                    os.makedirs(workspace_dst, exist_ok=True)
                    os.makedirs(os.path.join(workspace_dst, "cache"), exist_ok=True)

                # Salvar manifest instalado
                with open(os.path.join(app_path, ".installed.json"), 'w') as f:
                    json.dump({
                        "nome": nome_app,
                        "versao": versao,
                        "autor": autor,
                        "descricao": descricao,
                        "data_instalacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "origem": os.path.basename(arquivo_ppk)
                    }, f, indent=2)

                print(f"\n{Fore.GREEN}✅ App '{nome_app}' instalado com sucesso!{Fore.RESET}")
                print(f"   Local: {app_path}")
                return True

            except zipfile.BadZipFile:
                print(f"{Fore.RED}❌ Arquivo corrompido ou não é um .ppk válido{Fore.RESET}")
                return False
            except Exception as e:
                print(f"{Fore.RED}❌ Erro durante instalação: {e}{Fore.RESET}")
                return False

    def instalar_do_repositorio(self):
        """
        Instala app de um repositório remoto
        """
        print(f"{Fore.CYAN}📡 INSTALAR DO REPOSITÓRIO{Fore.RESET}")
        print()

        # Listar repositórios ativos
        repos_ativos = [r for r in self.repos['repositorios'] if r.get('ativo', True)]

        if not repos_ativos:
            print(f"{Fore.RED}❌ Nenhum repositório ativo!{Fore.RESET}")
            print("Adicione um repositório primeiro.")
            return False

        print("Repositórios disponíveis:")
        for i, repo in enumerate(repos_ativos, 1):
            print(f"  {i}. {repo['nome']} - {repo['url']}")

        try:
            escolha = int(input(f"\n{Fore.YELLOW}Escolha o repositório (1-{len(repos_ativos)}): {Fore.RESET}"))
            if escolha < 1 or escolha > len(repos_ativos):
                print(f"{Fore.RED}❌ Opção inválida{Fore.RESET}")
                return False

            repo = repos_ativos[escolha - 1]
            url_base = repo['url'].rstrip('/')

            # Baixar lista de apps
            print(f"\n{Fore.BLUE}📡 Conectando ao repositório...{Fore.RESET}")
            try:
                response = requests.get(f"{url_base}/apps.json", timeout=10)
                if response.status_code != 200:
                    print(f"{Fore.RED}❌ Não foi possível obter lista de apps{Fore.RESET}")
                    return False

                apps_disponiveis = response.json()

                print(f"\n📋 Apps disponíveis ({len(apps_disponiveis)}):")
                for i, app in enumerate(apps_disponiveis, 1):
                    print(f"  {i}. {app['nome']} - {app.get('versao', '1.0')}")
                    print(f"     {app.get('descricao', 'Sem descrição')[:60]}")

                escolha_app = int(input(f"\n{Fore.YELLOW}Escolha o app (1-{len(apps_disponiveis)}): {Fore.RESET}"))
                if escolha_app < 1 or escolha_app > len(apps_disponiveis):
                    print(f"{Fore.RED}❌ Opção inválida{Fore.RESET}")
                    return False

                app = apps_disponiveis[escolha_app - 1]

                # Baixar o pacote
                print(f"\n{Fore.BLUE}⬇️  Baixando {app['nome']}...{Fore.RESET}")
                pkg_url = f"{url_base}/pacotes/{app['arquivo']}"
                response = requests.get(pkg_url, stream=True, timeout=30)

                if response.status_code != 200:
                    print(f"{Fore.RED}❌ Falha no download{Fore.RESET}")
                    return False

                # Salvar temporariamente
                with tempfile.NamedTemporaryFile(suffix='.ppk', delete=False) as tmp:
                    for chunk in response.iter_content(chunk_size=8192):
                        tmp.write(chunk)
                    tmp_path = tmp.name

                # Instalar
                resultado = self.instalar_ppk(tmp_path)

                # Limpar arquivo temporário
                os.unlink(tmp_path)

                return resultado

            except requests.exceptions.RequestException as e:
                print(f"{Fore.RED}❌ Erro de conexão: {e}{Fore.RESET}")
                return False

        except ValueError:
            print(f"{Fore.RED}❌ Opção inválida{Fore.RESET}")
            return False

    def gerenciar_repositorios(self):
        """
        Gerencia repositórios de apps
        """
        while True:
            self.limpar_tela()
            self.mostrar_cabecalho()
            print(f"{Fore.MAGENTA}📡 GERENCIAR REPOSITÓRIOS{Fore.RESET}")
            print()

            print("Repositórios configurados:")
            for i, repo in enumerate(self.repos['repositorios'], 1):
                status = f"{Fore.GREEN}[✓]{Fore.RESET}" if repo.get('ativo', True) else f"{Fore.RED}[✗]{Fore.RESET}"
                print(f"  {i}. {status} {repo['nome']}")
                print(f"     URL: {repo['url']}")

            print()
            print("1. Adicionar repositório")
            print("2. Remover repositório")
            print("3. Ativar/Desativar repositório")
            print("4. Testar repositório")
            print("0. Voltar")

            opcao = input(f"\n{Fore.YELLOW}Opção: {Fore.RESET}").strip()

            if opcao == "1":
                nome = input("Nome do repositório: ").strip()
                url = input("URL base do repositório: ").strip()

                if nome and url:
                    self.repos['repositorios'].append({
                        "nome": nome,
                        "url": url,
                        "ativo": True
                    })
                    self.salvar_repositorios()
                    print(f"{Fore.GREEN}✅ Repositório adicionado!{Fore.RESET}")
                    time.sleep(1)

            elif opcao == "2":
                try:
                    idx = int(input("Número do repositório a remover: ")) - 1
                    if 0 <= idx < len(self.repos['repositorios']):
                        removido = self.repos['repositorios'].pop(idx)
                        self.salvar_repositorios()
                        print(f"{Fore.GREEN}✅ Repositório '{removido['nome']}' removido!{Fore.RESET}")
                        time.sleep(1)
                except:
                    print(f"{Fore.RED}❌ Opção inválida{Fore.RESET}")
                    time.sleep(1)

            elif opcao == "3":
                try:
                    idx = int(input("Número do repositório: ")) - 1
                    if 0 <= idx < len(self.repos['repositorios']):
                        repo = self.repos['repositorios'][idx]
                        repo['ativo'] = not repo.get('ativo', True)
                        self.salvar_repositorios()
                        status = "ativado" if repo['ativo'] else "desativado"
                        print(f"{Fore.GREEN}✅ Repositório '{repo['nome']}' {status}!{Fore.RESET}")
                        time.sleep(1)
                except:
                    print(f"{Fore.RED}❌ Opção inválida{Fore.RESET}")
                    time.sleep(1)

            elif opcao == "4":
                try:
                    idx = int(input("Número do repositório para testar: ")) - 1
                    if 0 <= idx < len(self.repos['repositorios']):
                        repo = self.repos['repositorios'][idx]
                        print(f"{Fore.BLUE}Testando {repo['url']}...{Fore.RESET}")
                        try:
                            response = requests.get(repo['url'], timeout=5)
                            if response.status_code == 200:
                                print(f"{Fore.GREEN}✅ Repositório acessível!{Fore.RESET}")
                            else:
                                print(f"{Fore.YELLOW}⚠️  Resposta HTTP {response.status_code}{Fore.RESET}")
                        except:
                            print(f"{Fore.RED}❌ Não foi possível conectar{Fore.RESET}")
                        time.sleep(2)
                except:
                    print(f"{Fore.RED}❌ Opção inválida{Fore.RESET}")
                    time.sleep(1)

            elif opcao == "0":
                break

    def listar_apps_instalados(self):
        """
        Lista apps instalados
        """
        self.limpar_tela()
        self.mostrar_cabecalho()
        print(f"{Fore.BLUE}📋 APPS INSTALADOS{Fore.RESET}")
        print()

        apps = []
        if os.path.exists(self.apps_dir):
            for app in os.listdir(self.apps_dir):
                app_path = os.path.join(self.apps_dir, app)
                if os.path.isdir(app_path):
                    manifest_path = os.path.join(app_path, ".installed.json")
                    if os.path.exists(manifest_path):
                        with open(manifest_path, 'r') as f:
                            info = json.load(f)
                        apps.append((app, info))
                    else:
                        apps.append((app, {"versao": "desconhecida", "autor": "?"}))

        if not apps:
            print(f"{Fore.YELLOW}📭 Nenhum app instalado{Fore.RESET}")
        else:
            for i, (app, info) in enumerate(sorted(apps), 1):
                print(f"  {i}. {Fore.GREEN}{app}{Fore.RESET} v{info.get('versao', '?')}")
                print(f"     Autor: {info.get('autor', '?')}")
                print(f"     Data: {info.get('data_instalacao', '?')}")
                print()

        input(f"\n{Fore.CYAN}Pressione Enter para continuar...{Fore.RESET}")

    def desinstalar_app(self):
        """
        Desinstala um app
        """
        self.limpar_tela()
        self.mostrar_cabecalho()
        print(f"{Fore.RED}🗑️  DESINSTALAR APP{Fore.RESET}")
        print()

        apps = []
        if os.path.exists(self.apps_dir):
            for app in os.listdir(self.apps_dir):
                app_path = os.path.join(self.apps_dir, app)
                if os.path.isdir(app_path):
                    apps.append(app)

        if not apps:
            print(f"{Fore.YELLOW}📭 Nenhum app para desinstalar{Fore.RESET}")
            time.sleep(2)
            return

        print("Apps instalados:")
        for i, app in enumerate(apps, 1):
            print(f"  {i}. {app}")

        try:
            escolha = int(input(f"\n{Fore.YELLOW}Escolha o app para desinstalar (0 para cancelar): {Fore.RESET}"))
            if escolha == 0:
                return

            if 1 <= escolha <= len(apps):
                app = apps[escolha - 1]
                app_path = os.path.join(self.apps_dir, app)
                workspace_path = os.path.join(self.workspace_dir, app)

                print(f"\n{Fore.RED}⚠️  Desinstalando {app}...{Fore.RESET}")
                print("Isso removerá o app e seus dados.")

                confirmar = input(f"{Fore.YELLOW}Tem certeza? (s/N): {Fore.RESET}").strip().lower()

                if confirmar == 's':
                    # Remover app
                    shutil.rmtree(app_path)
                    # Remover workspace (opcional)
                    if os.path.exists(workspace_path):
                        shutil.rmtree(workspace_path)
                    print(f"{Fore.GREEN}✅ App '{app}' desinstalado!{Fore.RESET}")
                else:
                    print(f"{Fore.BLUE}❌ Operação cancelada{Fore.RESET}")

                time.sleep(2)
        except ValueError:
            print(f"{Fore.RED}❌ Opção inválida{Fore.RESET}")
            time.sleep(1)

    def menu_principal(self):
        """
        Menu principal do instalador
        """
        while True:
            self.limpar_tela()
            self.mostrar_cabecalho()

            print(f"{Fore.CYAN}1.{Fore.RESET} Instalar de arquivo .ppk")
            print(f"{Fore.CYAN}2.{Fore.RESET} Instalar do repositório")
            print(f"{Fore.CYAN}3.{Fore.RESET} Gerenciar repositórios")
            print(f"{Fore.CYAN}4.{Fore.RESET} Listar apps instalados")
            print(f"{Fore.CYAN}5.{Fore.RESET} Desinstalar app")
            print(f"{Fore.CYAN}0.{Fore.RESET} Sair")
            print()

            opcao = input(f"{Fore.YELLOW}Escolha uma opção: {Fore.RESET}").strip()

            if opcao == "1":
                self.limpar_tela()
                self.mostrar_cabecalho()
                caminho = input("Caminho do arquivo .ppk: ").strip()
                if caminho:
                    self.instalar_ppk(caminho)
                    input(f"\n{Fore.CYAN}Pressione Enter para continuar...{Fore.RESET}")

            elif opcao == "2":
                self.instalar_do_repositorio()
                input(f"\n{Fore.CYAN}Pressione Enter para continuar...{Fore.RESET}")

            elif opcao == "3":
                self.gerenciar_repositorios()

            elif opcao == "4":
                self.listar_apps_instalados()

            elif opcao == "5":
                self.desinstalar_app()

            elif opcao == "0":
                print(f"\n{Fore.GREEN}👋 Saindo do PPK Installer...{Fore.RESET}")
                break

            else:
                print(f"{Fore.RED}❌ Opção inválida!{Fore.RESET}")
                time.sleep(1)

def main():
    """Função principal"""
    try:
        installer = PPKInstaller()
        installer.menu_principal()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}⚠️  Instalação interrompida{Fore.RESET}")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Erro inesperado: {e}{Fore.RESET}")
        import traceback
        traceback.print_exc()
        input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()