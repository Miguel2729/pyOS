import os
try:
	from colorama import Fore, init, Style
	
except ModuleNotFoundError:
	print("colorama não encontrado, instalando agora")	
	os.system("pip install colorama")
	try:
		from colorama import Fore, init, Style
	except ModuleNotFoundError:
		print("erro as instalar")
		quit()
import time
import re
import sys
import importlib
import subprocess
import time
import threading
os.system("apt install git")
if not os.path.exists("passwordexist.txt"):
	senhaconfig01 = input("definir senha?(s/n)")
	if senhaconfig01 == "s":
		with open("passwordexist.txt", 'w') as cfg01:
			cfg01.write("True")
		senha = input("sua senha:")
		with open("senha.txt", 'w') as cfg02:
			cfg02.write(senha)
			
			# Aplicar permissoes de segurança
		os.system("chmod 600 passwordexist.txt")
	if os.path.exists("senha.txt"):
		os.system("chmod 600 senha.txt")
	elif senhaconfig01 == "n":
		with open("passwordexist.txt", 'w') as cfg01:
			cfg01.write("False")
	else:
		print("opcao não reconhecida")
else:
	with open("passwordexist.txt", 'r') as existe:
		sim = existe.read()
		if sim == "True":
			with open("senha.txt", 'r') as senha:
				senhacorreta = senha.read()
				senhauser = input("senha: ")
				if senhauser == senhacorreta:
					pass
				else:
					print("senha incorreta")
					quit()
		else:
			pass
		
try:
	import requests
except ModuleNotFoundError:
	print("requests não encontrado, instalando agora")
	os.system("pip install requests")
	try:
		import requests
	except ModuleNotFoundError:
		print("erro as instalar")
		quit()
		
# inicialização
init()
pyOSdir = os.getcwd
colorconfig = Fore.WHITE
processos_ativos = {}
os.chdir("./")
os.makedirs("apps/libs", exist_ok=True)
print(Fore.YELLOW + "trabalhando em atualizaçoes...")
os.system("pip install --upgrade pip")
time.sleep(8)
os.system("clear")
def instalar_modulos():
	diratual = os.getcwd()
	os.chdir("./pyOS/system/modules")
	with open("pyOS_hora.py", 'w') as mod1:
		mod1.write("import time\n\ndef hora():\n	forhor = time.strftime('%H:%M')\n	return forhor")
	with open("pyOS_system.py", 'w') as mod2:
		mod2.write("import os\n\nwinbtn = '_ ⛶ X'\ndef upgpip():\n	os.system('pip install --upgrade pip')")
	os.chdir(diratual)
	os.makedirs("apps/libs", exist_ok=True)
	os.chdir("./apps/libs")
	with open('pyOS_app.py', 'w') as mod1app:
		mod1app.write("import pyfiglet\nfrom colorama import Fore\ndef fonts(fonte, texto):\n	text = pyfiglet.figlet.format(texto, font=fonte)\n\ndef colors(cor):\n	if cor == 'azul'\n		return Fore.BLUE\n	if cor == 'ciano':\n		return Fore.CYAN\n	if cor == 'roxo':\n		return Fore.MAGENTA\n	if cor == 'amarelo':\n		return Fore.YELLOW\n	if cor == 'vermelho':\n		return Fore.RED\n	if cor == 'normal':\n		return Fore.WHITE")
	with open("pyOS_proc.py", 'w') as mod2app:
		mod2app.write("""import os
import random
import subprocess
import sys

def criarproc(script, nome):
	# Encontra o diretório base automaticamente
	current_file = os.path.abspath(__file__)
	base_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
	proc_dir = os.path.join(base_dir, "pyOS", "proc")
	
	# Garante que o diretório existe
	os.makedirs(proc_dir, exist_ok=True)
	
	n1 = str(random.randint(0, 9))
	n2 = str(random.randint(0, 9))
	n3 = str(random.randint(0, 9))
	n4 = str(random.randint(0, 9))
	procpid = n1 + n2 + n3 + n4
	
	# Cria diretório do processo
	proc_path = os.path.join(proc_dir, procpid)
	os.makedirs(proc_path, exist_ok=True)
	
	# Escreve arquivos
	with open(os.path.join(proc_path, 'nome.txt'), 'w') as nomeproc:
		nomeproc.write(nome)
	with open(os.path.join(proc_path, 'script.py'), 'w') as scriptpy:
		scriptpy.write(script)
	
	# Inicia o processo em background
	try:
		processo = subprocess.Popen(
			[sys.executable, os.path.join(proc_path, 'script.py')],
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			text=True
		)
		return procpid, processo
	except Exception as e:
		print(f"Erro ao iniciar processo: {e}")
		return procpid, None""")
	os.chdir(diratual)

def instalar_hostsys():
	diroriginal = os.getcwd()
	os.chdir("./pyOS/system/hostsys")
	with open("restart.sh", 'w') as restart_sys:
		restart_sys.write('#!/bin/bash\nclear\ninit 6')
	with open("shutdown.sh", 'w') as quit_sys:
		quit_sys.write("#!/bin/bash\nclear\ninit 0")
		os.chdir(diroriginal)
	
def gerar_recursos_sistema():
    import os
    os.makedirs("./pyOS/systemRes", exist_ok=True)

    arquivos = {
        "voice_input.py": '''import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Diga algo...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='pt-BR')
        print(f"📝 Você disse: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Não entendi o que você disse.")
    except sr.RequestError as e:
        print(f"⚠️ Erro ao acessar o serviço de reconhecimento: {e}")
''',

        "ascii_image_display.py": '''from PIL import Image
from colorama import Fore, Style, init
import os

init(autoreset=True)

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=80):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

def display_ascii_image(path):
    if not os.path.exists(path):
        print("❌ Caminho da imagem inválido.")
        return
    image = Image.open(path)
    image = resize_image(image)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_img = "\\n".join([ascii_str[i:i+img_width] for i in range(0, len(ascii_str), img_width)])
    print(Fore.GREEN + ascii_img)
''',

        "device_comm.py": '''import platform
import subprocess

def list_devices():
    system = platform.system()
    print(f"🔍 Sistema detectado: {system}")
    
    if system == "Linux":
        subprocess.run(["lsusb"])
    elif system == "Windows":
        subprocess.run(["powershell", "Get-PnpDevice"])
    elif system == "Android":
        subprocess.run(["adb", "devices"])
    else:
        print("❌ Sistema não suportado para comunicação com dispositivos.")
'''
    }

    for nome, conteudo in arquivos.items():
        with open(f"./pyOS/systemRes/{nome}", "w", encoding="utf-8") as f:
            f.write(conteudo)
    print("✅ Recursos do sistema gerados com sucesso.")


def pyOS():
    from pathlib import Path
    os.makedirs("./pyOS/system/modules", exist_ok=True)
    os.makedirs("./pyOS/system/tmp", exist_ok=True)
    tmp_dir = Path("./pyOS/system/tmp")
    
    os.environ['TMPDIR'] = str(tmp_dir.absolute())
    os.environ['TEMP'] = str(tmp_dir.absolute())
    os.environ['TMP'] = str(tmp_dir.absolute())
    os.makedirs("./pyOS/system/hostsys", exist_ok=True)
    os.makedirs("./pyOS/proc", exist_ok=True)  # Este é o correto
    os.makedirs("./pyOS/systemRes", exist_ok=True)
    os.system("ln -s ../../systemRes ./pyOS/system/res")
    instalar_modulos()
    instalar_hostsys()
    gerar_recursos_sistema()
def verificar_processos_background():
    """Verifica e mantém processos rodando em background sem mensagens"""
    processos_com_erro = set()  # Conjunto para armazenar processos com erro
    
    while True:
        try:
            # Verificar se diretório de processos existe
            proc_dir = "./pyOS/proc"
            if not os.path.exists(proc_dir):
                time.sleep(5)
                continue
                
            # Listar todos os processos no diretório
            processos_no_diretorio = [d for d in os.listdir(proc_dir) 
                                    if os.path.isdir(os.path.join(proc_dir, d))]
            
            # Remover processos que não estão mais no diretório
            for pid in list(processos_ativos.keys()):
                if pid not in processos_no_diretorio:
                    try:
                        processos_ativos[pid].terminate()
                    except:
                        pass
                    del processos_ativos[pid]
                    if pid in processos_com_erro:
                        processos_com_erro.remove(pid)
            
            # Verificar e iniciar processos
            for pid in processos_no_diretorio:
                if pid in processos_com_erro:
                    continue
                    
                pid_path = os.path.join(proc_dir, pid)
                script_path = os.path.join(pid_path, 'script.py')
                
                # Verificar se o processo já está ativo
                if pid in processos_ativos:
                    if processos_ativos[pid].poll() is not None:
                        returncode = processos_ativos[pid].returncode
                        if returncode != 0:
                            processos_com_erro.add(pid)
                            error_file = os.path.join(pid_path, 'error.log')
                            with open(error_file, 'w') as f:
                                f.write(f"Processo terminou com código de erro: {returncode}\n")
                        del processos_ativos[pid]
                    continue
                
                # Iniciar novo processo
                if os.path.exists(script_path):
                    try:
                        processo = subprocess.Popen(
                            [sys.executable, script_path],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                            cwd=pid_path
                        )
                        processos_ativos[pid] = processo
                    except Exception as e:
                        processos_com_erro.add(pid)
                        error_file = os.path.join(pid_path, 'error.log')
                        with open(error_file, 'w') as f:
                            f.write(f"Erro ao iniciar processo: {e}\n")
            
            # Limpar processos finalizados
            for pid in list(processos_ativos.keys()):
                if processos_ativos[pid].poll() is not None:
                    returncode = processos_ativos[pid].returncode
                    if returncode != 0:
                        processos_com_erro.add(pid)
                        pid_path = os.path.join(proc_dir, pid)
                        error_file = os.path.join(pid_path, 'error.log')
                        with open(error_file, 'w') as f:
                            f.write(f"Processo terminou com código de erro: {returncode}\n")
                    del processos_ativos[pid]
                    
        except Exception:
            # Ignorar todos os erros silenciosamente
            pass
        
        time.sleep(3)
        


pyOS()
sys.path.insert(0, "pyOS/system/modules")
import pyOS_hora
import pyOS_system
        
# aplicativos
def calculadora():
	print("operadores:")
	print("divisão: /")
	print("multiplicação: *")
	print("somar: +")
	print("subtrair: -")
	try:
		# apenas numeros
		n1 = int(input("numero 1: "))
		n2 = int(input("numero 2: "))
	except ValueError:
		print("não é número")
		quit()
	op = input("operador matematico: ")
	# sem divisão por zero
	if  n2 == 0 and op == "/":
		print("erro de divisão por zero")
		quit()
	# apenas operadores validos
	elif op == "/" or op == "*" or op == "+" or op == "-":
		res = eval(f"{n1} {op} {n2}")
		print(res)
	else:
		print("operador invalído!")
	time.sleep(2)
	# impossivel injetar codigo, quem falar que pode não olhou o codigo direito
	
def notepad():
    # Criar diretório de notas se não existir
    notes_dir = "./notes"
    os.makedirs(notes_dir, exist_ok=True)
    
    executing = True
    while executing:
        print("açoes:\n1. ver\n2. adicionar\n3. remover\n4. sair\n5. ver conteudo de nota")
        acao = input("numero da acao:")
        
        if acao == "1":
            # Listar todas as notas
            try:
                arquivos = os.listdir(notes_dir)
                notas_txt = [f for f in arquivos if f.endswith('.txt')]
                
                if not notas_txt:
                    print("Nenhuma nota encontrada.")
                else:
                    print("Notas:")
                    for i, nota_file in enumerate(notas_txt, 1):
                        nome_nota = nota_file[:-4]  # Remove .txt
                        print(f"{i}. {nome_nota}")
            except FileNotFoundError:
                print("Diretório de notas não encontrado.")
                
        elif acao == "2":
            nome_nota = input("Nome da nota: ")
            conteudo = input("Conteúdo da nota: ")
            
            # Salvar nota em arquivo
            nota_path = os.path.join(notes_dir, f"{nome_nota}.txt")
            try:
                with open(nota_path, 'w', encoding='utf-8') as f:
                    f.write(conteudo)
                print(f"Nota '{nome_nota}' salva com sucesso!")
            except Exception as e:
                print(f"Erro ao salvar nota: {e}")
                
        elif acao == "3":
            # Listar notas para remoção
            try:
                arquivos = os.listdir(notes_dir)
                notas_txt = [f for f in arquivos if f.endswith('.txt')]
                
                if not notas_txt:
                    print("Nenhuma nota para remover.")
                else:
                    print("Notas disponíveis para remoção:")
                    for i, nota_file in enumerate(notas_txt, 1):
                        nome_nota = nota_file[:-4]
                        print(f"{i}. {nome_nota}")
                    
                    escolha = input("Digite o número ou nome da nota a remover: ")
                    
                    # Verificar se é número
                    if escolha.isdigit():
                        index = int(escolha) - 1
                        if 0 <= index < len(notas_txt):
                            nota_a_remover = notas_txt[index]
                        else:
                            print("Número inválido!")
                            continue
                    else:
                        # Buscar por nome
                        nota_a_remover = f"{escolha}.txt"
                        if nota_a_remover not in notas_txt:
                            print("Nota não encontrada!")
                            continue
                    
                    # Confirmar remoção
                    confirmar = input(f"Tem certeza que deseja remover '{nota_a_remover[:-4]}'? (s/n): ")
                    if confirmar.lower() == 's':
                        nota_path = os.path.join(notes_dir, nota_a_remover)
                        os.remove(nota_path)
                        print("Nota removida com sucesso!")
                        
            except FileNotFoundError:
                print("Diretório de notas não encontrado.")
            except Exception as e:
                print(f"Erro ao remover nota: {e}")
                
        elif acao == "4":
            executing = False
        elif acao == "5":
            nota = input("nome da nota: ") 
            with open("notes/" + nota + ".txt", 'r') as content:
                print("conteudo:\n" content.read())
            
        else:
            print("acao invalida")
			


def config():
	global colorconfig				
	print("cores texto:\n1. azul\n2. vermelho\n3. amerelo\n4. magenta\n5. verde\n6. normal\n0. outras configuracoes")
	coresc = input("cor(numero):")
	if coresc == "1":
		colorconfig = Fore.BLUE
	elif coresc == "2":
		colorconfig = Fore.RED
	elif coresc == "3":
		colorconfig = Fore.YELLOW
	elif coresc == "4":
		colorconfig = Fore.MAGENTA
	elif coresc == "5":
		colorconfig = Fore.GREEN
	elif coresc == "6":
		colorconfig = Fore.WHITE
	elif coresc == "0":
		print("opcoes:\n1. atualizar o pip\n2. informacoes")
		opcao = input("acao:")
		if opcao == "1":
			pyOS_system.upgpip()
		elif opcao == "2":
			print("info:")
			print("nome: pyOS")
			print("versão: v5.15")
			time.sleep(2)
	else:
		print("invalido!")
		
def terminal():
    executing = True
    while executing:
        diret = os.getcwd()
        coman = input(f"{diret}~$")
        
        if coman == "quit":
            executing = False
            
        elif coman.startswith("cd "):
            dire = coman[3:]
            os.chdir(dire)
            
        else:
            # Lista de comandos perigosos bloqueados
            comandos_perigosos = [
                "sudo rm -rf --no-preserve-root /",
                "sudo rm -rf --preserve-no-root /", 
                "rm -rf --no-preserve-root /",
                "rm -rf --preserve-no-root /",
                "rm -rf /",
                ":(){ :|:& };:",
                "forkbomb",
                "mkfs",
                "fdisk",
                "dd if=/dev/zero of=/dev/",
                "shutdown",
                "poweroff",
                "reboot",
                "halt",
                "init 0",
                "init 6",
                "> /dev/sda",
                "cat /dev/zero > /dev/",
                "mv /dev/null /dev/",
                "chmod -R 777 /",
                "chown -R root:root /",
                "echo 1 > /proc/sys/kernel/panic",
                "sysctl -w kernel.panic=1"
            ]
            
            # Comandos que só são permitidos dentro do diretório do pyOS
            comandos_restritos = [
                "rm -rf",
                "dd if=",
                "mkfs",
                "fdisk",
                "format"
            ]
            
            # Verificar se o comando é perigoso
            comando_perigoso = False
            for perigoso in comandos_perigosos:
                if perigoso in coman:
                    comando_perigoso = True
                    print(f"seguranca: comando bloqueado - {perigoso}")
                    break
            
            # Verificar se está tentando executar comandos restritos fora do diretório do pyOS
            if not comando_perigoso:
                for restrito in comandos_restritos:
                    if restrito in coman:
                        # Verificar se está no diretório do pyOS ou subdiretórios
                        current_path = os.getcwd()
                        pyos_path = os.path.abspath("./pyOS")
                        if not current_path.startswith(pyos_path):
                            comando_perigoso = True
                            print(f"seguranca: comando '{restrito}' só permitido dentro do diretório pyOS")
                            break
            
            # Verificar tentativas de acesso a arquivos sensíveis do sistema
            caminhos_proibidos = [
                "/etc/passwd",
                "/etc/shadow", 
                "/root/",
                "/boot/",
                "/sys/",
                "/proc/",
                "/dev/sda",
                "/dev/sdb",
                "/dev/null"
            ]
            
            if not comando_perigoso:
                for caminho in caminhos_proibidos:
                    if caminho in coman and not coman.startswith("python -m http.server"):
                        comando_perigoso = True
                        print(f"seguranca: acesso bloqueado a {caminho}")
                        break
            
            # Permitir python -m http.server em qualquer porta
            if coman.startswith("python -m http.server") or coman.startswith("python3 -m http.server"):
                # Extrair a porta se especificada
                porta = "8000"  # padrão
                if " " in coman:
                    partes = coman.split()
                    for i, parte in enumerate(partes):
                        if parte.isdigit() and i > 0:
                            porta = parte
                            break
                
                print(f"Iniciando servidor HTTP na porta {porta}...")
                os.system(coman)
                
            elif not comando_perigoso:
                # Executar comando seguro
                os.system(coman)
			
import shutil

def fileManager():
    def menu():
        print("\n📁 Gerenciador de Arquivos")
        print("[1] Listar arquivos")
        print("[2] Criar arquivo")
        print("[3] Ler arquivo")
        print("[4] Deletar arquivo/diretório")
        print("[5] Mudar diretório")
        print("[6] Voltar ao diretório anterior")
        print("[7] Editar arquivo")
        print("[0] Sair")

    current_dir = os.getcwd()

    while True:
        print(f"\n📂 Diretório atual: {current_dir}")
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                arquivos = os.listdir(current_dir)
                print("\nArquivos e Diretórios:")
                for a in arquivos:
                    caminho_completo = os.path.join(current_dir, a)
                    if os.path.isdir(caminho_completo):
                        print(f" 📁 {a}/")
                    else:
                        tamanho = os.path.getsize(caminho_completo)
                        print(f" 📄 {a} ({tamanho} bytes)")
            except PermissionError:
                print("❌ Permissão negada para listar este diretório")

        elif opcao == "2":
            nome = input("Nome do arquivo: ")
            conteudo = input("Conteúdo: ")
            caminho = os.path.join(current_dir, nome)
            try:
                with open(caminho, "w", encoding="utf-8") as f:
                    f.write(conteudo)
                print(f"✅ Arquivo '{nome}' criado.")
            except Exception as e:
                print(f"❌ Erro ao criar arquivo: {e}")

        elif opcao == "3":
            nome = input("Nome do arquivo: ")
            caminho = os.path.join(current_dir, nome)
            try:
                if os.path.isdir(caminho):
                    print("❌ Isso é um diretório, não um arquivo.")
                else:
                    with open(caminho, "r", encoding="utf-8") as f:
                        print("\n📄 Conteúdo:")
                        print(f.read())
            except FileNotFoundError:
                print("❌ Arquivo não encontrado.")
            except Exception as e:
                print(f"❌ Erro ao ler arquivo: {e}")

        elif opcao == "4":
            nome = input("Nome do arquivo/diretório: ")
            caminho = os.path.join(current_dir, nome)
            try:
                if os.path.isdir(caminho):
                    if not os.listdir(caminho):
                        os.rmdir(caminho)
                        print(f"🗑️ Diretório vazio '{nome}' deletado.")
                    else:
                        confirm = input("⚠️ Diretório não está vazio. Deletar recursivamente? (s/n): ")
                        if confirm.lower() == 's':
                            shutil.rmtree(caminho)
                            print(f"🗑️ Diretório '{nome}' e todo seu conteúdo deletados.")
                else:
                    os.remove(caminho)
                    print(f"🗑️ Arquivo '{nome}' deletado.")
            except FileNotFoundError:
                print("❌ Arquivo/Diretório não existe.")
            except Exception as e:
                print(f"❌ Erro ao deletar: {e}")

        elif opcao == "5":
            novo_dir = input("Novo diretório: ")
            if not os.path.isabs(novo_dir):
                novo_dir = os.path.join(current_dir, novo_dir)
            novo_dir = os.path.normpath(novo_dir)
            if os.path.isdir(novo_dir):
                current_dir = novo_dir
                print(f"📍 Diretório alterado para: {current_dir}")
            else:
                print("❌ Diretório inválido.")

        elif opcao == "6":
            parent_dir = os.path.dirname(current_dir)
            if os.path.isdir(parent_dir):
                current_dir = parent_dir
                print(f"↩️  Voltando para: {current_dir}")
            else:
                print("❌ Não é possível voltar mais")

        elif opcao == "7":
            nome = input("Nome do arquivo a editar: ")
            caminho = os.path.join(current_dir, nome)
            try:
                if os.path.isdir(caminho):
                    print("❌ Isso é um diretório, não um arquivo.")
                else:
                    with open(caminho, "r+", encoding="utf-8") as f:
                        conteudo_atual = f.read()
                        print("\n📄 Conteúdo atual:")
                        print(conteudo_atual)
                        novo_conteudo = input("\n✏️ Novo conteúdo (substituirá o atual): ")
                        f.seek(0)
                        f.write(novo_conteudo)
                        f.truncate()
                    print(f"✅ Arquivo '{nome}' editado com sucesso.")
            except FileNotFoundError:
                print("❌ Arquivo não encontrado.")
            except Exception as e:
                print(f"❌ Erro ao editar arquivo: {e}")

        elif opcao == "0":
            print("👋 Encerrando o gerenciador.")
            break

        else:
            print("⚠️ Opção inválida.")

def appsInstalados():
	def deps(arquivopython):
		dependencias = set()
		with open(arquivopython, 'r', encoding='utf-8') as f:
			for linha in f:
				linha = linha.strip()
				match_import = re.match(r'^import\s+([\w\.]+)', linha)
				if match_import:
					dependencias.add(match_import.group(1).split('.')[0])
					continue

				match_from = re.match(r'^from\s+([\w\.]+)\s+import\s+', linha)
				if match_from:
					dependencias.add(match_from.group(1).split('.')[0])
					continue

		return list(dependencias)
	
	aeac = {}
	while True:
		print("opcoes:\n1. instalar dependencias dos apps\n2. executar apps\n3. ver dependencias de apps\n4. instalar apps simples\n5. instalar dependencias no python dir\n6. instalar app completo\n7. executar apps completos\n8. definir arquivos python para apps completos\n9. ver arquivos de apps completos\n0. sair")
		acao = input("acao: ")
		if acao == "1":
			instalar = input("dependência (nome): ")
			os.system(f"pip install {instalar} --target=./apps/libs")
		elif acao == "2":
			app = input("app (sem o .py no final): ")
			os.system("clear")
			try:
				print(f'{app}                 {pyOS_system.winbtn}')
			except Exception:
				print(f'{app}                 ? ? ?')

			# SOLUÇÃO COM TABS - MÉTODO SIMPLES
			app_path = os.path.join("apps", f"{app}.py")
			if os.path.exists(app_path):
				try:
					# Adicionar diretório de libs ao path
					sys.path.insert(0, os.path.abspath("./apps/libs"))
					
					with open(app_path, 'r', encoding='utf-8') as f:
						codigo_app = f.read()
					
					# Executar o código do app
					exec(codigo_app, globals())
				except Exception as e:
					print(f"Erro ao executar app: {e}")
					time.sleep(3)
			else:
				print(f"App {app} não encontrado!")
				time.sleep(3)

					
		elif acao == "3":
			arquivo = input("arquivo: ")
			depen = deps("apps/" + arquivo)
			for depens in depen:
				print(depens)
				time.sleep(3)
		elif acao == "4":
			url = input("url: ")
			resposta = requests.get(url)
			nome = url.split('/')[-1]
			caminho = os.path.join('./apps', nome)
			with open(caminho, 'wb') as app:
				app.write(resposta.content)
		elif acao == "5":
			lib = input("biblioteca: ")
			os.system(f"pip install {lib}")
		elif acao == "0":
			break
		elif acao == "6":
			url = input("url: ")
			# Extrai o nome do repositório da URL
			repo_name = url.split('/')[-1]
			if repo_name.endswith('.git'):
				repo_name = repo_name[:-4]  # Remove .git se existir
			
			# Clona para um subdiretório dentro de ./apps
			destino = f"./apps/{repo_name}"
			os.system(f"git clone {url} {destino}")
			aeac[repo_name] = 'main.py'  # Define o arquivo principal
			print(f"Repositório clonado em: {destino}")
		elif acao == "7":
			app = input("pasta: ")
			arquivo = aeac.get(app)
			if arquivo:
				caminho = f"./apps/{app}/{arquivo}"
				if os.path.exists(caminho):
					# Adicionar diretório de libs ao path
					sys.path.insert(0, os.path.abspath("./apps/libs"))
					
					with open(caminho, 'r', encoding='utf-8') as appcom:
						exec(appcom.read(), globals())
				else:
					print(f"Arquivo {arquivo} não encontrado em {app}")
			else:
				print(f"App {app} não configurado")
		elif acao == "8":
			app_pra_configurar = input("app: ")
			novo_arquivo = input("novo arquivo: ")
			aeac[app_pra_configurar] = novo_arquivo
		elif acao == "9":
			app = input("app: ")
			try:
				arquivos = os.listdir(f"./apps/{app}")
				for arquivo in arquivos:
					print(arquivo)
			except FileNotFoundError:
				print(f"Pasta ./apps/{app} não encontrada")

def navegador_tui():
    try:
        from bs4 import BeautifulSoup
    except ModuleNotFoundError:
        os.system(f"{sys.executable} -m pip install beautifulsoup4")
        from bs4 import BeautifulSoup

    try:
        import pyfiglet
    except ModuleNotFoundError:
        os.system(f"{sys.executable} -m pip install pyfiglet")
        import pyfiglet

    largura = os.get_terminal_size().columns
    sessao = requests.Session()

    print(Fore.CYAN + pyfiglet.figlet_format("Navegador TUI", font="slant"))
    entrada = input(Fore.YELLOW + "🌐 Digite uma URL ou termo de busca: " + Style.RESET_ALL).strip()
    url = entrada if re.match(r'^https?://', entrada) else f"https://www.google.com/search?q={requests.utils.quote(entrada)}"

    try:
        resposta = sessao.get(url, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True)
        resposta.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"❌ Erro ao acessar a página: {e}" + Style.RESET_ALL)
        return

    soup = BeautifulSoup(resposta.text, 'html.parser')
    titulo = soup.title.string.strip() if soup.title and soup.title.string else "Sem título"
    print(Fore.MAGENTA + pyfiglet.figlet_format(titulo[:40], font="digital"))

    # Renderização TUI
    print(Fore.WHITE + "╔" + "═" * (largura - 2) + "╗")

    # Renderiza cabeçalhos
    for h in soup.find_all(re.compile('^h[1-6]$'))[:5]:
        nivel = int(h.name[1])
        texto = h.get_text(strip=True)
        cor = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.WHITE][nivel - 1]
        print("║ " + cor + (" " * nivel + texto).ljust(largura - 4) + Style.RESET_ALL + " ║")

    # Renderiza parágrafos
    for p in soup.find_all('p')[:5]:
        texto = p.get_text(strip=True)
        for linha in re.findall(r'.{1,' + str(largura - 4) + '}', texto):
            print("║ " + Fore.LIGHTWHITE_EX + linha.ljust(largura - 4) + Style.RESET_ALL + " ║")

    # Renderiza formulários
    formularios = soup.find_all('form')
    for i, form in enumerate(formularios):
        print("║" + Fore.YELLOW + f" [📝 FORMULÁRIO {i+1}] ".center(largura - 2) + Style.RESET_ALL + "║")
        campos = form.find_all('input')
        botoes = form.find_all('button')
        for campo in campos:
            nome = campo.get('name') or 'sem_nome'
            tipo = campo.get('type') or 'text'
            placeholder = campo.get('placeholder') or nome
            print("║ " + Fore.YELLOW + f"[{tipo.upper()}] {placeholder}".ljust(largura - 4) + Style.RESET_ALL + " ║")
        for botao in botoes:
            texto = botao.get_text(strip=True) or botao.get('value') or 'Botão'
            print("║ " + Fore.GREEN + f"[🟩 BOTÃO] {texto}".ljust(largura - 4) + Style.RESET_ALL + " ║")

        # Interação com formulário
        print("║" + " " * (largura - 2) + "║")
        print("║ " + Fore.CYAN + "Deseja preencher este formulário? (s/n): ".ljust(largura - 4) + Style.RESET_ALL + " ║")
        if input("👉 ").lower().startswith("s"):
            dados = {}
            for campo in campos:
                nome = campo.get('name')
                if nome:
                    valor = input(Fore.YELLOW + f"✍️ {nome}: " + Style.RESET_ALL)
                    dados[nome] = valor
            metodo = form.get('method', 'get').lower()
            acao = form.get('action') or url
            try:
                if metodo == 'post':
                    resposta = sessao.post(acao, data=dados)
                else:
                    resposta = sessao.get(acao, params=dados)
                print(Fore.GREEN + "✅ Formulário enviado com sucesso!" + Style.RESET_ALL)
                print(Fore.CYAN + f"🔁 Redirecionado para: {resposta.url}" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"❌ Erro ao enviar formulário: {e}" + Style.RESET_ALL)

    print("╚" + "═" * (largura - 2) + "╝")
    input(Fore.CYAN + "\n🧭 Pressione Enter para encerrar..." + Style.RESET_ALL)

def taskmgr():
    # Salva o diretório atual para retornar depois
    diretorio_original = os.getcwd()
    
    # Define o caminho correto para o diretório de processos
    proc_dir = "./pyOS/proc"
    
    # Verifica se o diretório existe
    if not os.path.exists(proc_dir):
        print("❌ Diretório de processos não encontrado!")
        print("Tentando criar o diretório...")
        try:
            os.makedirs(proc_dir, exist_ok=True)
            print("✅ Diretório criado com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao criar diretório: {e}")
            return
    
    try:
        # Muda para o diretório de processos
        os.chdir(proc_dir)
        
        # Lista os processos
        processos = os.listdir()
        if not processos:
            print("📭 Nenhum processo em execução")
        else:
            print("📋 Processos em execução:")
            for pasta in processos:
                caminho_pasta = os.path.join(pasta)
                if os.path.isdir(caminho_pasta):
                    caminho_nome = os.path.join(pasta, 'nome.txt')
                    if os.path.isfile(caminho_nome):
                        try:
                            nome = open(caminho_nome, encoding='utf-8').read().strip()
                            print(f"• {nome} [PID: {pasta}]")
                        except:
                            print(f"• Processo sem nome [PID: {pasta}]")
        
        # Opção para encerrar processo
        escolha = input("\n🔴 Digite o PID do processo para encerrar (ou 'quit' para sair): ")
        if escolha == "quit":
            return
        elif escolha in processos:
            confirmar = input(f"⚠️  Tem certeza que deseja encerrar o processo {escolha}? (s/n): ")
            if confirmar.lower() == 's':
                import shutil
                try:
                    shutil.rmtree(escolha)
                    print(f"✅ Processo {escolha} encerrado com sucesso!")
                except Exception as e:
                    print(f"❌ Erro ao encerrar processo: {e}")
        else:
            print("❌ PID não encontrado!")
            
    except Exception as e:
        print(f"❌ Erro no gerenciador de tarefas: {e}")
    finally:
        # Sempre retorna ao diretório original
        os.chdir(diretorio_original)
        time.sleep(2)

def abrirapp(app):
	os.system("clear")
	try:
		importlib.reload(pyOS_system)
	except Exception:
		# Remove do sys.modules primeiro
		if "pyOS_system" in sys.modules:
			del sys.modules["pyOS_system"]
		# Remove do escopo global se existir
		if 'pyOS_system' in globals():
			del globals()['pyOS_system']
		# Remove do escopo local se existir
		if 'pyOS_system' in locals():
			del locals()['pyOS_system']
		pass
	
	espaco = "                 "
	try:
		print(f'{app}{espaco}{pyOS_system.winbtn}')
	except Exception:
		print(f'{app}{espaco}? ? ?')
	try:
		apps[app]()
	except KeyError:
		print(Fore.RED + "app não encontrado")
		time.sleep(3)

def encerrar_processos_ao_sair():
    """Encerra todos os processos ativos ao sair do sistema"""
    for pid, processo in processos_ativos.items():
        try:
            processo.terminate()
            print(f"Processo {pid} encerrado")
        except:
            pass
    processos_ativos.clear()

apps = {
	"calculadora": calculadora,
	"notepad": notepad,
	"config": config,
	"terminal": terminal,
	"gerenciador de arquivos": fileManager,
	"appsInstalados": appsInstalados,
	"navegador": navegador_tui,
	"gerenciador de tarefas": taskmgr
}
# Inicie a thread de verificação de processos
thread_processos = threading.Thread(target=verificar_processos_background, daemon=True)
thread_processos.start()
executando = True
def parar():
	global executando
	executando = False
while executando:			
	print(colorconfig + "colorteste01")
	os.system("clear")
	try:
		importlib.reload(pyOS_system)
	except Exception:
		pass
	
	try:
		print(f'python-executive                 {pyOS_system.winbtn}')
	except Exception:
		print(f'python-executive                 ? ? ?')
	
	print(Fore.CYAN + "=python==hora==fechar==hostsys=\n")
	print(colorconfig + "apps:")
	nomes = list(apps.keys())
	nomes = list(apps.keys())
	nomes = list(apps.keys())
	for i in range(0, len(nomes), 3):
		print(nomes[i], end='  ')
		if i + 1 < len(nomes):
			print(nomes[i + 1], end='  ')
		if i + 2 < len(nomes):
			print(nomes[i + 2])
		else:
			print()
	app = input("app: ")
	os.system("clear")
	if app == "func":
		os.system("clear")
		print(colorconfig + "colorteste")
		os.system("clear")
		try:
			print(f'python-executive                 {pyOS_system.winbtn}')
		except Exception:
			print(f'python-executive                 ? ? ?')
		print(Fore.CYAN + "=python==hora==fechar==hostsys=")
		funcesc = input("func: ")
		if funcesc == "python":
			os.system("clear")
			print(Fore.CYAN + "=python==hora==fechar==hostsys=\n     versão\n=     pip_versão")
			escolha = input("subfunc: ")
			if escolha == "versão":
				os.system("python --version")
				time.sleep(3)
			elif escolha == "pip_versão":
				os.system("pip --version")
				time.sleep(3)
		elif funcesc == "hora":
			try:
				# Recarrega o módulo corretamente
				if "pyOS_hora" in sys.modules:
					importlib.reload(sys.modules["pyOS_hora"])
				hora = pyOS_hora.hora()
			except Exception as error:
				# Limpeza completa
				if "pyOS_hora" in sys.modules:
					del sys.modules["pyOS_hora"]
				if 'pyOS_hora' in globals():
					del globals()['pyOS_hora']
				print(f"não foi possivel obter hora: {error}")
				hora = "Erro"
			print(hora)
			del hora
			time.sleep(3)
		elif funcesc == "fechar":
			encerrar_processos_ao_sair()
			quit()
		elif funcesc == "hostsys":
			os.system("clear")
			try:
				print(f'python-executive                 {pyOS_system.winbtn}')
			except Exception:
				print(f'python-executive                 ? ? ?')
			print(Fore.CYAN + "=python==hora==fechar==hostsys=")
			print(Fore.CYAN + "                                                  desligar")
			print(Fore.CYAN + "                                                  reiniciar")
			subfuncesc = input("subfunc: ")
			if subfuncesc == "desligar":
				confirmar = input("desligar?(s/n):")
				if confirmar == "s":
					encerrar_processos_ao_sair()
					os.system("sh ./pyOS/system/hostsys/shutdown.sh")
			elif subfuncesc == "reiniciar":
				confirmar = input("reiniciar?(s/n): ")
				if confirmar == "s":
					encerrar_processos_ao_sair()
					os.system("sh ./pyOS/system/hostsys/restart.sh")
	elif app == "quit":
		encerrar_processos_ao_sair()
		quit()
	elif app in apps:
		abrirapp(app)
	else:
		print(Fore.RED + "app não encontrado")
		time.sleep(3)
