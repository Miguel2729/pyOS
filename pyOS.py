"""
pyOS

objetivo:
		no linux sistemas como alpine, arch, não tem tem gui, invez de criar uma gui real pesado para caralho, criamos um tui amigagel zero linha de comando, é como ter um interface manager so que pro linux e mais leve

notas:
		1. os botoes de acao falso da janela não é simulacao, sao decorações para tornar o tui mais famíliar
		2. ele se chama pyOS porque tenta imitar um os simples para ser amigavel, não que ele é sistema simulado
		3. so use o pyOS se o seu computador é linux sem interface grafica e voce não sabe os comandos, é como um terminal com rodinhas
"""

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

import colorama
import time
import random
import json
import socket
from typing import List, Dict
import signal
import re
import sys
from datetime import datetime
import importlib
import subprocess
import time
import shutil
import traceback
import tempfile
import curses
from pathlib import Path
import colorama
import hashlib
import secrets
import getpass

versionparts = [6, 6]
rodando2 = {}
version = f"v{versionparts[0]}.{versionparts[1]}"
dir_original = os.getcwd()

def criar_barra(msg):
		try:
				print(f'{msg}				  {pyOS_system.winbtn}')
		except Exception:
				print(f'{msg}				  ? ? ?')

def exception_handler(exc_type, exc_value, exc_traceback):
	if issubclass(exc_type, KeyboardInterrupt):
		sys.__excepthook__(exc_type, exc_value, exc_traceback)
		return


	# Primeiro limpa a tela
	os.system('cls' if os.name == 'nt' else 'clear')

	# depois chama a função criar_barra
	criar_barra("system error")



	# Printa o erro
	print("⚠️ " + str(exc_value))

	# Menu de opções
	print("[1] reiniciar o sistema | [2] desligar o sistema | [0] ignorar")

	while True:
		try:
			opcao = input("Opção: ").strip()
			if opcao == "1":
				python = sys.executable
				os.execl(python, python, *sys.argv)
			elif opcao == "0":
					return
			elif opcao == "2":
				print("Desligando o sistema...")
				quit()
			else:
				print("Opção inválida! Digite 1 ou 2.")
		except (KeyboardInterrupt, EOFError):
			print("\nDesligando o sistema...")
			quit()

sys.excepthook = exception_handler





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
pyOSdir = os.getcwd()
colorconfig = Fore.WHITE
processos_ativos = {}
os.chdir("./")
os.makedirs("./apps", exist_ok=True)
os.makedirs("./workspace", exist_ok=True)
os.system("clear")
if os.path.exists("./syscreated.txt") and not os.path.exists("./pyOS"):
	print("⛔️ a pasta ./pyOS esta ausente, o pyOS não funcionara corretamente")
	opcao = input("[1] entra mesmo assim [2] desligar: ")
	if opcao == "1":
		pass
	elif opcao == "2":
		quit()
	else:
		quit()

def instalar_modulos():
		diratual = os.getcwd()
		os.chdir("./pyOS/system/modules")

		with open("pyOS_hora.py", 'w') as mod1:
				mod1.write("import time\n\ndef hora():\n\tforhor = time.strftime('%H:%M')\n\treturn forhor")

		with open("pyOS_system.py", 'w') as mod2:
				mod2.write("import os\n\nwinbtn = '_ ⛶ X'\ndef upgpip():\n\tos.system('pip install --upgrade pip')")
		os.chdir(diratual)






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

		"ascii_image_display.py": '''
from PIL import Image
from colorama import Fore, Style, init
import os

init(autoreset=True)

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=80):
	width, height = image.size
	ratio = height / width / 1.65
	new_height = int(new_width * ratio)
	return image.resize((new_width, new_height))

def rgb_to_ansi(r, g, b):
	return f"\033[38;2;{r};{g};{b}m"

def pixels_to_ascii_colored(image):
	pixels = image.getdata()
	colored_chars = []
	
	for pixel in pixels:
		if isinstance(pixel, tuple):
			r, g, b = pixel[:3]
			char = ASCII_CHARS[sum(pixel[:3]) // 75]
			ansi_color = rgb_to_ansi(r, g, b)
			colored_chars.append((ansi_color, char))
		else:
			char = ASCII_CHARS[pixel // 25]
			colored_chars.append(("", char))
	
	return colored_chars

def display_ascii_image(path):
	if not os.path.exists(path):
		print("❌ Caminho da imagem inválido.")
		return
	
	try:
		image = Image.open(path)
		image = resize_image(image)
		
		if image.mode != 'RGB':
			image = image.convert('RGB')
			
		colored_chars = pixels_to_ascii_colored(image)
		img_width = image.width
		
		for i in range(0, len(colored_chars), img_width):
			line_chars = colored_chars[i:i+img_width]
			line = ""
			for ansi, char in line_chars:
				line += f"{ansi}{char}"
			print(line + "\033[0m")
		
	except Exception as e:
		print(f"❌ Erro ao processar imagem: {e}")

# Exemplo de uso:
# display_ascii_image("caminho/para/sua/imagem.jpg")
		'''
	}

	for nome, conteudo in arquivos.items():
		with open(f"./pyOS/systemRes/{nome}", "w", encoding="utf-8") as f:
			f.write(conteudo)
	print("✅ Recursos do sistema gerados com sucesso.")

	for nome, conteudo in arquivos.items():
		with open(f"./pyOS/systemRes/{nome}", "w", encoding="utf-8") as f:
			f.write(conteudo)
	print("✅ Recursos do sistema gerados com sucesso.")


def pyOS():
	if os.path.exists("./syscreated.txt"):
			return
	from pathlib import Path
	os.makedirs("./pyOS/system/modules", exist_ok=True)
	os.makedirs("./pyOS/system/tmp", exist_ok=True)
	tmp_dir = Path("./pyOS/system/tmp")

	os.environ['TMPDIR'] = str(tmp_dir.absolute())
	os.environ['TEMP'] = str(tmp_dir.absolute())
	os.environ['TMP'] = str(tmp_dir.absolute())
	os.makedirs("./pyOS/system/hostsys", exist_ok=True)
	os.makedirs("./pyOS/systemRes", exist_ok=True)
	os.system("ln -s ../../systemRes ./pyOS/system/res")
	instalar_modulos()
	with open("app_boot_perms.json", "w") as f:
			f.write("{}")
	gerar_recursos_sistema()
	with open("syscreated.txt", "w") as conclu:
			conclu.write("True")




pyOS()



# Arquivos de configuração (nomes ocultos para maior discrição)
ARQUIVO_SENHA_CONFIG = ".password_config"
ARQUIVO_CREDENCIAIS = ".credenciais"

def gerar_hash_senha(senha, salt):
    """Gera um hash seguro usando PBKDF2-HMAC-SHA256"""
    return hashlib.pbkdf2_hmac('sha256', senha.encode('utf-8'), salt, 100000).hex()

def definir_permissoes_seguras(caminho_arquivo):
    """Tenta definir permissões de leitura/escrita apenas para o dono (Unix)"""
    try:
        os.chmod(caminho_arquivo, 0o600)
    except OSError:
        # Ignora erro no Windows, pois chmod não funciona da mesma forma
        pass

def configurar_senha():
    nome = input("digite seu nome de usuário: ") or "usuário"
    with open("user_name.txt", "w") as f:
        f.write(nome)
    print("=== Configuração de Segurança ===")
    senhaconfig01 = input("Deseja definir uma senha de proteção? (s/n): ").lower()
    
    if senhaconfig01 == "s":
        senha = getpass.getpass("Crie sua senha: ")
        confirmacao = getpass.getpass("Confirme sua senha: ")
        
        if senha != confirmacao:
            print("As senhas não coincidem. Configuração cancelada.")
            with open(ARQUIVO_SENHA_CONFIG, 'w') as cfg:
                cfg.write("False")
            definir_permissoes_seguras(ARQUIVO_CONFIG)
            return

        # Gerar salt aleatório
        salt = secrets.token_hex(16)
        
        # Gerar hash da senha
        hash_senha = gerar_hash_senha(senha, salt.encode('utf-8'))
        
        # Salvar config (True)
        with open(ARQUIVO_SENHA_CONFIG, 'w') as cfg01:
            cfg01.write("True")
        
        # Salvar salt e hash (formato: salt$hash)
        with open(ARQUIVO_CREDENCIAIS, 'w') as cfg02:
            cfg02.write(f"{salt}${hash_senha}")
        
        definir_permissoes_seguras(ARQUIVO_SENHA_CONFIG)
        definir_permissoes_seguras(ARQUIVO_CREDENCIAIS)
        print("Senha configurada com sucesso!")
        
    elif senhaconfig01 == "n":
        with open(ARQUIVO_SENHA_CONFIG, 'w') as cfg01:
            cfg01.write("False")
        definir_permissoes_seguras(ARQUIVO_SENHA_CONFIG)
        print("Acesso sem senha configurado.")
    else:
        print("Opção não reconhecida.")

def verificar_senha():
    try:
        with open(ARQUIVO_SENHA_CONFIG, 'r') as existe:
            sim = existe.read().strip()
    except FileNotFoundError:
        return True  # Arquivo não existe, permite acesso
    
    if sim == "True":
        try:
            with open(ARQUIVO_CREDENCIAIS, 'r') as cred:
                dados = cred.read().strip().split('$')
                if len(dados) != 2:
                    raise ValueError("Arquivo de credenciais corrompido")
                
                salt_armazenado, hash_armazenado = dados
                
                # Pede a senha sem mostrar na tela
                senha_user = getpass.getpass("Digite a senha: ")
                
                # Gera o hash da senha digitada com o mesmo salt
                hash_tentativa = gerar_hash_senha(senha_user, salt_armazenado.encode('utf-8'))
                
                if hash_tentativa == hash_armazenado:
                    print("Acesso permitido.")
                    return True
                else:
                    print("Senha incorreta.")
                    return False
        except FileNotFoundError:
            print("Erro: Arquivo de senha não encontrado, mas a config diz que existe senha.")
            return False
    else:
        # Se não tem senha, permite acesso direto
        return True

# --- Lógica Principal ---

if not os.path.exists(ARQUIVO_SENHA_CONFIG):
    configurar_senha()
else:
    if not verificar_senha():
        quit()

nome = "usuário"
try:
    with open("user_name.txt", "r") as f:
        nome = f.read()
except:
    pass

# O restante do seu programa continuaria aqui...
print(f"bem-vindo {nome}")
time.sleep(0.5)


sys.path.insert(0, "pyOS/system/modules")
try:
		import pyOS_hora
		import pyOS_system
except Exception as e:
		print(f"erro ao importar modulos: {e}")

# aplicativos
def calculadora():
		try:
			n1 = float(input("número 1: "))
			n2 = float(input("número 2: "))
		except ValueError:
			print("não é número")
			input("pressione enter para sair")
			return
		print()
		print("1. adição")
		print("2. subtração")
		print("3. multiplicação")
		print("4. divisão")
		print("5. potência")
		print("6. divisão inteira")
		print("7. resto de divisão")
		try:
			op = int(input("número do operador: "))
			if not(1 <= op <= 7):
				raise ValueError()
		except ValueError:
			print("não é uma opção válido")
			input("pressione enter para sair")
			return
		ops = {
		1: lambda a, b: a + b,
		2: lambda a, b: a - b,
		3: lambda a, b: a * b,
		4: lambda a, b: a / b,
		5: lambda a, b: a ** b,
		6: lambda a, b: a // b,
		7: lambda a, b: a % b
		}
		
		try:
			r = ops[op](n1, n2)
		except:
			r = "NaN"
		str(r)
		if str(r).endswith(".0"):
			r = int(r)
		print(r)
		input("pressione enter para sair")
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
				print("conteudo:\n" + content.read())

		else:
			print("acao invalida")

def calcular_tamanho_pasta(caminho):
	"""
	Calcula o tamanho total de uma pasta em bytes.
	
	Args:
		caminho (str ou Path): Caminho para a pasta
	
	Returns:
		int: Tamanho total em bytes
	"""
	caminho = Path(caminho)
	tamanho_total = 0

	if not caminho.exists():
		raise FileNotFoundError(f"O caminho '{caminho}' não existe")

	if caminho.is_file():
		return caminho.stat().st_size

	for item in caminho.rglob('*'):
		if item.is_file():
			tamanho_total += item.stat().st_size

	return tamanho_total

def formatar_bytes(bytes_valor):
	"""
	Formata um valor em bytes para uma string legível com unidade apropriada.
	Mostra apenas os dígitos significativos sem casas decimais desnecessárias.
	
	Args:
		bytes_valor (int): Valor em bytes
	
	Returns:
		str: String formatada com a unidade apropriada
	"""
	if bytes_valor == 0:
		return "0 B"

	# Unidades de medida em ordem crescente
	unidades = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

	# Encontra o índice da unidade apropriada
	indice = 0
	valor = float(bytes_valor)

	while valor >= 1024 and indice < len(unidades) - 1:
		valor /= 1024
		indice += 1

	# Arredonda para 2 casas decimais e remove casas desnecessárias
	valor_arredondado = round(valor, len(str(valor).split(".")[1]))
	
	# Remove casas decimais desnecessárias
	if valor_arredondado.is_integer():
		return f"{int(valor_arredondado)} {unidades[indice]}"
	else:
		# Remove zeros à direita e ponto se necessário
		return f"{valor_arredondado:.2f}".rstrip('0').rstrip('.') + f" {unidades[indice]}"

def antivirus():
    """
    Antivírus avançado para pyOS com análise AST, detecção de ofuscação,
    classificação de malware e quarentena segura
    """
    import hashlib
    import ast
    import re
    import json
    import os
    import shutil
    import subprocess
    import base64
    import string
    import time
    from datetime import datetime
    from pathlib import Path
    from typing import Dict, List, Tuple, Optional
    from enum import Enum
    import traceback
    from colorama import Fore, Style

    # Cores para output
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    MAGENTA = Fore.MAGENTA
    RESET = Style.RESET_ALL

    class MalwareType(Enum):
        """Tipos de malware classificados"""
        SAFE = "seguro"
        UNKNOWN = "desconhecido"
        SPYWARE = "spyware"
        RANSOMWARE = "ransomware"
        ROOTKIT = "rootkit"
        TROJAN = "trojan"
        BACKDOOR = "backdoor"
        MINER = "minerador"
        DOWNLOADER = "downloader"
        KEYLOGGER = "keylogger"
        RAT = "rat"
        WORM = "worm"
        ADWARE = "adware"

    class ThreatAction(Enum):
        """Ações que o malware tenta executar"""
        NONE = "nenhuma"
        FILE_DELETION = "deleção de arquivos"
        FILE_ENCRYPTION = "criptografia de arquivos"
        DATA_EXFILTRATION = "exfiltração de dados"
        KEYLOGGING = "captura de teclas"
        PERSISTENCE = "persistência no sistema"
        PRIVILEGE_ESCALATION = "escalonação de privilégios"
        NETWORK_CONNECTION = "conexão de rede suspeita"
        PROCESS_INJECTION = "injeção de processo"
        CRYPTO_MINING = "mineração de criptomoedas"
        SCREEN_CAPTURE = "captura de tela"
        MICROPHONE_ACCESS = "acesso ao microfone"
        CAMERA_ACCESS = "acesso à câmera"
        CREDENTIAL_THEFT = "roubo de credenciais"
        SYSTEM_MODIFICATION = "modificação do sistema"
        DOWNLOADER = "downloader"
        BACKDOOR = "backdoor"      # ← Adicionar esta
        RANSOMWARE = "ransomware"  # ← Adicionar esta (opcional, mas usado)    class AntivirusEngine:
    class AntivirusEngine:
        """Motor principal do antivírus com análise avançada"""

        def __init__(self, auto_action: bool = False):
            self.base_dir = Path("./apps").resolve()
            self.pyos_dir = Path("./pyOS").resolve()
            self.quarantine_dir = self.pyos_dir / "quarentena_segura"
            self.db_path = self.pyos_dir / "antivirus_db.json"
            self.whitelist_path = self.pyos_dir / "whitelist_assinada.json"
            self.blacklist_path = self.pyos_dir / "blacklist.json"
            self.logs_dir = self.pyos_dir / "antivirus_logs"
            self.signature_key_path = self.pyos_dir / "av_signature.key"

            # URLs e domínios suspeitos conhecidos
            self.suspicious_domains = [
                "pastebin.com", "gist.github.com", "ngrok.io", "duckdns.org",
                "no-ip.com", "dynu.com", "afraid.org", "changeip.com"
            ]
            self.suspicious_patterns = [
                r"https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",  # IP direto
                r"https?://[a-z0-9]{32,}\.",  # Hash na URL
                r"wss?://",  # WebSocket
            ]

            # Comandos shell perigosos
            self.dangerous_shell_commands = [
                ("rm -rf", 10, ThreatAction.FILE_DELETION),
                ("dd if=", 9, ThreatAction.SYSTEM_MODIFICATION),
                ("mkfs", 8, ThreatAction.SYSTEM_MODIFICATION),
                ("chmod 777", 7, ThreatAction.PRIVILEGE_ESCALATION),
                ("chown root", 7, ThreatAction.PRIVILEGE_ESCALATION),
                ("wget", 5, ThreatAction.DOWNLOADER),
                ("curl", 5, ThreatAction.DOWNLOADER),
                ("nc ", 6, ThreatAction.BACKDOOR),
                ("netcat", 6, ThreatAction.BACKDOOR),
                ("bash -i", 8, ThreatAction.BACKDOOR),
                ("python -c", 6, ThreatAction.DOWNLOADER),
                ("perl -e", 6, ThreatAction.DOWNLOADER),
                ("openssl", 5, ThreatAction.DATA_EXFILTRATION),
                ("gpg", 4, ThreatAction.DATA_EXFILTRATION),
                ("tar czf", 5, ThreatAction.DATA_EXFILTRATION),
                ("zip -r", 5, ThreatAction.DATA_EXFILTRATION),
                ("ssh ", 4, ThreatAction.DATA_EXFILTRATION),
                ("scp ", 4, ThreatAction.DATA_EXFILTRATION),
                ("iptables -F", 8, ThreatAction.SYSTEM_MODIFICATION),
                ("ufw disable", 7, ThreatAction.SYSTEM_MODIFICATION),
                ("systemctl stop", 6, ThreatAction.SYSTEM_MODIFICATION),
                ("kill -9", 5, ThreatAction.NONE),
                ("pkill", 5, ThreatAction.NONE),
                ("crontab", 7, ThreatAction.PERSISTENCE),
                ("@reboot", 8, ThreatAction.PERSISTENCE),
                ("nohup", 6, ThreatAction.PERSISTENCE),
                ("disown", 6, ThreatAction.PERSISTENCE),
                ("screen -dmS", 6, ThreatAction.PERSISTENCE),
                ("tmux new -d", 6, ThreatAction.PERSISTENCE),
            ]

            # Padrões Python perigosos
            self.dangerous_python_patterns = [
                # Execução de código
                (r"os\.system\s*\(", 8, ThreatAction.SYSTEM_MODIFICATION),
                (r"os\.popen\s*\(", 8, ThreatAction.SYSTEM_MODIFICATION),
                (r"subprocess\.(call|run|Popen)\s*\(", 8, ThreatAction.SYSTEM_MODIFICATION),
                (r"eval\s*\(", 9, ThreatAction.NONE),
                (r"exec\s*\(", 9, ThreatAction.NONE),
                (r"compile\s*\(", 7, ThreatAction.NONE),
                (r"__import__\s*\(", 6, ThreatAction.DOWNLOADER),
                (r"importlib\.(import_module|reload)\s*\(", 6, ThreatAction.DOWNLOADER),

                # Acesso a arquivos sensíveis
                (r"open\s*\([^)]*['\"](/etc/passwd|/etc/shadow|/root/)", 9, ThreatAction.CREDENTIAL_THEFT),
                (r"shutil\.rmtree\s*\(", 7, ThreatAction.FILE_DELETION),
                (r"os\.remove\s*\(", 5, ThreatAction.FILE_DELETION),
                (r"os\.unlink\s*\(", 5, ThreatAction.FILE_DELETION),

                # Rede e exfiltração
                (r"socket\.(connect|bind|listen)\s*\(", 6, ThreatAction.NETWORK_CONNECTION),
                (r"requests\.(get|post|put|delete)\s*\(", 5, ThreatAction.DATA_EXFILTRATION),
                (r"urllib\.(request|parse)\.", 5, ThreatAction.DATA_EXFILTRATION),
                (r"http\.client\.", 5, ThreatAction.NETWORK_CONNECTION),
                (r"ftplib\.", 6, ThreatAction.DATA_EXFILTRATION),
                (r"smtplib\.", 6, ThreatAction.DATA_EXFILTRATION),

                # Persistência
                (r"exec2\.py", 7, ThreatAction.PERSISTENCE),
                (r"background.*\.py", 6, ThreatAction.PERSISTENCE),
                (r"daemon.*\.py", 6, ThreatAction.PERSISTENCE),
                (r"service.*\.py", 5, ThreatAction.PERSISTENCE),

                # Captura de entrada
                (r"pynput\.keyboard", 8, ThreatAction.KEYLOGGING),
                (r"keyboard\.hook", 8, ThreatAction.KEYLOGGING),
                (r"getpass\.", 6, ThreatAction.CREDENTIAL_THEFT),
                (r"input\s*\([^)]*senha|password|pass", 7, ThreatAction.CREDENTIAL_THEFT),

                # Captura de tela/câmera/microfone
                (r"pyautogui\.screenshot", 7, ThreatAction.SCREEN_CAPTURE),
                (r"cv2\.VideoCapture", 7, ThreatAction.CAMERA_ACCESS),
                (r"pygame\.camera", 7, ThreatAction.CAMERA_ACCESS),
                (r"speech_recognition", 6, ThreatAction.MICROPHONE_ACCESS),
                (r"pyaudio\.", 6, ThreatAction.MICROPHONE_ACCESS),
                (r"sounddevice\.", 6, ThreatAction.MICROPHONE_ACCESS),

                # Criptografia (possível ransomware)
                (r"Crypto\.Cipher", 7, ThreatAction.FILE_ENCRYPTION),
                (r"cryptography\.fernet", 7, ThreatAction.FILE_ENCRYPTION),
                (r"rsa\.", 6, ThreatAction.FILE_ENCRYPTION),
                (r"aes\.", 7, ThreatAction.FILE_ENCRYPTION),
                (r"encrypt\s*\(", 6, ThreatAction.FILE_ENCRYPTION),
                (r"decrypt\s*\(", 5, ThreatAction.NONE),

                # Mineração
                (r"cryptonight", 9, ThreatAction.CRYPTO_MINING),
                (r"xmrig", 9, ThreatAction.CRYPTO_MINING),
                (r"mining\.pool", 9, ThreatAction.CRYPTO_MINING),
                (r"stratum\+tcp", 9, ThreatAction.CRYPTO_MINING),

                # Ofuscação
                (r"base64\.b64decode\s*\(", 6, ThreatAction.NONE),
                (r"base64\.decodebytes\s*\(", 6, ThreatAction.NONE),
                (r"codecs\.decode\s*\(", 5, ThreatAction.NONE),
                (r"marshal\.loads?\s*\(", 7, ThreatAction.NONE),
                (r"pickle\.loads?\s*\(", 7, ThreatAction.NONE),
                (r"eval\s*\(\s*base64", 9, ThreatAction.NONE),
                (r"exec\s*\(\s*base64", 9, ThreatAction.NONE),
                (r"__builtins__", 8, ThreatAction.NONE),
                (r"globals\s*\(\)", 6, ThreatAction.NONE),
                (r"locals\s*\(\)", 6, ThreatAction.NONE),
                (r"setattr\s*\(", 6, ThreatAction.NONE),
                (r"getattr\s*\(", 5, ThreatAction.NONE),
                (r"delattr\s*\(", 6, ThreatAction.NONE),
            ]

            # Inicializar diretórios
            self.quarantine_dir.mkdir(parents=True, exist_ok=True)
            self.logs_dir.mkdir(parents=True, exist_ok=True)
            # Carregar dados
            self.db = self._load_db()
            self.whitelist = self._load_whitelist()
            self.blacklist = self._load_blacklist()

            # Configuração de ação automática
            self.auto_action = auto_action

        def _load_db(self) -> Dict:
            """Carrega banco de dados de scans"""
            if self.db_path.exists():
                try:
                    with open(self.db_path, 'r', encoding='utf-8') as f:
                        return json.load(f)
                except:
                    pass
            return {"scans": [], "quarantine": [], "stats": {"total": 0, "threats": 0, "clean": 0}}

        def _save_db(self):
            """Salva banco de dados"""
            with open(self.db_path, 'w', encoding='utf-8') as f:
                json.dump(self.db, f, indent=2, ensure_ascii=False)

        def _load_whitelist(self) -> Dict:
            """Carrega whitelist com verificação de assinatura"""
            default_whitelist = {
                "calculadora": {"trust_level": 10, "reason": "app nativo", "hash": ""},
                "notepad": {"trust_level": 10, "reason": "app nativo", "hash": ""},
                "agenda": {"trust_level": 10, "reason": "app nativo", "hash": ""},
                "paint": {"trust_level": 10, "reason": "app nativo", "hash": ""},
                "terminal": {"trust_level": 7, "reason": "app nativo com restrições", "hash": ""},
                "gerenciador de arquivos": {"trust_level": 8, "reason": "app nativo", "hash": ""},
                "config": {"trust_level": 9, "reason": "app nativo", "hash": ""},
                "gerenciador de tarefas": {"trust_level": 8, "reason": "app nativo", "hash": ""},
            }

            if self.whitelist_path.exists():
                try:
                    with open(self.whitelist_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        # Verificar assinatura se existir
                        if "signature" in data and "data" in data:
                            if self._verify_signature(data["data"], data["signature"]):
                                default_whitelist.update(data["data"])
                            else:
                                print(f"{YELLOW}⚠️  Assinatura da whitelist inválida!{RESET}")
                        else:
                            default_whitelist.update(data)
                except Exception as e:
                    print(f"{RED}Erro ao carregar whitelist: {e}{RESET}")

            return default_whitelist

        def _verify_signature(self, data: str, signature: str) -> bool:
            """Verifica assinatura digital da whitelist"""
            # Implementação simplificada - em produção usar GPG ou cryptography
            try:
                # Hash dos dados
                data_hash = hashlib.sha256(data.encode()).hexdigest()
                # Em produção: verificar com chave pública
                # Aqui verificamos se a assinatura existe e tem formato válido
                if len(signature) >= 64 and signature.startswith("SIG_"):
                    return True
                return False
            except:
                return False

        def _sign_whitelist(self, data: Dict) -> Dict:
            """Assina digitalmente a whitelist"""
            data_str = json.dumps(data, sort_keys=True)
            # Em produção: usar chave privada para assinar
            signature = "SIG_" + hashlib.sha256(data_str.encode()).hexdigest()
            return {
                "data": data,
                "signature": signature,
                "timestamp": datetime.now().isoformat(),
                "version": "1.0"
            }

        def _load_blacklist(self) -> Dict:
            """Carrega blacklist"""
            if self.blacklist_path.exists():
                try:
                    with open(self.blacklist_path, 'r', encoding='utf-8') as f:
                        return json.load(f)
                except:
                    pass
            return {}

        def _calculate_hash(self, filepath: Path) -> str:
            """Calcula hash SHA256 do arquivo"""
            sha256_hash = hashlib.sha256()
            try:
                with open(filepath, "rb") as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        sha256_hash.update(byte_block)
                return sha256_hash.hexdigest()
            except:
                return ""

        def _calculate_entropy(self, data: bytes) -> float:
            """Calcula entropia de Shannon para detectar ofuscação"""
            if not data:
                return 0.0

            import math
            byte_counts = {}
            
            for byte in data:
                byte_counts[byte] = byte_counts.get(byte, 0) + 1

            data_len = len(data)
            entropy = 0.0
            for count in byte_counts.values():
                if count > 0:
                    p = count / data_len
                    entropy -= p * math.log2(p)

            return entropy

        def _analyze_python_ast(self, filepath: Path) -> Tuple[int, List[str], MalwareType, List[ThreatAction]]:
            """Análise AST profunda de código Python"""
            pontuacao = 0
            problemas = []
            malware_type = MalwareType.UNKNOWN
            actions = []
            detected_patterns = set()

            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    codigo = f.read()

                # Verificar ofuscação por entropia
                entropy = self._calculate_entropy(codigo.encode())
                if entropy > 6.5:
                    pontuacao += 15
                    problemas.append(f"Alta entropia ({entropy:.2f}) - possível código ofuscado")
                    detected_patterns.add("obfuscation")

                # Verificar strings codificadas em base64
                base64_pattern = r'[A-Za-z0-9+/]{50,}={0,2}'
                base64_matches = re.findall(base64_pattern, codigo)
                for match in base64_matches:
                    try:
                        decoded = base64.b64decode(match).decode('utf-8', errors='ignore')
                        if any(p in decoded.lower() for p in ['os.system', 'eval', 'exec', 'import']):
                            pontuacao += 20
                            problemas.append("Código malicioso codificado em base64 detectado")
                            detected_patterns.add("encoded_payload")
                    except:
                        pass

                # Parse AST
                try:
                    tree = ast.parse(codigo)
                except SyntaxError as e:
                    problemas.append(f"Erro de sintaxe: {e}")
                    pontuacao += 5
                    return pontuacao, problemas, MalwareType.UNKNOWN, actions

                # Analisar nós AST
                for node in ast.walk(tree):
                    # Imports perigosos
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            if alias.name in ['os', 'sys', 'subprocess', 'socket', 'pickle', 'marshal']:
                                pontuacao += 3
                                problemas.append(f"Importação: {alias.name}")

                    if isinstance(node, ast.ImportFrom):
                        if node.module in ['os', 'sys', 'subprocess', 'socket', 'ctypes']:
                            pontuacao += 4
                            problemas.append(f"ImportFrom: {node.module}")

                    # Chamadas de função
                    if isinstance(node, ast.Call):
                        func_name = ""
                        if isinstance(node.func, ast.Attribute):
                            func_name = node.func.attr
                        elif isinstance(node.func, ast.Name):
                            func_name = node.func.id

                        # Verificar contra padrões perigosos
                        for pattern, peso, action in self.dangerous_python_patterns:
                            if re.search(pattern, f"{func_name}(", re.IGNORECASE):
                                pontuacao += peso
                                problemas.append(f"Padrão perigoso: {func_name} (+{peso})")
                                actions.append(action)
                                detected_patterns.add(func_name)

                    # Strings suspeitas
                    if isinstance(node, ast.Constant) and isinstance(node.value, str):
                        valor = node.value.lower()
                        # URLs suspeitas
                        for pattern in self.suspicious_patterns:
                            if re.search(pattern, node.value):
                                pontuacao += 10
                                problemas.append(f"URL suspeita: {node.value[:50]}")
                                actions.append(ThreatAction.NETWORK_CONNECTION)
                                detected_patterns.add("suspicious_url")

                        # Domínios suspeitos
                        for domain in self.suspicious_domains:
                            if domain in valor:
                                pontuacao += 8
                                problemas.append(f"Domínio suspeito: {domain}")
                                detected_patterns.add("suspicious_domain")

                        # Comandos shell em strings
                        for cmd, peso, action in self.dangerous_shell_commands:
                            if cmd in valor:
                                pontuacao += peso
                                problemas.append(f"Comando shell em string: {cmd}")
                                actions.append(action)
                                detected_patterns.add("shell_command")

                # Classificar tipo de malware baseado nos padrões detectados
                malware_type = self._classify_malware(detected_patterns, actions)

            except Exception as e:
                problemas.append(f"Erro na análise AST: {e}")
                pontuacao += 3

            return pontuacao, problemas, malware_type, actions

        def _analyze_shell_script(self, filepath: Path) -> Tuple[int, List[str], MalwareType, List[ThreatAction]]:
            """Análise de scripts shell (.sh)"""
            pontuacao = 0
            problemas = []
            actions = []
            detected_patterns = set()

            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    conteudo = f.read()

                # Verificar comandos perigosos
                for cmd, peso, action in self.dangerous_shell_commands:
                    if cmd in conteudo:
                        pontuacao += peso
                        problemas.append(f"Comando perigoso: {cmd} (+{peso})")
                        actions.append(action)
                        detected_patterns.add(cmd)

                # Verificar ofuscação shell
                if re.search(r'\$\([^)]+\)', conteudo):
                    pontuacao += 5
                    problemas.append("Subshell detectada (possível ofuscação)")

                if re.search(r'eval\s+', conteudo):
                    pontuacao += 10
                    problemas.append("Comando eval detectado")
                    detected_patterns.add("eval")

                # Verificar download e execução
                if re.search(r'(wget|curl).+\|\s*(bash|sh)', conteudo):
                    pontuacao += 20
                    problemas.append("Download e execução de script remoto!")
                    detected_patterns.add("remote_exec")

                # Classificar malware
                malware_type = self._classify_malware(detected_patterns, actions)

            except Exception as e:
                problemas.append(f"Erro na análise shell: {e}")
                pontuacao += 3

            return pontuacao, problemas, malware_type, actions

        def _classify_malware(self, patterns: set, actions: List[ThreatAction]) -> MalwareType:
            """Classifica o tipo de malware baseado nos padrões detectados"""
            action_counts = {}
            for action in actions:
                action_counts[action] = action_counts.get(action, 0) + 1

            # Regras de classificação
            if ThreatAction.FILE_ENCRYPTION in actions:
                return MalwareType.RANSOMWARE

            if ThreatAction.KEYLOGGING in actions or ThreatAction.CREDENTIAL_THEFT in actions:
                if ThreatAction.DATA_EXFILTRATION in actions:
                    return MalwareType.SPYWARE
                return MalwareType.KEYLOGGER

            if ThreatAction.PERSISTENCE in actions and ThreatAction.PRIVILEGE_ESCALATION in actions:
                return MalwareType.ROOTKIT

            if ThreatAction.BACKDOOR in actions or "nc " in patterns or "netcat" in patterns:
                return MalwareType.BACKDOOR

            if ThreatAction.CRYPTO_MINING in actions:
                return MalwareType.MINER
                
            if ThreatAction.DOWNLOADER in actions and ThreatAction.PERSISTENCE in actions:
                return MalwareType.TROJAN

            if ThreatAction.DATA_EXFILTRATION in actions and ThreatAction.SCREEN_CAPTURE in actions:
                return MalwareType.RAT

            if ThreatAction.PERSISTENCE in actions and "crontab" in patterns:
                return MalwareType.WORM

            if len(actions) > 0:
                return MalwareType.TROJAN

            return MalwareType.UNKNOWN

        def _quarantine_app(self, app_name: str, app_path: Path, reason: str) -> bool:
            """Move app para quarentena com permissões restritas"""
            try:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                quarantine_path = self.quarantine_dir / f"{app_name}_{timestamp}"

                # Copiar para quarentena
                if app_path.is_dir():
                    shutil.copytree(app_path, quarantine_path)
                else:
                    shutil.copy2(app_path, quarantine_path)

                # Aplicar permissões restritas em TODOS os arquivos
                for root, dirs, files in os.walk(quarantine_path):
                    for file in files:
                        file_path = Path(root) / file
                        try:
                            # chmod 000
                            os.chmod(file_path, 0o000)
                            # Mudar owner para nobody (se possível)
                            try:
                                import pwd
                                nobody_uid = pwd.getpwnam('nobody').pw_uid
                                nobody_gid = pwd.getpwnam('nobody').pw_gid
                                os.chown(file_path, nobody_uid, nobody_gid)
                            except:
                                pass  # Ignora se não tiver permissão
                        except Exception as e:
                            print(f"{YELLOW}⚠️  Não foi possível alterar permissões: {e}{RESET}")

                # Remover permissão de boot
                self._remove_boot_permission(app_name)

                # Remover original
                if app_path.exists():
                    if app_path.is_dir():
                        shutil.rmtree(app_path)
                    else:
                        os.remove(app_path)

                # Registrar na DB
                hash_value = ""
                if quarantine_path.is_dir():
                    files = list(quarantine_path.glob('*'))
                    if files:
                        hash_value = self._calculate_hash(files[0])
                else:
                    hash_value = self._calculate_hash(quarantine_path)
                    
                self.db["quarantine"].append({
                    "app": app_name,
                    "original_path": str(app_path),
                    "quarantine_path": str(quarantine_path),
                    "reason": reason,
                    "timestamp": datetime.now().isoformat(),
                    "hash": hash_value
                })
                self._save_db()

                return True
            except Exception as e:
                print(f"{RED}Erro na quarentena: {e}{RESET}")
                traceback.print_exc()
                return False

        def _remove_boot_permission(self, app_name: str):
            """Remove permissão de inicialização do app"""
            boot_perms_path = Path("./app_boot_perms.json")
            if boot_perms_path.exists():
                try:
                    with open(boot_perms_path, 'r') as f:
                        perms = json.load(f)
                    if app_name in perms:
                        perms[app_name] = False
                        with open(boot_perms_path, 'w') as f:
                            json.dump(perms, f, indent=2)
                except:
                    pass

        def _log_scan(self, app_name: str, result: Dict):
            """Registra scan nos logs"""
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "app": app_name,
                "status": result.get("status", "unknown"),
                "risk_score": result.get("risk_score", 0),
                "malware_type": result.get("malware_type", "unknown"),
                "actions": [a.value for a in result.get("actions", [])]
            }
            self.db["scans"].append(log_entry)
            self._save_db()

        def scan_app(self, app_name: str, auto_quarantine: bool = None) -> Dict:
            """Escaneia um aplicativo completo"""
            if auto_quarantine is None:
                auto_quarantine = self.auto_action

            app_path = self.base_dir / app_name
            result = {
                "app": app_name,
                "path": str(app_path),
                "status": "seguro",
                "risk_score": 0,
                "malware_type": MalwareType.SAFE.value,
                "actions": [],
                "problems": [],
                "files_scanned": 0,
                "timestamp": datetime.now().isoformat()
            }

            print(f"\n{CYAN}{'='*60}{RESET}")
            print(f"{CYAN}🔍 ESCANEANDO: {app_name}{RESET}")
            print(f"{CYAN}{'='*60}{RESET}")

            # Verificar whitelist
            if app_name in self.whitelist:
                info = self.whitelist[app_name]
                print(f"{GREEN}✓ Na whitelist (confiável){RESET}")
                print(f"   Nível: {info.get('trust_level', 'N/A')}/10")
                print(f"   Motivo: {info.get('reason', 'N/A')}")
                result["status"] = "whitelist"
                self._log_scan(app_name, result)
                return result

            # Verificar blacklist
            if app_name in self.blacklist:
                print(f"{RED}⚠️  Na blacklist!{RESET}")
                print(f"   Motivo: {self.blacklist[app_name]}")
                result["status"] = "blacklist"
                result["risk_score"] = 100
                result["malware_type"] = "bloqueado"
                if auto_quarantine:
                    self._quarantine_app(app_name, app_path, "Na blacklist")
                self._log_scan(app_name, result)
                return result

            # Escanear arquivos
            total_risk = 0
            all_actions = []
            all_problems = []
            malware_types = []
            if app_path.exists():
                files_to_scan = list(app_path.rglob("*.py")) + list(app_path.rglob("*.sh"))

                for filepath in files_to_scan:
                    result["files_scanned"] += 1
                    print(f"   📄 {filepath.name}...")

                    if filepath.suffix == '.py':
                        risk, problems, mtype, actions = self._analyze_python_ast(filepath)
                    elif filepath.suffix == '.sh':
                        risk, problems, mtype, actions = self._analyze_shell_script(filepath)
                    else:
                        continue

                    total_risk += risk
                    all_actions.extend(actions)
                    all_problems.extend(problems)
                    if mtype != MalwareType.UNKNOWN:
                        malware_types.append(mtype)

            # Calcular resultado final
            result["risk_score"] = total_risk
            result["actions"] = list(set(all_actions))
            result["problems"] = all_problems[:10]  # Limitar problemas

            # Determinar tipo de malware predominante
            if malware_types:
                # Pegar o tipo mais severo
                severity_order = [
                    MalwareType.RANSOMWARE, MalwareType.ROOTKIT, MalwareType.RAT,
                    MalwareType.BACKDOOR, MalwareType.MINER, MalwareType.TROJAN,
                    MalwareType.SPYWARE, MalwareType.KEYLOGGER, MalwareType.WORM
                ]
                for mtype in severity_order:
                    if mtype in malware_types:
                        result["malware_type"] = mtype.value
                        break
                else:
                    result["malware_type"] = malware_types[0].value
            else:
                result["malware_type"] = MalwareType.UNKNOWN.value

            # Classificar status
            if total_risk >= 50:
                result["status"] = "crítico"
            elif total_risk >= 30:
                result["status"] = "alto_risco"
            elif total_risk >= 15:
                result["status"] = "medio_risco"
            elif total_risk >= 5:
                result["status"] = "baixo_risco"
            else:
                result["status"] = "seguro"

            # Exibir resultado
            print(f"\n{BLUE}📊 RESULTADO:{RESET}")
            print(f"   Arquivos escaneados: {result['files_scanned']}")
            print(f"   Pontuação de risco: {total_risk}")
            print(f"   Tipo: {result['malware_type']}")
            print(f"   Status: {result['status'].upper()}")

            if result["actions"]:
                print(f"\n{YELLOW}⚠️  Ações detectadas:{RESET}")
                for action in set(result["actions"]):
                    print(f"   • {action.value}")

            if result["problems"]:
                print(f"\n{YELLOW}📋 Problemas encontrados:{RESET}")
                for p in result["problems"][:5]:
                    print(f"   • {p}")

            # Ação automática
            if result["status"] in ["crítico", "alto_risco"] and auto_quarantine:
                print(f"\n{RED}🚨 AÇÃO AUTOMÁTICA: Colocando em quarentena...{RESET}")
                if self._quarantine_app(app_name, app_path, f"Risco: {total_risk}, Tipo: {result['malware_type']}"):
                    result["status"] = "quarentena"
            elif result["status"] in ["crítico", "alto_risco"]:
                confirm = input(f"\n{RED}Colocar em quarentena? (s/n): {RESET}").strip().lower()
                if confirm == 's':
                    if self._quarantine_app(app_name, app_path, f"Risco: {total_risk}"):
                        result["status"] = "quarentena"

            self._log_scan(app_name, result)
            return result

        def scan_all(self, auto_quarantine: bool = None):
            """Escaneia todos os aplicativos"""
            if auto_quarantine is None:
                auto_quarantine = self.auto_action

            print(f"\n{CYAN}{'='*60}{RESET}")
            print(f"{CYAN}🛡️  ESCANEAMENTO COMPLETO - pyOS ANTIVIRUS{RESET}")
            print(f"{CYAN}{'='*60}{RESET}")

            apps = [d for d in os.listdir(self.base_dir) if os.path.isdir(self.base_dir / d)]
            results = []

            for i, app in enumerate(apps, 1):
                print(f"\n[{i}/{len(apps)}] {app}")
                result = self.scan_app(app, auto_quarantine)
                results.append(result)

            # Resumo
            print(f"\n{CYAN}{'='*60}{RESET}")
            print(f"{CYAN}📊 RESUMO DO ESCANEAMENTO{RESET}")
            print(f"{CYAN}{'='*60}{RESET}")

            threats = [r for r in results if r["status"] not in ["seguro", "whitelist"]]
            print(f"   Total de apps: {len(apps)}")
            print(f"   Seguros: {len(apps) - len(threats)}")
            print(f"   Ameaças detectadas: {len(threats)}")

            if threats:
                print(f"\n{RED}⚠️  AMEAÇAS:{RESET}")
                for t in threats:
                    print(f"   • {t['app']} - {t['malware_type']} (Risco: {t['risk_score']})")

            self._save_db()
            input(f"\n{YELLOW}Pressione Enter para continuar...{RESET}")

        def manage_whitelist(self):
            """Gerenciar whitelist com assinatura digital"""
            while True:
                os.system('clear')
                print(f"\n{CYAN}{'='*60}{RESET}")
                print(f"{CYAN}📋 GERENCIAR WHITELIST{RESET}")
                print(f"{CYAN}{'='*60}{RESET}")
                print("1. Ver whitelist atual")
                print("2. Adicionar app à whitelist")
                print("3. Remover app da whitelist")
                print("4. Assinar whitelist (admin)")
                print("5. Verificar assinatura")
                print("0. Voltar")

                op = input(f"\n{CYAN}Opção: {RESET}").strip()

                if op == "1":
                    print(f"\n{BLUE}Apps na whitelist:{RESET}")
                    for app, info in self.whitelist.items():
                        print(f"   • {app} (Nível: {info.get('trust_level', 'N/A')})")
                    input(f"\n{YELLOW}Enter para continuar...{RESET}")

                elif op == "2":
                    app_name = input("Nome do app: ").strip()
                    reason = input("Motivo: ").strip()
                    trust = input("Nível (1-10): ").strip()

                    try:
                        trust = int(trust)
                        if 1 <= trust <= 10:
                            # Calcular hash do app
                            app_path = self.base_dir / app_name
                            app_hash = ""
                            if app_path.exists():
                                files = list(app_path.rglob("*.py"))
                                if files:
                                    app_hash = self._calculate_hash(files[0])

                            self.whitelist[app_name] = {
                                "trust_level": trust,
                                "reason": reason,
                                "hash": app_hash,
                                "added": datetime.now().isoformat()
                            }

                            # Salvar e assinar
                            signed = self._sign_whitelist(self.whitelist)
                            with open(self.whitelist_path, 'w', encoding='utf-8') as f:
                                json.dump(signed, f, indent=2, ensure_ascii=False)

                            print(f"{GREEN}✓ Adicionado e assinado{RESET}")
                        else:
                            print(f"{RED}Nível inválido{RESET}")
                    except:
                        print(f"{RED}Entrada inválida{RESET}")
                    input(f"\n{YELLOW}Enter para continuar...{RESET}")

                elif op == "3":
                    app_name = input("Nome do app para remover: ").strip()
                    if app_name in self.whitelist:
                        del self.whitelist[app_name]
                        signed = self._sign_whitelist(self.whitelist)
                        with open(self.whitelist_path, 'w', encoding='utf-8') as f:
                            json.dump(signed, f, indent=2, ensure_ascii=False)
                        print(f"{GREEN}✓ Removido{RESET}")
                    else:
                        print(f"{RED}App não encontrado{RESET}")
                    input(f"\n{YELLOW}Enter para continuar...{RESET}")

                elif op == "4":
                    signed = self._sign_whitelist(self.whitelist)
                    with open(self.whitelist_path, 'w', encoding='utf-8') as f:
                        json.dump(signed, f, indent=2, ensure_ascii=False)
                    print(f"{GREEN}✓ Whitelist assinada{RESET}")
                    input(f"\n{YELLOW}Enter para continuar...{RESET}")

                elif op == "5":
                    if self.whitelist_path.exists():
                        with open(self.whitelist_path, 'r') as f:
                            data = json.load(f)
                        if "signature" in data:
                            if self._verify_signature(json.dumps(data["data"]), data["signature"]):
                                print(f"{GREEN}✓ Assinatura válida{RESET}")
                            else:
                                print(f"{RED}✗ Assinatura inválida!{RESET}")
                        else:
                            print(f"{YELLOW}⚠️  Sem assinatura{RESET}")
                    input(f"\n{YELLOW}Enter para continuar...{RESET}")

                elif op == "0":
                    break

        def manage_blacklist(self):
            """Gerenciar blacklist"""
            while True:
                os.system('clear')
                print(f"\n{CYAN}{'='*60}{RESET}")
                print(f"{CYAN}📋 GERENCIAR BLACKLIST{RESET}")
                print(f"{CYAN}{'='*60}{RESET}")
                print("1. Ver blacklist atual")
                print("2. Adicionar app à blacklist")
                print("3. Remover app da blacklist")
                print("0. Voltar")

                op = input(f"\n{CYAN}Opção: {RESET}").strip()

                if op == "1":
                    print(f"\n{RED}Apps na blacklist:{RESET}")
                    for app, reason in self.blacklist.items():
                        print(f"   • {app} - {reason}")
                    input(f"\n{YELLOW}Enter para continuar...{RESET}")

                elif op == "2":
                    app_name = input("Nome do app: ").strip()
                    reason = input("Motivo: ").strip()
                    self.blacklist[app_name] = reason
                    with open(self.blacklist_path, 'w', encoding='utf-8') as f:
                        json.dump(self.blacklist, f, indent=2, ensure_ascii=False)
                    print(f"{GREEN}✓ Adicionado{RESET}")
                    input(f"\n{YELLOW}Enter para continuar...{RESET}")

                elif op == "3":
                    app_name = input("Nome do app para remover: ").strip()
                    if app_name in self.blacklist:
                        del self.blacklist[app_name]
                        with open(self.blacklist_path, 'w', encoding='utf-8') as f:
                            json.dump(self.blacklist, f, indent=2, ensure_ascii=False)
                        print(f"{GREEN}✓ Removido{RESET}")
                    else:
                        print(f"{RED}App não encontrado{RESET}")
                    input(f"\n{YELLOW}Enter para continuar...{RESET}")

                elif op == "0":
                    break

        def view_quarantine(self):
            """Visualizar quarentena"""
            os.system('clear')
            print(f"\n{CYAN}{'='*60}{RESET}")
            print(f"{CYAN}📦 QUARENTENA{RESET}")
            print(f"{CYAN}{'='*60}{RESET}")

            if not self.db["quarantine"]:
                print(f"\n{GREEN}Nenhum app em quarentena{RESET}")
            else:
                for i, item in enumerate(self.db["quarantine"], 1):
                    print(f"\n{i}. {item['app']}")
                    print(f"   Motivo: {item['reason']}")
                    print(f"   Data: {item['timestamp']}")
                    print(f"   Local: {item['quarantine_path']}")

            print(f"\n{CYAN}{'='*60}{RESET}")
            print("1. Restaurar app")
            print("2. Excluir permanentemente")
            print("0. Voltar")

            op = input(f"\n{CYAN}Opção: {RESET}").strip()

            if op == "1" and self.db["quarantine"]:
                idx = input("Número do app: ").strip()
                if idx.isdigit() and 1 <= int(idx) <= len(self.db["quarantine"]):
                    item = self.db["quarantine"][int(idx) - 1]
                    confirm = input(f"Restaurar {item['app']}? (s/n): ").strip().lower()
                    if confirm == 's':
                        # Restaurar permissões e mover de volta
                        # (implementação simplificada)
                        print(f"{GREEN}✓ Restaurado (implementação manual necessária){RESET}")
            elif op == "2" and self.db["quarantine"]:
                idx = input("Número do app: ").strip()
                if idx.isdigit() and 1 <= int(idx) <= len(self.db["quarantine"]):
                    item = self.db["quarantine"][int(idx) - 1]
                    confirm = input(f"Excluir permanentemente {item['app']}? (s/n): ").strip().lower()
                    if confirm == 's':
                        shutil.rmtree(item['quarantine_path'], ignore_errors=True)
                        self.db["quarantine"].pop(int(idx) - 1)
                        self._save_db()
                        print(f"{GREEN}✓ Excluído{RESET}")

        def menu_interativo(self):
            """Menu principal do antivírus"""
            while True:
                os.system('clear')
                print(f"\n{CYAN}{'='*60}{RESET}")
                print(f"{CYAN}🛡️  PYOS ANTIVIRUS ENGINE v2.0{RESET}")
                print(f"{CYAN}{'='*60}{RESET}")
                print(f"\n{WHITE}Opções:{RESET}")
                print("  1. Escanear app específico")
                print("  2. Escanear todos os apps")
                print("  3. Ver quarentena")
                print("  4. Gerenciar whitelist (assinada)")
                print("  5. Gerenciar blacklist")
                print("  6. Ver estatísticas")
                print("  7. Configurar ação automática")
                print("  0. Sair")

                opcao = input(f"\n{CYAN}Escolha: {RESET}").strip()

                if opcao == "1":
                    app_name = input("Nome do app: ").strip()
                    if (self.base_dir / app_name).exists():
                        self.scan_app(app_name)
                        input(f"\n{YELLOW}Enter para continuar...{RESET}")
                    else:
                        print(f"{RED}App não encontrado{RESET}")
                        time.sleep(1)

                elif opcao == "2":
                    auto = input("Agir automaticamente em ameaças? (s/n): ").strip().lower() == 's'
                    self.scan_all(auto)

                elif opcao == "3":
                    self.view_quarantine()

                elif opcao == "4":
                    self.manage_whitelist()

                elif opcao == "5":
                    self.manage_blacklist()

                elif opcao == "6":
                    print(f"\n{CYAN}{'='*60}{RESET}")
                    print(f"{CYAN}📊 ESTATÍSTICAS{RESET}")
                    print(f"{CYAN}{'='*60}{RESET}")
                    print(f"   Total de scans: {len(self.db['scans'])}")
                    print(f"   Apps em quarentena: {len(self.db['quarantine'])}")
                    print(f"   Apps na whitelist: {len(self.whitelist)}")
                    print(f"   Apps na blacklist: {len(self.blacklist)}")
                    input(f"\n{YELLOW}Enter para continuar...{RESET}")

                elif opcao == "7":
                    self.auto_action = input("Ação automática ativada? (s/n): ").strip().lower() == 's'
                    print(f"{GREEN}✓ Configurado{RESET}")
                    time.sleep(1)

                elif opcao == "0":
                    print(f"\n{GREEN}👋 Saindo...{RESET}")
                    break

                else:
                    print(f"{RED}Opção inválida{RESET}")
                    time.sleep(1)

    # Executar
    try:
        print(f"\n{CYAN}Iniciando Antivírus pyOS...{RESET}")
        auto = input("Ativar ação automática? (s/n): ").strip().lower() == 's'
        av = AntivirusEngine(auto_action=auto)
        av.menu_interativo()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Interrompido{RESET}")
    except Exception as e:
        print(f"\n{RED}Erro: {e}{RESET}")
        traceback.print_exc()
        input("Pressione Enter...")



def diskMgr():
    """
    Gerenciador de disco para Linux com operações de gerenciamento
    """
    
    def limpar_tela():
        """Limpa a tela do terminal"""
        os.system('clear')
    
    def obter_discos() -> List[Dict]:
        """Obtém lista de discos do sistema"""
        discos = []
        try:
            resultado = subprocess.run(
                ['lsblk', '-o', 'NAME,SIZE,TYPE,MODEL,MOUNTPOINT', '-d', '-n'],
                capture_output=True, text=True
            )
            
            for linha in resultado.stdout.strip().split('\n'):
                if linha and 'disk' in linha:
                    partes = linha.split(maxsplit=4)
                    if len(partes) >= 3:
                        discos.append({
                            'nome': partes[0],
                            'tamanho': partes[1],
                            'tipo': partes[2],
                            'modelo': partes[3] if len(partes) > 3 else 'N/A',
                            'montagem': partes[4] if len(partes) > 4 else 'N/A'
                        })
            return discos
        except Exception as e:
            print(f"Erro ao obter discos: {e}")
            return []
    
    def obter_particoes(disco: str) -> List[Dict]:
        """Obtém partições de um disco específico"""
        particoes = []
        try:
            resultado = subprocess.run(
                ['lsblk', '-o', 'NAME,SIZE,TYPE,MOUNTPOINT,FSTYPE', f'/dev/{disco}', '-n'],
                capture_output=True, text=True
            )
            
            for linha in resultado.stdout.strip().split('\n')[1:]:
                if linha and 'part' in linha:
                    partes = linha.split()
                    if len(partes) >= 3:
                        particoes.append({
                            'nome': partes[0],
                            'tamanho': partes[1],
                            'tipo': partes[2],
                            'montagem': partes[3] if len(partes) > 3 else 'N/A',
                            'fs': partes[4] if len(partes) > 4 else 'N/A'
                        })
            return particoes
        except Exception as e:
            print(f"Erro ao obter partições: {e}")
            return []
    
    def exibir_discos(discos: List[Dict]) -> None:
        """Exibe lista de discos"""
        print("\n" + "="*80)
        print(" " * 30 + "DISPOSITIVOS DE ARMAZENAMENTO")
        print("="*80)
        print(f"{'Nº':<4} {'Disco':<12} {'Tamanho':<10} {'Modelo':<25} {'Montagem':<15}")
        print("-"*80)
        
        for i, disco in enumerate(discos, 1):
            print(f"{i:<4} {disco['nome']:<12} {disco['tamanho']:<10} "
                  f"{disco['modelo'][:24]:<25} {disco['montagem']:<15}")
        print("="*80)
    
    def exibir_particoes(disco: str, particoes: List[Dict]) -> None:
        """Exibe partições de um disco"""
        print("\n" + "="*80)
        print(f" " * 25 + f"PARTIÇÕES DO DISCO: {disco}")
        print("="*80)
        print(f"{'Nº':<4} {'Partição':<15} {'Tamanho':<10} {'Sistema':<12} {'Montagem':<20}")
        print("-"*80)
        
        for i, part in enumerate(particoes, 1):
            print(f"{i:<4} {part['nome']:<15} {part['tamanho']:<10} "
                  f"{part['fs']:<12} {part['montagem']:<20}")
        
        if not particoes:
            print(" " * 30 + "Nenhuma partição encontrada")
        print("="*80)
    
    def criar_tabela_particao(disco: str) -> bool:
        """Cria nova tabela de partição (GPT ou MBR)"""
        print("\n" + "="*60)
        print(" " * 15 + "CRIAR TABELA DE PARTIÇÃO")
        print("="*60)
        print("ATENÇÃO: Isso vai APAGAR TODOS OS DADOS do disco!")
        print(f"Disco: /dev/{disco}")
        print("\nTipos de tabela:")
        print("1. GPT (recomendado para UEFI)")
        print("2. MBR (para sistemas legados)")
        
        opcao = input("\nEscolha o tipo (1-2): ").strip()
        
        if opcao not in ['1', '2']:
            print("Opção inválida!")
            return False
        
        confirm = input(f"\nDeseja realmente criar tabela de partição em /dev/{disco}? (s/N): ").strip().lower()
        
        if confirm != 's':
            print("Operação cancelada.")
            return False
        
        try:
            if opcao == '1':
                subprocess.run(['sudo', 'parted', f'/dev/{disco}', 'mklabel', 'gpt'], check=True)
                print("Tabela GPT criada com sucesso!")
            else:
                subprocess.run(['sudo', 'parted', f'/dev/{disco}', 'mklabel', 'msdos'], check=True)
                print("Tabela MBR criada com sucesso!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Erro ao criar tabela: {e}")
            return False
    
    def criar_particao(disco: str) -> bool:
        """Cria nova partição usando parted"""
        print("\n" + "="*60)
        print(" " * 20 + "CRIAR NOVA PARTIÇÃO")
        print("="*60)
        print(f"Disco: /dev/{disco}")
        
        try:
            # Obtém tamanho do disco
            resultado = subprocess.run(['lsblk', '-b', '-o', 'SIZE', f'/dev/{disco}', '-n'], 
                                     capture_output=True, text=True)
            tamanho_bytes = int(resultado.stdout.strip())
            tamanho_gb = tamanho_bytes / (1024**3)
            
            print(f"\nTamanho total do disco: {tamanho_gb:.1f} GB")
            print("\nExemplos de tamanho:")
            print("- 100% (usar todo o disco)")
            print("- 50% (metade do disco)")
            print("- 10GB (10 gigabytes)")
            print("- 512MB (512 megabytes)")
            
            tamanho = input("\nDigite o tamanho da partição (ex: 10GB, 50%, 100%): ").strip()
            
            # Converte tamanho para formato do parted
            if tamanho.endswith('%'):
                tamanho = tamanho
            elif tamanho.upper().endswith('GB'):
                tamanho = tamanho.upper()
            elif tamanho.upper().endswith('MB'):
                tamanho = tamanho.upper()
            else:
                tamanho = tamanho + "GB"
            
            subprocess.run(['sudo', 'parted', f'/dev/{disco}', 'mkpart', 'primary', '0%', tamanho], check=True)
            print("Partição criada com sucesso!")
            
            # Atualiza tabela de partições
            subprocess.run(['sudo', 'partprobe', f'/dev/{disco}'], check=True)
            time.sleep(1)
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Erro ao criar partição: {e}")
            return False
    
    def formatar_particao(particao: str) -> bool:
        """Formata uma partição com sistema de arquivos"""
        print("\n" + "="*60)
        print(" " * 20 + "FORMATAR PARTIÇÃO")
        print("="*60)
        print(f"Partição: /dev/{particao}")
        print("\nSistemas de arquivos disponíveis:")
        print("1. ext4 (recomendado para Linux)")
        print("2. NTFS (compatível com Windows)")
        print("3. FAT32 (compatibilidade máxima)")
        print("4. btrfs (avançado, com snapshots)")
        print("5. xfs (bom para arquivos grandes)")
        
        opcao = input("\nEscolha o sistema de arquivos (1-5): ").strip()
        
        sistemas = {
            '1': 'ext4',
            '2': 'ntfs',
            '3': 'fat32',
            '4': 'btrfs',
            '5': 'xfs'
        }
        
        if opcao not in sistemas:
            print("Opção inválida!")
            return False
        
        fs = sistemas[opcao]
        
        confirm = input(f"\nDeseja formatar /dev/{particao} como {fs}? (s/N): ").strip().lower()
        
        if confirm != 's':
            print("Operação cancelada.")
            return False
        
        try:
            print(f"Formatando /dev/{particao} como {fs}...")
            
            if fs == 'ntfs':
                subprocess.run(['sudo', 'mkfs.ntfs', '-f', f'/dev/{particao}'], check=True)
            elif fs == 'fat32':
                subprocess.run(['sudo', 'mkfs.vfat', '-F32', f'/dev/{particao}'], check=True)
            elif fs == 'btrfs':
                subprocess.run(['sudo', 'mkfs.btrfs', '-f', f'/dev/{particao}'], check=True)
            elif fs == 'xfs':
                subprocess.run(['sudo', 'mkfs.xfs', '-f', f'/dev/{particao}'], check=True)
            else:
                subprocess.run(['sudo', 'mkfs.ext4', '-F', f'/dev/{particao}'], check=True)
            
            print(f"Formatação concluída com sucesso!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Erro ao formatar: {e}")
            return False
    
    def montar_particao(particao: str) -> bool:
        """Monta uma partição em um ponto de montagem"""
        print("\n" + "="*60)
        print(" " * 20 + "MONTAR PARTIÇÃO")
        print("="*60)
        print(f"Partição: /dev/{particao}")
        
        ponto = input("\nDigite o ponto de montagem (ex: /mnt/dados): ").strip()
        
        if not ponto:
            print("Ponto de montagem inválido!")
            return False
        
        # Cria diretório se não existir
        if not os.path.exists(ponto):
            try:
                subprocess.run(['sudo', 'mkdir', '-p', ponto], check=True)
            except:
                print(f"Não foi possível criar o diretório {ponto}")
                return False
        
        try:
            subprocess.run(['sudo', 'mount', f'/dev/{particao}', ponto], check=True)
            print(f"Partição montada em {ponto} com sucesso!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Erro ao montar: {e}")
            return False
    
    def desmontar_particao(particao: str) -> bool:
        """Desmonta uma partição"""
        print("\n" + "="*60)
        print(" " * 20 + "DESMONTAR PARTIÇÃO")
        print("="*60)
        print(f"Partição: /dev/{particao}")
        
        confirm = input("\nDeseja desmontar esta partição? (s/N): ").strip().lower()
        
        if confirm != 's':
            print("Operação cancelada.")
            return False
        
        try:
            subprocess.run(['sudo', 'umount', f'/dev/{particao}'], check=True)
            print("Partição desmontada com sucesso!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Erro ao desmontar: {e}")
            return False
    
    def deletar_particao(disco: str, particao: str) -> bool:
        """Deleta uma partição"""
        print("\n" + "="*60)
        print(" " * 20 + "DELETAR PARTIÇÃO")
        print("="*60)
        print(f"Partição: /dev/{particao}")
        print("\nATENÇÃO: Isso vai APAGAR TODOS OS DADOS da partição!")
        
        confirm = input(f"\nDeseja realmente deletar /dev/{particao}? (s/N): ").strip().lower()
        
        if confirm != 's':
            print("Operação cancelada.")
            return False
        
        try:
            # Obtém o número da partição
            num_part = particao.replace(disco, '')
            
            # Usa parted para deletar
            subprocess.run(['sudo', 'parted', f'/dev/{disco}', 'rm', num_part], check=True)
            print("Partição deletada com sucesso!")
            
            # Atualiza tabela
            subprocess.run(['sudo', 'partprobe', f'/dev/{disco}'], check=True)
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Erro ao deletar partição: {e}")
            return False
    
    def gerenciar_particoes(disco: str, particao_nome: str, particao: Dict) -> None:
        """Menu para gerenciar uma partição específica"""
        while True:
            limpar_tela()
            print("\n" + "="*70)
            print(f" " * 20 + f"GERENCIANDO PARTIÇÃO: {particao_nome}")
            print("="*70)
            print(f"Tamanho: {particao['tamanho']}")
            print(f"Sistema: {particao['fs']}")
            print(f"Montagem: {particao['montagem']}")
            print("="*70)
            print("\nOPÇÕES:")
            print("1. Formatar partição")
            print("2. Montar partição")
            print("3. Desmontar partição")
            print("4. Deletar partição")
            print("5. Voltar")
            print("="*70)
            
            opcao = input("\nEscolha uma opção (1-5): ").strip()
            
            if opcao == '1':
                if formatar_particao(particao_nome):
                    input("\nPartição formatada! Pressione ENTER para continuar...")
            elif opcao == '2':
                if montar_particao(particao_nome):
                    input("\nPartição montada! Pressione ENTER para continuar...")
            elif opcao == '3':
                if desmontar_particao(particao_nome):
                    input("\nPartição desmontada! Pressione ENTER para continuar...")
            elif opcao == '4':
                if deletar_particao(disco, particao_nome):
                    input("\nPartição deletada! Pressione ENTER para continuar...")
                    break
            elif opcao == '5':
                break
            else:
                print("\nOpção inválida!")
                input("Pressione ENTER para continuar...")
    
    def gerenciar_disco(disco: str) -> None:
        """Menu para gerenciar um disco específico"""
        while True:
            limpar_tela()
            print("\n" + "="*70)
            print(f" " * 20 + f"GERENCIANDO DISCO: {disco}")
            print("="*70)
            
            particoes = obter_particoes(disco)
            exibir_particoes(disco, particoes)
            
            print("\n" + "="*70)
            print("OPÇÕES:")
            print("1. Criar nova partição")
            print("2. Criar nova tabela de partição (APAGA TODOS OS DADOS)")
            print("3. Gerenciar uma partição existente")
            print("4. Voltar ao menu principal")
            print("5. Sair")
            print("="*70)
            
            opcao = input("\nEscolha uma opção (1-5): ").strip()
            
            if opcao == '1':
                if criar_particao(disco):
                    input("\nPartição criada! Pressione ENTER para continuar...")
            elif opcao == '2':
                if criar_tabela_particao(disco):
                    input("\nTabela criada! Pressione ENTER para continuar...")
            elif opcao == '3':
                if particoes:
                    print("\nPartições disponíveis:")
                    for i, part in enumerate(particoes, 1):
                        print(f"{i}. {part['nome']} ({part['tamanho']})")
                    
                    escolha = input("\nEscolha o número da partição: ").strip()
                    if escolha.isdigit():
                        idx = int(escolha) - 1
                        if 0 <= idx < len(particoes):
                            gerenciar_particoes(disco, particoes[idx]['nome'], particoes[idx])
                else:
                    print("\nNenhuma partição disponível!")
                    input("Pressione ENTER para continuar...")
            elif opcao == '4':
                break
            elif opcao == '5':
                print("\nSaindo...")
                exit(0)
            else:
                print("\nOpção inválida!")
                input("Pressione ENTER para continuar...")
    
    def menu_principal():
        """Menu principal da aplicação"""
        while True:
            limpar_tela()
            print("\n" + "="*70)
            print(" " * 20 + "GERENCIADOR DE DISCO")
            print(" " * 22 + "Disk Manager")
            print("="*70)
            
            discos = obter_discos()
            exibir_discos(discos)
            
            print("\n" + "="*70)
            print("OPÇÕES:")
            print("0. Atualizar lista")
            print(f"1-{len(discos)}. Gerenciar disco específico")
            print("Q. Sair")
            print("="*70)
            
            opcao = input("\nEscolha uma opção: ").strip().upper()
            
            if opcao == 'Q':
                print("\nSaindo do Disk Manager...")
                break
            elif opcao == '0':
                continue
            elif opcao.isdigit():
                num = int(opcao)
                if 1 <= num <= len(discos):
                    gerenciar_disco(discos[num-1]['nome'])
                else:
                    print("\nNúmero de disco inválido!")
                    input("Pressione ENTER para continuar...")
            else:
                print("\nOpção inválida!")
                input("Pressione ENTER para continuar...")
    
    # Executa o programa
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")
        input("Pressione ENTER para sair...")

def config():
	global rodando2
	def cls():
		os.system("clear")
		criar_barra("config")
	while True:
		cls()
		print("configurações")
		print("1. internet")
		print("2. aplicativos")
		print("3. desinstalar o pyOS")
		print("4. gerenciar discos")
		print("5. atualização/novidades")
		print("outro/0. sair")
		print()
		try:
			op = int(input("opção: "))
		except:
			print("diga uma opção valida")
			continue
		if op == 1:
			cls()
			print("1. controle de rede")
			print("2. diagnóstico de rede")
			print('outro. sair')
			try:
				op = int(input("opção: "))
			except:
				print("diga uma opção valida")
				continue
			if op == 1:
				cls()
				abrirapp("controle de internet")
				cls()
			elif op == 2:
				cls()
				abrirapp("diagnostico de rede")
				cls()
			else:
				pass
				cls()
		elif op == 2:
			cls()
			apps = {}
			for i, app in enumerate(os.listdir("./apps")):
				apps[i] = app
				print(f"{i}. {app}")
			try:
				op = int(input("opção: "))
			except:
				print("diga uma opção valida")
				continue
			if op not in apps:
				print("esse app nao existe")
			else:
				cls()
				path = f"{os.getcwd()}/apps/{apps[op]}"
				wpath = f"{os.getcwd()}/workspace/{apps[op]}"
				print(f"config - {apps[op]}")
				print("1. ver informações de espaço")
				print("2. limpar dados")
				print("3. desinstalar")
				print("4. forçar encerramento")
				print("5. autorizar iniciar com o sistema")
				print("6. desautorizar iniciar com o sistema")
				print("7. limpar cache")
				print("8. propriedades")
				print("9. abrir")
				print("outro. sair")
				try:
					aop = int(input("opção: "))
				except:
					print("diga uma opção valida")
					continue
				if aop == 1:
					asize = calcular_tamanho_pasta(path)
					dsize = calcular_tamanho_pasta(wpath)
					csize = calcular_tamanho_pasta(f"{wpath}/cache")
					total = asize + dsize # dsize ja inclui o tamanho do cache
					print(f"codigo: {formatar_bytes(asize)}")
					print(f"dados: {formatar_bytes(dsize)}")
					print(f"cache: {formatar_bytes(csize)}")
					print(f"total: {formatar_bytes(total)}")
					input("pressione enter para sair...")
				elif aop == 2:
					shutil.rmtree(wpath)
					os.makedirs(f"{wpath}/cache", exist_ok=True)
				elif aop == 3:
					if apps[op] in rodando2:
						os.kill(rodando2[apps[op]], signal.SIGKILL)
						del rodando2[apps[op]]
					shutil.rmtree(wpath)
					shutil.rmtree(path)
					print(f"{apps[op]} desinstalado")
					time.sleep(0.5)
				elif aop == 7:
					shutil.rmtree(f"{wpath}/cache")
					os.makedirs(f"{wpath}/cache", exist_ok=True)
				elif aop == 4:
					if apps[op] in rodando2:
						os.kill(rodando2[apps[op]], signal.SIGKILL)
						del rodando2[apps[op]]
				elif aop == 5:
					with open("app_boot_perms.json", "r") as f:
						ag = json.load(f)
					with open("app_boot_perms.json", "w") as f:
						ag[apps[op]] = True
						json.dump(ag, f)
				elif aop == 6:
					with open("app_boot_perms.json", "r") as f:
						ag = json.load(f)
					with open("app_boot_perms.json", "w") as f:
						ag[apps[op]] = False
						json.dump(ag, f)
				elif aop == 8:
					at = formatar_bytes(calcular_tamanho_pasta(path))
					print(f"tamamho: {at}")
					print(f"executando em segundo plano: {apps[op] in rodando2}")
					input("pressione enter para sair...")
				elif aop == 9:
					abrirapp(apps[op])
				
				else:
					cls()
					pass
		elif op == 3:
			os.system("clear")
			criar_barra("desinstalar")
			uninstall()
		elif op == 4:
			os.system('clear')
			criar_barra("disk manager")
			diskMgr()
		elif op == 5:
			cls()
			os.system("wget -O VERSION_HISTORY.txt https://raw.githubusercontent.com/Miguel2729/pyOS/refs/heads/main/VERSION_HISTORY.txt")
			cls()
			novo = "???"
			try:
				with open("VERSION_HISTORY.txt", "r") as f:
					tmp = f.readlines()
					for l in tmp:
						if ":" not in l:
							continue
						v, n = l.split(":")
						if v == version.replace("v", ""):
							novo = n.strip()
							break
			except Exception as e:
				novo = "não foi possível obter as novidades: " + e
			print(f"pyOS {version}")
			print(f"novidades: {novo}")
			print()
			print("1. atualizar")
			print("0. voltar")
			try:
				op = int(input("opcao: "))
			except:
				print("digite um número")
				input("pressione enter para sair...")
			if op == 1:
				os.remove("./syscreated.txt")
				os.system("wget https://raw.githubusercontent.com/Miguel2729/pyOS/refs/heads/main/pyOS.py")
				os.execv(sys.executable, [sys.executable, *sys.argv])
			else:
				pass
		elif op == 0:
			break
		else:
			break






def terminal():
	import getpass
	global apps
	try:
			user = getpass.getuser()
	except Exception:
			user = "unknown"
	executing = True
	while executing:
		diret = os.getcwd()
		coman = input(Fore.CYAN + f"{__import__('socket').gethostname()}@{user} {diret}>" + Fore.RESET)

		if coman in ["quit", "exit"]:
			os.chdir(dir_original)
			executing = False

		elif coman.startswith("cd "):
			dire = coman[3:]
			os.chdir(dire)
		elif coman == "unlock_sys":
			apps["system-mgr"] = sysmgr
			print("system-mgr unlocked")
		elif coman.startswith("priv "):
			os.system(coman[len("priv "):])


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
				"sysctl -w kernel.panic=1",
				"kill 0",
				"pkill 0",
				"pkill 1",
				"pkill -P 1",
				"kill -9 1",
				"pkill -9",
				"pkill -u root",
				"pkill -f python",
				"kill -9 $$",
				"cat senha.txt"
				"rm -rf pyOS",
				"rm -r pyOS",
				"rm -rv pyOS",
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
				"/dev/sdb"
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
	mostrar_ocultos = False
	def menu():
		os.system("clear")
		criar_barra('gerenciador de arquivos')
		print("\n📁 Gerenciador de Arquivos")
		print("[1] Listar arquivos")
		print("[2] Criar arquivo")
		print("[3] Criar pasta")
		print("[4] Ler arquivo")
		print("[5] Deletar arquivo/diretório")
		print("[6] Mudar diretório")
		print("[7] Voltar ao diretório anterior")
		print("[8] Editar arquivo")
		print("[9] Ativar/Desativar mostrar arquivos ocultos")
		print("[10] abrir com")
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
						if a.startswith(".") and not mostrar_ocultos:
							continue
						print(f" 📁 {a}/")
					else:
						tamanho = os.path.getsize(caminho_completo)
						print(f" 📄 {a} ({formatar_bytes(tamanho)})")
				
			except PermissionError:
				print("❌ Permissão negada para listar este diretório")
			input("pressione enter para sair...")
		elif opcao == "2":
			nome = input("Nome do arquivo: ")
			os.system(f"touch {nome}")
		elif opcao == "3":
			nome = input("nome da pasta: ")
			if os.path.exists(nome):
				print("ela ja existe")
			else:
				try:
					os.mkdir(nome)
				except Exception as e:
					print("não foi possível criar a pasta", e)
		elif opcao == "4":
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
			input("pressione enter para sair.")

		elif opcao == "5":
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

		elif opcao == "6":
			novo_dir = input("Novo diretório: ")
			if not os.path.isabs(novo_dir):
				novo_dir = os.path.join(current_dir, novo_dir)
			novo_dir = os.path.normpath(novo_dir)
			if os.path.isdir(novo_dir):
				current_dir = novo_dir
				print(f"📍 Diretório alterado para: {current_dir}")
			else:
				print("❌ Diretório inválido.")

		elif opcao == "7":
			parent_dir = os.path.dirname(current_dir)
			if os.path.isdir(parent_dir):
				current_dir = parent_dir
				print(f"↩️  Voltando para: {current_dir}")
			else:
				print("❌ Não é possível voltar mais")

		elif opcao == "8":
			nome = input("Nome do arquivo a editar: ")
			caminho = os.path.join(current_dir, nome)
			os.system(f"nano {caminho}")
		elif opcao == "9":
			mostrar_ocultos = not mostrar_ocultos
		elif opcao == "10":
			f = input("nome do arquivo: ")
			ftype = f.split(".")[1] if "." in f else ""
			if not ftype:
				print("arquivo sem extensão")
				input("pressione enter para sair...")
				continue
	
			# Verificação corrigida do arquivo
			if not os.path.exists(f"{current_dir}/{f}"):
				print("esse arquivo não existe")
				input("pressione enter para sair...")
				continue
	
			an = 1
			apps = {}
			for app in os.listdir("./apps"):
				if os.path.exists(f"./apps/{app}/{ftype}.py"):
					apps[an] = app
					an += 1
	
			if len(apps) <= 0:
				print("nenhum app pode abrir o arquivo")
				input("pressione enter para sair...")
				continue
	
			for i, n in apps.items():
				print(f"{i}. {n}")
	
			try:
				a = int(input("escolha o app: "))
			except ValueError:
				print("digite algo valido")
				input("pressione enter para sair...")
				continue
	
			if a not in apps:
				print("digite algo valido")
				input("pressione enter para sair...")
				continue
	
			abrirapp_c(apps[a], ac=ftype, argv=[f"{current_dir}/{f}"])				
		elif opcao == "0":
			print("👋 Encerrando o gerenciador.")
			break

		else:
			print("⚠️ Opção inválida.")

def navegador():
	"""Navegador TUI completo com suporte a mouse, renderização fiel e formulários"""
	import curses
	import yaml
	from bs4 import BeautifulSoup, Comment
	import requests
	from PIL import Image
	import io
	import os
	import sys
	import time
	from urllib.parse import urljoin, urlparse

	class VirtualMouse:
		def __init__(self, config_file='mouse_tui_browser.yml'):
			self.x = 0
			self.y = 0
			self.enabled = False
			self.clicked = False
			self.last_click_x = -1
			self.last_click_y = -1
			self.sensitivity = 1
			self.load_config(config_file)

		def load_config(self, config_file):
			try:
				with open(config_file, 'r') as f:
					config = yaml.safe_load(f)
					self.enabled = config.get('mouse_enabled', False)
					self.sensitivity = config.get('mouse_sensitivity', 1)
			except:
				self.enabled = False

		def move(self, dx, dy):
			if self.enabled:
				self.x += dx * self.sensitivity
				self.y += dy * self.sensitivity

		def click(self, x, y):
			if self.enabled:
				self.clicked = True
				self.last_click_x = x
				self.last_click_y = y

		def release(self):
			self.clicked = False

	class TUIBrowser:
		def __init__(self):
			self.stdscr = None
			self.mouse = VirtualMouse()
			self.current_url = ""
			self.base_url = ""
			self.raw_html = ""
			self.parsed_content = None
			self.elements = []
			self.history = []
			self.history_index = -1
			self.selected_element = 0
			self.input_mode = False
			self.input_text = ""
			self.input_element = None
			self.input_field_index = -1
			self.status_message = ""
			self.status_timer = 0
			self.scroll_offset = 0
			self.content_lines = []
			self.content_positions = []
			self.form_data = {}
			self.last_render_time = 0
			self.needs_render = True
			self.status_is_error = False

		def init_curses(self):
			self.stdscr = curses.initscr()
			curses.noecho()
			curses.cbreak()
			self.stdscr.keypad(True)
			self.stdscr.nodelay(False)
			self.stdscr.timeout(100)

			try:
				curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
				curses.mouseinterval(0)
				print("\033[?1003h\033[?1015h\033[?1006h")
				self.mouse.enabled = True
			except:
				self.mouse.enabled = False

			try:
				curses.start_color()
				curses.use_default_colors()
				if curses.COLORS >= 8:
					curses.init_pair(1, curses.COLOR_CYAN, -1)
					curses.init_pair(2, curses.COLOR_GREEN, -1)
					curses.init_pair(3, curses.COLOR_YELLOW, -1)
					curses.init_pair(4, curses.COLOR_RED, -1)
					curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLUE)
					curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
					curses.init_pair(7, curses.COLOR_BLUE, -1)
					curses.init_pair(8, curses.COLOR_MAGENTA, -1)
					self.has_colors = True
				else:
					self.has_colors = False
			except:
				self.has_colors = False

		def cleanup_curses(self):
			try:
				print("\033[?1003l\033[?1015l\033[?1006l")
				curses.nocbreak()
				self.stdscr.keypad(False)
				curses.echo()
				curses.endwin()
			except:
				pass

		def get_color_pair(self, num):
			if self.has_colors:
				try:
					return curses.color_pair(num)
				except:
					return 0
			return 0

		def set_status(self, message, is_error=False):
			self.status_message = message
			self.status_timer = 100
			self.status_is_error = is_error

		def clean_html(self, soup):
			"""Remove tags indesejadas do HTML"""
			# Remove scripts
			for script in soup.find_all(['script', 'style', 'noscript']):
				script.decompose()

			# Remove comentários
			for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
				comment.extract()

			# Remove meta, link, etc
			for tag in soup.find_all(['meta', 'link', 'head']):
				tag.decompose()

			return soup

		def fetch_url(self, url):
			if not url:
				return False

			if not url.startswith(('http://', 'https://')):
				url = 'https://' + url

			try:
				self.set_status(f"Carregando {url}...")
				self.needs_render = True

				headers = {
					'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
				}
				response = requests.get(url, headers=headers, timeout=10)
				response.raise_for_status()

				self.current_url = url
				self.base_url = url
				self.raw_html = response.text

				if url not in self.history:
					self.history.append(url)
					self.history_index = len(self.history) - 1

				self.parsed_content = BeautifulSoup(response.text, 'html.parser')
				self.parsed_content = self.clean_html(self.parsed_content)
				self.parse_elements()
				self.render_to_lines()
				self.set_status(f"✓ Página carregada: {url}")
				self.selected_element = 0
				self.scroll_offset = 0
				return True

			except requests.exceptions.RequestException as e:
				self.raw_html = f"Erro ao carregar {url}: {str(e)}"
				self.parsed_content = None
				self.elements = []
				self.content_lines = self.raw_html.split('\n')
				self.set_status(f"Erro: {str(e)[:50]}", True)
				return False

		def parse_elements(self):
			self.elements = []

			if not self.parsed_content:
				return

			# Links - apenas os que tem href
			for i, a in enumerate(self.parsed_content.find_all('a', href=True)):
				text = a.get_text(strip=True)
				href = a['href']
				if text and not href.startswith('javascript:'):
					self.elements.append({
						'id': f"link_{i}",
						'type': 'link',
						'text': text[:60],
						'href': href,
						'element': a,
						'y_pos': -1
					})

			# Botões
			for i, button in enumerate(self.parsed_content.find_all('button')):
				text = button.get_text(strip=True)
				if text:
					self.elements.append({
						'id': f"button_{i}",
						'type': 'button',
						'text': text[:60],
						'element': button,
						'y_pos': -1
					})

			# Inputs
			for i, input_field in enumerate(self.parsed_content.find_all('input')):
				input_type = input_field.get('type', 'text')
				if input_type not in ['hidden', 'submit', 'button']:
					name = input_field.get('name', f'input_{i}')
					placeholder = input_field.get('placeholder', '')
					value = input_field.get('value', '')

					self.elements.append({
						'id': f"input_{i}",
						'type': 'input',
						'input_type': input_type,
						'name': name,
						'placeholder': placeholder,
						'value': value,
						'text': f"[{input_type}] {placeholder or name}",
						'element': input_field,
						'y_pos': -1
					})

			# Imagens
			for i, img in enumerate(self.parsed_content.find_all('img')):
				src = img.get('src', '')
				alt = img.get('alt', '')
				if src and not src.startswith('data:'):
					self.elements.append({
						'id': f"img_{i}",
						'type': 'image',
						'src': src,
						'alt': alt or 'imagem',
						'text': f"[IMAGEM] {alt[:40] if alt else 'sem descrição'}",
						'element': img,
						'y_pos': -1
					})

		def get_visible_text(self, element):
			"""Extrai texto visível ignorando tags de script/style"""
			if element.name in ['script', 'style', 'noscript']:
				return ""
			return element.get_text(strip=True)

		def render_to_lines(self):
			"""Renderiza o HTML preservando a estrutura e posições"""
			self.content_lines = []
			self.content_positions = []

			if not self.parsed_content:
				self.content_lines = ["Sem conteúdo para exibir"]
				return

			h, w = self.stdscr.getmaxyx()
			content_width = w - 45 if w >= 80 else w - 2

			# Pega o body
			body = self.parsed_content.body
			if not body:
				body = self.parsed_content

			y_pos = 0
			element_index = 0

			def process_node(node, indent=0):
				nonlocal y_pos, element_index

				if node.name is None:
					# Texto puro
					text = str(node).strip()
					if text and not text.startswith('<'):
						lines = self.wrap_text(text, content_width - indent)
						for line in lines:
							if indent > 0:
								self.content_lines.append(' ' * indent + line)
							else:
								self.content_lines.append(line)
							y_pos += 1

				elif node.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
					text = self.get_visible_text(node)
					if text:
						level = int(node.name[1])
						prefix = '#' * level + ' '
						lines = self.wrap_text(prefix + text, content_width)
						for line in lines:
							# Centraliza títulos
							if len(line) < content_width:
								spaces = (content_width - len(line)) // 2
								line = ' ' * spaces + line
							self.content_lines.append(line)
							y_pos += 1
						self.content_lines.append('')
						y_pos += 1

				elif node.name == 'p':
					text = self.get_visible_text(node)
					if text:
						lines = self.wrap_text(text, content_width)
						for line in lines:
							self.content_lines.append(line)
							y_pos += 1
						self.content_lines.append('')
						y_pos += 1

				elif node.name == 'br':
					self.content_lines.append('')
					y_pos += 1

				elif node.name == 'hr':
					self.content_lines.append('─' * content_width)
					y_pos += 1

				elif node.name in ['ul', 'ol']:
					for i, li in enumerate(node.find_all('li', recursive=False)):
						text = self.get_visible_text(li)
						bullet = '•' if node.name == 'ul' else f'{i+1}.'
						lines = self.wrap_text(f"{bullet} {text}", content_width - 2)
						for line in lines:
							self.content_lines.append('  ' + line)
							y_pos += 1

				elif node.name == 'table':
					rows = node.find_all('tr')
					for row in rows:
						cols = row.find_all(['td', 'th'])
						if cols:
							row_text = []
							for col in cols:
								col_text = self.get_visible_text(col)[:15]
								row_text.append(col_text.ljust(15))
							self.content_lines.append(' '.join(row_text))
							y_pos += 1
					self.content_lines.append('')
					y_pos += 1

				elif node.name == 'a' and node.get('href'):
					# Links interativos
					text = self.get_visible_text(node)
					if text:
						if element_index < len(self.elements):
							self.elements[element_index]['y_pos'] = y_pos
							element_index += 1

						href = node.get('href', '')
						display_text = f"[ {text} ]"
						lines = self.wrap_text(display_text, content_width)
						for line in lines:
							self.content_lines.append(line)
							y_pos += 1

				elif node.name == 'button':
					text = self.get_visible_text(node)
					if text:
						if element_index < len(self.elements):
							self.elements[element_index]['y_pos'] = y_pos
							element_index += 1

						self.content_lines.append(f"[ {text} ]")
						y_pos += 1

				elif node.name == 'input':
					input_type = node.get('type', 'text')
					if input_type not in ['hidden']:
						if element_index < len(self.elements):
							self.elements[element_index]['y_pos'] = y_pos
							element_index += 1

						placeholder = node.get('placeholder', '')
						value = node.get('value', '')

						if input_type == 'checkbox':
							checked = 'x' if node.get('checked') else ' '
							self.content_lines.append(f'[{checked}] {placeholder}')
						elif input_type == 'radio':
							checked = '●' if node.get('checked') else '○'
							self.content_lines.append(f'{checked} {placeholder}')
						else:
							display = value or placeholder or '...'
							self.content_lines.append(f'[ {display[:30]} ]')
						y_pos += 1

				elif node.name == 'img':
					if element_index < len(self.elements):
						self.elements[element_index]['y_pos'] = y_pos
						element_index += 1

					alt = node.get('alt', '')
					self.content_lines.append(f'🖼️  {alt or "Imagem"}')
					y_pos += 1

				elif node.name == 'div':
					# Processa filhos de div
					for child in node.children:
						if child.name or (child.string and child.string.strip()):
							process_node(child, indent + 2)

				else:
					# Processa outros elementos
					for child in node.children:
						if child.name or (child.string and child.string.strip()):
							process_node(child, indent)

			# Processa o body
			for child in body.children:
				process_node(child)

			# Remove linhas vazias consecutivas
			cleaned_lines = []
			prev_empty = False
			for line in self.content_lines:
				if line.strip() == '':
					if not prev_empty:
						cleaned_lines.append('')
					prev_empty = True
				else:
					cleaned_lines.append(line)
					prev_empty = False

			self.content_lines = cleaned_lines

		def wrap_text(self, text, width):
			"""Quebra texto em linhas respeitando palavras"""
			if not text:
				return []

			lines = []
			words = text.split()
			current_line = ""

			for word in words:
				if len(current_line + " " + word) <= width:
					current_line += (" " + word if current_line else word)
				else:
					if current_line:
						lines.append(current_line)
					current_line = word

			if current_line:
				lines.append(current_line)

			return lines if lines else [text[:width]]

		def draw_header(self):
			h, w = self.stdscr.getmaxyx()
			if h < 5 or w < 60:
				self.stdscr.addstr(0, 0, "Terminal muito pequeno!")
				return

			url_display = self.current_url if self.current_url else "Nenhuma página"
			if len(url_display) > w - 20:
				url_display = url_display[:w-23] + "..."

			header = f" 🌐 Navegador TUI - {url_display} "
			hist_pos = f" [{self.history_index+1}/{len(self.history)}]" if self.history else ""

			try:
				if self.has_colors:
					self.stdscr.addstr(0, 0, header[:w-1], self.get_color_pair(1) | curses.A_BOLD)
					if hist_pos:
						self.stdscr.addstr(0, w-len(hist_pos)-1, hist_pos, self.get_color_pair(2))
					self.stdscr.addstr(1, 0, "─" * (w-1), self.get_color_pair(2))
				else:
					self.stdscr.addstr(0, 0, header[:w-1], curses.A_BOLD)
					if hist_pos:
						self.stdscr.addstr(0, w-len(hist_pos)-1, hist_pos)
					self.stdscr.addstr(1, 0, "─" * (w-1))
			except:
				pass

		def draw_content(self):
			h, w = self.stdscr.getmaxyx()
			start_y = 3
			max_lines = h - 5
			content_width = w - 45 if w >= 80 else w - 2

			content_x = 1 if w < 80 else 1
			menu_x = w - 44 if w >= 80 else w

			try:
				# Desenha conteúdo
				display_lines = self.content_lines[self.scroll_offset:self.scroll_offset + max_lines]

				for i, line in enumerate(display_lines):
					y = start_y + i
					if y >= h - 2:
						break

					# Verifica se esta linha contém elemento selecionado
					is_selected = False
					absolute_y = self.scroll_offset + i

					for elem in self.elements:
						if elem.get('y_pos') == absolute_y and self.elements.index(elem) == self.selected_element:
							is_selected = True
							break

					# Desenha com destaque se selecionado
					if is_selected and not self.input_mode:
						attr = self.get_color_pair(5) | curses.A_BOLD if self.has_colors else curses.A_REVERSE
						self.stdscr.addstr(y, content_x, line[:content_width], attr)
					else:
						self.stdscr.addstr(y, content_x, line[:content_width])

			except curses.error:
				pass

			# Indicador de scroll
			if len(self.content_lines) > max_lines:
				scroll_percent = self.scroll_offset / max(1, len(self.content_lines) - max_lines)
				scroll_pos = int(scroll_percent * (max_lines - 3))
				try:
					self.stdscr.addstr(start_y + scroll_pos, w-2, '█')
				except:
					pass

		def draw_elements_menu(self):
			h, w = self.stdscr.getmaxyx()
			if w < 80 or not self.elements:
				return

			menu_x = w - 44
			menu_y = 3
			menu_width = 43

			try:
				# Cabeçalho do menu
				if self.has_colors:
					self.stdscr.addstr(menu_y-1, menu_x, "┌" + "─" * (menu_width-2) + "┐", self.get_color_pair(2))
					self.stdscr.addstr(menu_y, menu_x, "│ 📋 ELEMENTOS " + " " * (menu_width-16) + "│", self.get_color_pair(1))
					self.stdscr.addstr(menu_y+1, menu_x, "├" + "─" * (menu_width-2) + "┤", self.get_color_pair(2))
				else:
					self.stdscr.addstr(menu_y-1, menu_x, "+" + "-" * (menu_width-2) + "+")
					self.stdscr.addstr(menu_y, menu_x, "| ELEMENTOS " + " " * (menu_width-13) + "|")
					self.stdscr.addstr(menu_y+1, menu_x, "+" + "-" * (menu_width-2) + "+")

				# Lista de elementos
				visible_elements = self.elements[:h-10]
				for i, element in enumerate(visible_elements):
					y = menu_y + 2 + i
					if y >= h-3:
						break

					if element['type'] == 'link':
						icon = '🔗'
						color = self.get_color_pair(7)
					elif element['type'] == 'button':
						icon = '🖱️'
						color = self.get_color_pair(8)
					elif element['type'] == 'input':
						icon = '📝'
						color = self.get_color_pair(3)
					elif element['type'] == 'image':
						icon = '🖼️'
						color = self.get_color_pair(4)
					else:
						icon = '•'
						color = 0

					if i == self.selected_element:
						prefix = '▶ '
						attr = self.get_color_pair(5) | curses.A_BOLD if self.has_colors else curses.A_REVERSE
					else:
						prefix = '  '
						attr = color if self.has_colors else 0

					text = f"{prefix}{icon} {element['text'][:35]}"
					self.stdscr.addstr(y, menu_x + 2, text[:menu_width-4], attr)

				# Rodapé do menu
				footer_y = menu_y + 2 + len(visible_elements)
				if footer_y < h-2:
					if self.has_colors:
						self.stdscr.addstr(footer_y, menu_x, "└" + "─" * (menu_width-2) + "┘", self.get_color_pair(2))
					else:
						self.stdscr.addstr(footer_y, menu_x, "+" + "-" * (menu_width-2) + "+")

			except curses.error:
				pass

		def draw_footer(self):
			h, w = self.stdscr.getmaxyx()
			if h < 5:
				return

			# Status
			if self.status_message and self.status_timer > 0:
				try:
					status_color = self.get_color_pair(4) if self.status_is_error else self.get_color_pair(3)
					self.stdscr.addstr(h-3, 1, f" {self.status_message} "[:w-3], status_color | curses.A_BOLD)
				except:
					pass

			# Comandos
			footer = " [Q]Sair [U]URL [↑↓]Rolar [Tab]Sel [Enter]Abrir [M]Mouse [R]Recarregar"
			if self.mouse.enabled:
				footer += f" [X:{self.mouse.x} Y:{self.mouse.y}]"

			try:
				if self.has_colors:
					self.stdscr.addstr(h-2, 0, "─" * (w-1), self.get_color_pair(2))
					self.stdscr.addstr(h-1, 0, footer[:w-1], self.get_color_pair(3))
				else:
					self.stdscr.addstr(h-2, 0, "-" * (w-1))
					self.stdscr.addstr(h-1, 0, footer[:w-1])
			except:
				pass

		def draw_mouse_cursor(self):
			if self.mouse.enabled:
				try:
					h, w = self.stdscr.getmaxyx()
					if 0 <= self.mouse.x < w and 0 <= self.mouse.y < h:
						try:
							current_char = self.stdscr.inch(self.mouse.y, self.mouse.x) & 0xFF
							if current_char == ord(' '):
								cursor_char = '·'
							else:
								cursor_char = chr(current_char)
						except:
							cursor_char = '·'

						if self.has_colors:
							self.stdscr.addstr(self.mouse.y, self.mouse.x, cursor_char, 
											 self.get_color_pair(6) | curses.A_REVERSE)
						else:
							self.stdscr.addstr(self.mouse.y, self.mouse.x, cursor_char, 
											 curses.A_REVERSE)
				except:
					pass

		def handle_mouse(self):
			if not self.mouse.enabled:
				return False

			try:
				mouse_event = self.stdscr.getmouse()
				if not mouse_event:
					return False

				id, x, y, z, bstate = mouse_event

				self.mouse.x = x
				self.mouse.y = y

				if bstate & curses.BUTTON1_CLICKED or bstate & curses.BUTTON1_PRESSED:
					self.mouse.click(x, y)
					self.check_mouse_click(x, y)
				else:
					self.mouse.release()

				if bstate & curses.BUTTON4_PRESSED:
					self.scroll_offset = max(0, self.scroll_offset - 3)
				if bstate & curses.BUTTON5_PRESSED:
					self.scroll_offset += 3

				return True

			except curses.error:
				return False
			except Exception:
				return False

		def check_mouse_click(self, x, y):
			h, w = self.stdscr.getmaxyx()
			menu_x = w - 44

			# Clique no menu
			if menu_x <= x < w:
				element_index = y - 5
				if 0 <= element_index < len(self.elements):
					self.selected_element = element_index
					self.activate_element(self.elements[element_index])
					return

			# Clique no conteúdo
			content_y = y - 3
			if content_y >= 0:
				absolute_y = self.scroll_offset + content_y
				for i, elem in enumerate(self.elements):
					if elem.get('y_pos') == absolute_y:
						self.selected_element = i
						self.activate_element(elem)
						break

		def activate_element(self, element):
			try:
				if element['type'] == 'link':
					href = element['href']
					if href and not href.startswith('javascript:'):
						full_url = urljoin(self.base_url, href)
						self.fetch_url(full_url)
					else:
						self.set_status("Link sem destino válido")

				elif element['type'] == 'button':
					self.set_status(f"✓ Botão clicado: {element['text']}")
					self.needs_render = True

				elif element['type'] == 'input':
					self.input_mode = True
					self.input_element = element
					self.input_text = element.get('value', '')
					self.input_field_index = self.elements.index(element)
					self.set_status("✏️ Digite e pressione ENTER (ESC cancela)")

				elif element['type'] == 'image':
					src = element['src']
					if src and not src.startswith('data:'):
						full_url = urljoin(self.base_url, src)
						self.set_status(f"Carregando imagem...")
						ascii_img = self.url_to_ascii(full_url)
						if ascii_img:
							self.content_lines = ascii_img.split('\n')
							self.set_status("✓ Imagem convertida para ASCII")
						else:
							self.set_status("✗ Falha ao carregar imagem", True)

			except Exception as e:
				self.set_status(f"Erro: {str(e)[:30]}", True)

		def url_to_ascii(self, url):
			try:
				response = requests.get(url, stream=True, timeout=5)
				img = Image.open(io.BytesIO(response.content))

				if img.mode != 'L':
					img = img.convert('L')

				h, w = self.stdscr.getmaxyx()
				max_width = w - 45 if w >= 80 else w - 2
				aspect = img.height / img.width
				new_width = min(max_width, 60)
				new_height = int(new_width * aspect * 0.5)
				img = img.resize((new_width, new_height))

				chars = [' ', '.', ',', ':', ';', '+', '*', '#', '%', '@']
				art = []

				for y in range(new_height):
					line = ''
					for x in range(new_width):
						pixel = img.getpixel((x, y))
						idx = pixel // 25
						line += chars[min(idx, 9)]
					art.append(line)

				return '\n'.join(art)

			except Exception:
				return None

		def handle_input(self, key):
			if key == 27:
				self.input_mode = False
				self.input_text = ""
				self.input_element = None
				self.input_field_index = -1
				self.set_status("✖ Input cancelado")

			elif key == ord('\n') or key == ord('\r'):
				if self.input_element:
					self.input_element['value'] = self.input_text

					if self.input_field_index >= 0:
						self.elements[self.input_field_index]['value'] = self.input_text
						self.elements[self.input_field_index]['text'] = f"[{self.input_element['input_type']}] {self.input_text or self.input_element['placeholder']}"

					self.set_status(f"✓ Input: {self.input_text[:30]}")

				self.input_mode = False
				self.input_text = ""
				self.input_element = None
				self.input_field_index = -1
				self.needs_render = True

			elif key == curses.KEY_BACKSPACE or key == 127 or key == 8:
				self.input_text = self.input_text[:-1]

			elif 32 <= key <= 126:
				self.input_text += chr(key)

		def run(self):
			self.init_curses()
			self.fetch_url("example.com")

			while True:
				try:
					if self.needs_render and self.parsed_content:
						self.render_to_lines()
						self.needs_render = False

					self.stdscr.clear()
					self.draw_header()
					self.draw_content()
					self.draw_elements_menu()
					self.draw_footer()
					self.draw_mouse_cursor()
					self.stdscr.refresh()

					if self.status_timer > 0:
						self.status_timer -= 1
					else:
						self.status_message = ""

					key = self.stdscr.getch()

					if key == curses.KEY_MOUSE:
						self.handle_mouse()
						continue

					if key == ord('q'):
						break

					elif key == ord('u'):
						self.cleanup_curses()
						try:
							url = input("\nDigite a URL: ").strip()
						except:
							url = ""
						self.init_curses()
						if url:
							self.fetch_url(url)

					elif key == ord('m'):
						self.mouse.enabled = not self.mouse.enabled
						if self.mouse.enabled:
							try:
								curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
								self.set_status("✓ Mouse ativado")
							except:
								self.mouse.enabled = False
								self.set_status("✗ Mouse não suportado", True)
						else:
							self.set_status("✗ Mouse desativado")

					elif key == ord('\t'):
						if self.elements:
							self.selected_element = (self.selected_element + 1) % len(self.elements)
							self.set_status(f"Elemento {self.selected_element + 1} selecionado")

					elif key == curses.KEY_UP:
						self.scroll_offset = max(0, self.scroll_offset - 1)
						if self.elements and not self.input_mode:
							self.selected_element = (self.selected_element - 1) % len(self.elements)

					elif key == curses.KEY_DOWN:
						self.scroll_offset += 1
						if self.elements and not self.input_mode:
							self.selected_element = (self.selected_element + 1) % len(self.elements)

					elif key == curses.KEY_PPAGE:
						self.scroll_offset = max(0, self.scroll_offset - 20)

					elif key == curses.KEY_NPAGE:
						self.scroll_offset += 20

					elif key == curses.KEY_LEFT:
						if self.history_index > 0:
							self.history_index -= 1
							self.fetch_url(self.history[self.history_index])

					elif key == curses.KEY_RIGHT:
						if self.history_index < len(self.history) - 1:
							self.history_index += 1
							self.fetch_url(self.history[self.history_index])

					elif key == ord('r') or key == ord('R'):
						if self.current_url:
							self.fetch_url(self.current_url)

					elif key == ord('\n') or key == ord('\r'):
						if self.elements and self.selected_element < len(self.elements) and not self.input_mode:
							self.activate_element(self.elements[self.selected_element])

					elif self.input_mode:
						self.handle_input(key)

					max_scroll = max(0, len(self.content_lines) - (self.stdscr.getmaxyx()[0] - 5))
					self.scroll_offset = max(0, min(self.scroll_offset, max_scroll))

				except KeyboardInterrupt:
					break
				except Exception as e:
					self.set_status(f"Erro: {str(e)[:30]}", True)

			self.cleanup_curses()

	browser = TUIBrowser()
	browser.run()


def taskmgr():
	"""
	Abre um gerenciador de tarefas com menu para Linux
	"""
	import subprocess
	import os
	import signal
	import time

	class GerenciadorTarefasLinux:
		def __init__(self):
			self.executando = True

		def _executar_comando(self, comando):
			"""Executa comando Linux e retorna resultado"""
			try:
				resultado = subprocess.run(
					comando,
					shell=True,
					capture_output=True,
					text=True,
					encoding='utf-8',
					errors='ignore'
				)
				if resultado.returncode == 0:
					return resultado.stdout.strip()
				else:
					return f"Erro: {resultado.stderr.strip()}"
			except Exception as e:
				return f"Erro: {str(e)}"

		def limpar_tela(self):
			"""Limpa a tela do terminal"""
			os.system('clear')

		def mostrar_cabecalho(self):
			"""Mostra cabeçalho do menu"""
			print("╔════════════════════════════════════════════╗")
			print("║	 GERENCIADOR DE TAREFAS - LINUX		║")
			print("╚════════════════════════════════════════════╝")

		def mostrar_menu(self):
			"""Mostra o menu principal"""
			print("\n=== MENU PRINCIPAL ===")
			print("1. Listar todos os processos")
			print("2. Ver top processos (CPU)")
			print("3. Ver top processos (Memória)")
			print("4. Buscar processo por nome")
			print("5. Matar processo por PID")
			print("6. Matar processo por nome")
			print("7. Ver informações do sistema")
			print("8. Ver árvore de processos")
			print("9. Ver processos por usuário")
			print("10. Encontrar processo por porta")
			print("11. Iniciar novo processo")
			print("0. Sair")
			print("=" * 40)

		def listar_processos(self):
			"""Lista todos os processos usando ps"""
			self.limpar_tela()
			self.mostrar_cabecalho()
			print("\n=== LISTA DE PROCESSOS ===")
			print("Mostrando os 20 processos mais ativos...\n")

			# Executa ps aux ordenado por CPU
			saida = self._executar_comando('ps aux --sort=-%cpu | head -30')

			if saida.startswith('Erro'):
				print("Erro ao listar processos!")
				input("\nPressione Enter para continuar...")
				return

			# Mostra a saída formatada
			linhas = saida.split('\n')

			if len(linhas) > 0:
				# Cabeçalho
				cabecalho = linhas[0]
				print(cabecalho)
				print("-" * min(100, len(cabecalho) + 20))

				# Dados
				for linha in linhas[1:]:
					if linha.strip():
						# Formata a linha para melhor visualização
						partes = linha.split(None, 10)  # Divide em no máximo 11 partes
						if len(partes) >= 11:
							usuario = partes[0][:10].ljust(10)
							pid = partes[1].rjust(6)
							cpu = partes[2].rjust(6)
							mem = partes[3].rjust(6)
							comando = partes[10][:50] + "..." if len(partes[10]) > 50 else partes[10]
							print(f"{usuario} {pid} {cpu}% {mem}% {comando}")
						else:
							print(linha[:100])  # Mostra até 100 caracteres
			else:
				print("Nenhum processo encontrado!")

			print(f"\nTotal de processos mostrados: {len(linhas) - 1 if len(linhas) > 1 else 0}")

			input("\nPressione Enter para voltar ao menu...")

		def top_cpu(self):
			"""Mostra top processos por CPU"""
			self.limpar_tela()
			self.mostrar_cabecalho()
			print("\n=== TOP PROCESSOS - CPU ===")
			print("Processos que mais usam CPU:\n")

			saida = self._executar_comando('ps aux --sort=-%cpu | head -20')

			if saida.startswith('Erro'):
				print("Erro ao obter processos!")
			else:
				print(saida)

			input("\nPressione Enter para continuar...")

		def top_memoria(self):
			"""Mostra top processos por memória"""
			self.limpar_tela()
			self.mostrar_cabecalho()
			print("\n=== TOP PROCESSOS - MEMÓRIA ===")
			print("Processos que mais usam memória:\n")

			saida = self._executar_comando('ps aux --sort=-%mem | head -20')

			if saida.startswith('Erro'):
				print("Erro ao obter processos!")
			else:
				print(saida)

			input("\nPressione Enter para continuar...")

		def buscar_por_nome(self):
			"""Busca processos por nome"""
			self.limpar_tela()
			self.mostrar_cabecalho()
			print("\n=== BUSCAR PROCESSO POR NOME ===")

			nome = input("Digite parte do nome do processo: ").strip()
			if not nome:
				print("Nome não pode ser vazio!")
				input("\nPressione Enter para continuar...")
				return

			print(f"\nBuscando processos com '{nome}'...\n")
			saida = self._executar_comando(f'ps aux | grep -i "{nome}" | grep -v grep | head -30')

			if saida and not saida.startswith('Erro'):
				print(f"Processos encontrados com '{nome}':")
				print("-" * 60)
				print(saida)
			else:
				print(f"Nenhum processo encontrado com '{nome}'")

			input("\nPressione Enter para continuar...")

		def matar_por_pid(self):
			"""Mata processo por PID"""
			self.limpar_tela()
			self.mostrar_cabecalho()
			print("\n=== MATAR PROCESSO POR PID ===")

			try:
				pid = input("Digite o PID do processo: ").strip()
				if not pid.isdigit():
					print("PID deve ser um número!")
					input("\nPressione Enter para continuar...")
					return

				pid_int = int(pid)

				# Primeiro mostra informações do processo
				print(f"\nObtendo informações do processo {pid_int}...")
				info = self._executar_comando(f'ps -p {pid_int} -o pid,user,%cpu,%mem,command 2>/dev/null')

				if not info or 'PID' not in info:
					print(f"Processo com PID {pid_int} não encontrado!")
					input("\nPressione Enter para continuar...")
					return

				print(f"\nProcesso encontrado:")
				print(info)

				confirmar = input(f"\nTem certeza que deseja matar o processo {pid_int}? (s/N): ").strip().lower()

				if confirmar == 's':
					print(f"\nEncerrando processo {pid_int}...")

					# Tenta SIGTERM primeiro (terminação graciosa)
					try:
						os.kill(pid_int, signal.SIGTERM)
						time.sleep(1)

						# Verifica se processo ainda existe
						verifica = self._executar_comando(f'ps -p {pid_int} 2>/dev/null')
						if verifica and str(pid_int) in verifica:
							# Se ainda existe, força com SIGKILL
							os.kill(pid_int, signal.SIGKILL)
							time.sleep(0.5)
							print(f"Processo {pid_int} forçado a terminar (SIGKILL)")
						else:
							print(f"Processo {pid_int} terminado graciosamente (SIGTERM)")

					except ProcessLookupError:
						print(f"Processo {pid_int} não encontrado (já foi encerrado)")
					except PermissionError:
						print(f"Permissão negada para encerrar processo {pid_int}!")
						print("Tente executar este programa com sudo.")
					except Exception as e:
						print(f"Erro ao encerrar processo: {e}")
				else:
					print("Operação cancelada!")

			except ValueError:
				print("PID inválido!")
			except Exception as e:
				print(f"Erro: {str(e)}")

			input("\nPressione Enter para continuar...")

		def matar_por_nome(self):
			"""Mata processos por nome"""
			self.limpar_tela()
			self.mostrar_cabecalho()
			print("\n=== MATAR PROCESSOS POR NOME ===")

			nome = input("Digite parte do nome do processo: ").strip()
			if not nome:
				print("Nome não pode ser vazio!")
				input("\nPressione Enter para continuar...")
				return

			# Primeiro mostra os processos
			print(f"\nBuscando processos com '{nome}'...")
			saida = self._executar_comando(f'ps aux | grep -i "{nome}" | grep -v grep | head -20')

			if not saida or saida.startswith('Erro'):
				print(f"Nenhum processo encontrado com '{nome}'")
				input("\nPressione Enter para continuar...")
				return

			print(f"\nProcessos encontrados com '{nome}':")
			print("-" * 80)
			print(saida)
			print("-" * 80)

			confirmar = input(f"\nTem certeza que deseja matar TODOS estes processos? (s/N): ").strip().lower()

			if confirmar == 's':
				# Extrai PIDs
				linhas = saida.split('\n')
				pids_mortos = []

				for linha in linhas:
					if linha.strip():
						partes = linha.split(None, 10)
						if len(partes) >= 2 and partes[1].isdigit():
							pid = int(partes[1])
							try:
								# Tenta SIGTERM primeiro
								os.kill(pid, signal.SIGTERM)
								time.sleep(0.1)

								# Se ainda existe, força com SIGKILL
								if self._executar_comando(f'ps -p {pid} 2>/dev/null'):
									os.kill(pid, signal.SIGKILL)

								pids_mortos.append(pid)
								print(f"✓ Processo {pid} ({partes[10][:30]}...) encerrado")
							except ProcessLookupError:
								print(f"✗ Processo {pid} já estava encerrado")
							except PermissionError:
								print(f"✗ Permissão negada para processo {pid}")
							except Exception:
								print(f"✗ Erro ao encerrar processo {pid}")

				print(f"\nTotal de processos mortos: {len(pids_mortos)}")
			else:
				print("Operação cancelada!")

			input("\nPressione Enter para continuar...")

		def info_sistema(self):
			"""Mostra informações do sistema"""
			self.limpar_tela()
			self.mostrar_cabecalho()
			print("\n=== INFORMAÇÕES DO SISTEMA ===")

			# Memória
			print("\n--- MEMÓRIA ---")
			memoria = self._executar_comando('free -h')
			if memoria and not memoria.startswith('Erro'):
				print(memoria)
			else:
				print("Não foi possível obter informações de memória")

			# CPU - Corrigindo a string com escape
			print("\n--- CPU ---")
			# Usando regex sem o escape problemático
			cpu_info = self._executar_comando('lscpu | grep -E "Model name|CPU.s.|CPU MHz" | head -3')
			if cpu_info and not cpu_info.startswith('Erro'):
				print(cpu_info)
			else:
				# Tenta alternativa
				cpu_alt = self._executar_comando('cat /proc/cpuinfo | grep -E "model name|cpu cores" | head -3')
				if cpu_alt:
					print(cpu_alt)
				else:
					print("Não foi possível obter informações da CPU")

			# Uptime
			print("\n--- UPTIME ---")
			uptime = self._executar_comando('uptime')
			if uptime and not uptime.startswith('Erro'):
				print(uptime)
			else:
				print("Não foi possível obter uptime")

			# Load average
			print("\n--- LOAD AVERAGE ---")
			load = self._executar_comando('cat /proc/loadavg')
			if load and not load.startswith('Erro'):
				print(f"Load average: {load}")

			# Disco
			print("\n--- USO DE DISCO ---")
			disco = self._executar_comando('df -h / | tail -1')
			if disco and not disco.startswith('Erro'):
				print(f"Disco raiz (/): {disco}")

			# Processos
			print("\n--- RESUMO DE PROCESSOS ---")
			proc_count = self._executar_comando('ps aux | wc -l')
			if proc_count and proc_count.isdigit():
				print(f"Processos em execução: {int(proc_count) - 1}")

			input("\nPressione Enter para continuar...")

		def arvore_processos(self):
			"""Mostra árvore de processos"""
			self.limpar_tela()
			self.mostrar_cabecalho()
			print("\n=== ÁRVORE DE PROCESSOS ===")
			print("Mostrando hierarquia de processos...\n")

			# Tenta pstree, se não existir, usa ps com formato de árvore
			arvore = self._executar_comando('which pstree && pstree -p || ps auxf --forest')

			if arvore and not arvore.startswith('Erro'):
				# Limita a saída para não sobrecarregar o terminal
				linhas = arvore.split('\n')
				for linha in linhas[:40]:  # Mostra apenas as primeiras 40 linhas
					print(linha)

				if len(linhas) > 40:
					print(f"\n... e mais {len(linhas) - 40} linhas (saída truncada)")
			else:
				print("Não foi possível obter a árvore de processos")

			input("\nPressione Enter para continuar...")

		def processos_usuario(self):
			"""Mostra processos de um usuário"""
			self.limpar_tela()
			self.mostrar_cabecalho()
			print("\n=== PROCESSOS POR USUÁRIO ===")

			usuario_atual = os.getlogin()
			usuario = input(f"Digite o nome do usuário (deixe vazio para '{usuario_atual}'): ").strip()
			if not usuario:
				usuario = usuario_atual

			print(f"\nProcessos do usuário '{usuario}':\n")
			processos = self._executar_comando(f'ps -u {usuario} -o pid,%cpu,%mem,command --sort=-%cpu | head -30')

			if processos and not processos.startswith('Erro'):
				print(processos)
			else:
				print(f"Não foi possível obter processos do usuário '{usuario}'")
				print("Ou o usuário não existe ou não tem processos em execução.")

			input("\nPressione Enter para continuar...")

		def processo_por_porta(self):
			"""Encontra processo por porta"""
			self.limpar_tela()
			self.mostrar_cabecalho()
			print("\n=== PROCESSO POR PORTA ===")

			porta = input("Digite o número da porta: ").strip()
			if not porta.isdigit():
				print("Porta deve ser um número!")
				input("\nPressione Enter para continuar...")
				return

			print(f"\nBuscando processo usando porta {porta}...\n")
			processo = self._executar_comando(f'sudo lsof -i :{porta} 2>/dev/null || lsof -i :{porta} 2>/dev/null')

			if processo and not processo.startswith('Erro'):
				print(f"Processo(s) usando porta {porta}:")
				print(processo)
			else:
				print(f"Nenhum processo usando porta {porta}")
				print("Ou você não tem permissão para ver (tente executar com sudo)")

			input("\nPressione Enter para continuar...")

		def iniciar_processo(self):
			"""Inicia um novo processo"""
			self.limpar_tela()
			self.mostrar_cabecalho()
			print("\n=== INICIAR NOVO PROCESSO ===")

			comando = input("Digite o comando para executar: ").strip()
			if not comando:
				print("Comando não pode ser vazio!")
				input("\nPressione Enter para continuar...")
				return

			background = input("Executar em background? (s/N): ").strip().lower() == 's'

			try:
				if background:
					print(f"\nExecutando em background: {comando}")
					processo = subprocess.Popen(
						comando,
						shell=True,
						stdout=subprocess.DEVNULL,
						stderr=subprocess.DEVNULL,
						start_new_session=True
					)
					print(f"✓ Processo iniciado em background")
					print(f"  PID: {processo.pid}")
					print(f"  Comando: {comando[:50]}{'...' if len(comando) > 50 else ''}")
				else:
					print(f"\nExecutando: {comando}")
					print("-" * 60)

					# Executa e captura saída em tempo real
					processo = subprocess.Popen(
						comando,
						shell=True,
						stdout=subprocess.PIPE,
						stderr=subprocess.STDOUT,
						text=True,
						bufsize=1,
						universal_newlines=True
					)

					# Mostra saída em tempo real
					for linha in processo.stdout:
						print(linha.rstrip())

					processo.wait()
					print("-" * 60)
					print(f"\n✓ Processo finalizado")
					print(f"  Código de saída: {processo.returncode}")

			except KeyboardInterrupt:
				print("\n\n✗ Processo interrompido pelo usuário")
			except FileNotFoundError:
				print(f"\n✗ Comando não encontrado: {comando}")
			except Exception as e:
				print(f"\n✗ Erro: {str(e)}")

			input("\nPressione Enter para continuar...")

		def executar(self):
			"""Loop principal do gerenciador"""
			while self.executando:
				self.limpar_tela()
				self.mostrar_cabecalho()
				self.mostrar_menu()

				try:
					opcao = input("\nEscolha uma opção: ").strip()

					if opcao == '0':
						print("\nSaindo do gerenciador de tarefas...")
						time.sleep(1)
						self.executando = False

					elif opcao == '1':
						self.listar_processos()

					elif opcao == '2':
						self.top_cpu()

					elif opcao == '3':
						self.top_memoria()

					elif opcao == '4':
						self.buscar_por_nome()

					elif opcao == '5':
						self.matar_por_pid()

					elif opcao == '6':
						self.matar_por_nome()

					elif opcao == '7':
						self.info_sistema()

					elif opcao == '8':
						self.arvore_processos()

					elif opcao == '9':
						self.processos_usuario()

					elif opcao == '10':
						self.processo_por_porta()

					elif opcao == '11':
						self.iniciar_processo()

					else:
						print("Opção inválida! Pressione Enter para tentar novamente.")
						input()

				except KeyboardInterrupt:
					print("\n\nSaindo do gerenciador de tarefas...")
					time.sleep(1)
					self.executando = False
				except Exception as e:
					print(f"\nErro inesperado: {e}")
					input("Pressione Enter para continuar...")

	# Cria e executa o gerenciador
	gerenciador = GerenciadorTarefasLinux()
	gerenciador.executar()




def messages():
	"""
	Abre um app de mensagens P2P para 2 pessoas com nomes de usuário
	"""
	import socket
	import threading
	import time
	import os

	# Configurações
	HOST = '0.0.0.0'
	PORT = 8888

	def limpar_tela():
		os.system('cls' if os.name == 'nt' else 'clear')

	def exibir_chat(historico, meu_nome, outro_nome):
		"""Exibe a interface do chat"""
		limpar_tela()
		print("═" * 50)
		print(f"💬 CHAT: {meu_nome} ↔ {outro_nome}")
		print("═" * 50)

		if not historico:
			print("\n✨ Comece a conversar! ✨")

		for remetente, mensagem, hora in historico:
			if remetente == meu_nome:
				print(f"\033[92m[{hora}] {meu_nome}: {mensagem}\033[0m")
			else:
				print(f"\033[96m[{hora}] {outro_nome}: {mensagem}\033[0m")

		print("─" * 50)
		print("Digite sua mensagem ou '/sair' para encerrar")
		print("═" * 50)

	def obter_nome_usuario():
		"""Obtém o nome do usuário"""
		while True:
			nome = input("Digite seu nome de usuário: ").strip()
			if nome:
				return nome
			print("❌ Nome inválido. Tente novamente.")

	def servidor():
		"""Modo servidor - espera conexão"""
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind((HOST, PORT))
		sock.listen(1)

		limpar_tela()
		print("═" * 50)
		print("🕐 AGUARDANDO CONEXÃO...")
		print(f"Endereço: {HOST}:{PORT}")
		print("═" * 50)

		conn, addr = sock.accept()

		# Trocar nomes de usuário
		meu_nome = obter_nome_usuario()
		conn.send(meu_nome.encode('utf-8'))
		outro_nome = conn.recv(1024).decode('utf-8')

		return conn, sock, meu_nome, outro_nome

	def cliente():
		"""Modo cliente - conecta ao servidor"""
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		limpar_tela()
		print("═" * 50)
		print("🔗 CONECTANDO AO SERVIDOR...")
		print("═" * 50)

		# Tentar conectar
		tentativas = 0
		while tentativas < 5:
			try:
				sock.connect((HOST, PORT))
				break
			except:
				tentativas += 1
				print(f"Tentativa {tentativas}/5...")
				time.sleep(2)
		else:
			print("❌ Não foi possível conectar ao servidor")
			return None, None, None, None

		# Trocar nomes de usuário
		outro_nome = sock.recv(1024).decode('utf-8')
		meu_nome = obter_nome_usuario()
		sock.send(meu_nome.encode('utf-8'))

		return sock, None, meu_nome, outro_nome

	def chat(conn, sock_server, meu_nome, outro_nome):
		"""Loop principal do chat"""
		from datetime import datetime
		historico = []

		def receber_mensagens():
			"""Thread para receber mensagens"""
			while True:
				try:
					data = conn.recv(1024).decode('utf-8')
					if not data:
						break

					hora_atual = datetime.now().strftime("%H:%M:%S")

					if data == "/sair":
						historico.append((outro_nome, "🚪 Saiu do chat", hora_atual))
						exibir_chat(historico, meu_nome, outro_nome)
						break

					historico.append((outro_nome, data, hora_atual))
					exibir_chat(historico, meu_nome, outro_nome)

				except:
					break

		# Iniciar thread de recebimento
		recv_thread = threading.Thread(target=receber_mensagens, daemon=True)
		recv_thread.start()

		# Mensagem de boas-vindas
		hora_inicio = datetime.now().strftime("%H:%M:%S")
		historico.append(("Sistema", f"✅ Chat iniciado às {hora_inicio}", hora_inicio))

		# Loop para enviar mensagens
		while True:
			exibir_chat(historico, meu_nome, outro_nome)

			try:
				mensagem = input(f"{meu_nome}> ").strip()
			except:
				break

			if not mensagem:
				continue

			if mensagem.lower() == '/sair':
				hora_saida = datetime.now().strftime("%H:%M:%S")
				historico.append((meu_nome, "🚪 Saindo do chat...", hora_saida))
				conn.send("/sair".encode('utf-8'))
				exibir_chat(historico, meu_nome, outro_nome)
				time.sleep(2)
				break

			hora_envio = datetime.now().strftime("%H:%M:%S")
			historico.append((meu_nome, mensagem, hora_envio))

			try:
				conn.send(mensagem.encode('utf-8'))
			except:
				historico.append(("Sistema", "❌ Erro ao enviar mensagem", hora_envio))
				break

		# Limpeza
		conn.close()
		if sock_server:
			sock_server.close()

	# ============== INÍCIO DO APLICATIVO ==============
	limpar_tela()
	print("═" * 50)
	print("💬 BEM-VINDO AO CHAT P2P")
	print("═" * 50)

	# Escolher modo
	print("\nEscolha o modo:")
	print("1. Criar sala (Aguardar outra pessoa)")
	print("2. Entrar em sala existente")
	print("3. Sair")

	while True:
		try:
			opcao = input("\nOpção (1/2/3): ").strip()

			if opcao == '1':
				conn, sock, meu_nome, outro_nome = servidor()
				if conn:
					chat(conn, sock, meu_nome, outro_nome)
				break

			elif opcao == '2':
				conn, sock, meu_nome, outro_nome = cliente()
				if conn:
					chat(conn, sock, meu_nome, outro_nome)
				break

			elif opcao == '3':
				print("\nAté logo! 👋")
				break

			else:
				print("❌ Opção inválida. Escolha 1, 2 ou 3.")

		except KeyboardInterrupt:
			print("\n\nChat interrompido pelo usuário.")
			break
		except Exception as e:
			print(f"\n❌ Erro: {e}")
			break



def images():
		sys.path.insert(0, "./pyOS/systemRes")
		od = os.getcwd
		import ascii_image_display as aid
		print("1. ver fotos\n2. visualizar fotos\n0. sair")
		escolha = input("escolha: ")
		if escolha == "1":
				os.chdir("imgs/")
				os.listdir()
				os.chdir("..")
				input("aperte enter para sair")
		elif escolha == "2":
				caminho = "imgs/"+ input("foto(apenas o arquivo nome com extensão): ")
				aid.display_ascii_image(caminho)
				input("aperte enter para sair")
		elif escolha == "0":
				os.chdir(od)
				return





def sysmgr():
		print(f"pyOS {version} - {os.getcwd()} running as pid {os.getpid()}")
		while True:
				print("1. permissoes\n2. senha\n3. arquivos temp.\n4. processos\n0. sair\n")
				esco = input("numero da opçao: ")
				if esco == "1":
						diret = input("diretorio/arquivo: ")
						perm = input("permissão(chmod): ")
						recur = input("recursivo?(s/n): ")
						if recur == "s":
								os.system(f"chmod -R {perm} {diret}")
						else:
								os.system(f"chmod {perm} {diret}")
				elif esco == "2":
						print("1. alterar\n2. alterar configuracao\n")
						esco2 = input("escolha: ")
						if esco2 == "1":
								with open("senha.txt", "w") as senha:
										senha.write(input("nova senha: "))
						elif esco2 == "2":
								with open("passwordexist.txt", "w") as newcfg:
										esco2_2 = input("s/n: ")
										if esco2_2 == "s":
												newcfg.write("True")
										else:
												newcfg.write("False")
				elif esco == "3":
						print(os.listdir("./pyOS/system/tmp"))
				elif esco == "4":
						print(str(os.listdir("./pyOS/proc")) + "\n")
						print("1. matar\n2. editar pid\n3. editar nome\n0. sair\n")
						esco3 = input("escolha: ")
						if esco3 == "1":
								pid = input("pid: ")
								shutil.rmtree("./pyOS/proc/" + pid)
						elif esco3 == "2":
								pid_at = input("pid: ")
								pid_no = input("novo pid: ")
								os.rename("./pyOS/proc/" + pid_at, "./pyOS/proc/" + pid_no)
						elif esco3 == "3":
								pid = input("pid: ")
								with open(f"./pyOS/proc/{pid}/nome.txt", "w") as name:
										name.write(input("nome novo: "))
						elif esco3 == "0":
								pass
				elif esco == "0":
						break





def diagnosticar_rede():
	from datetime import datetime
	"""
	Função para diagnosticar problemas de rede e sugerir soluções
	"""
	problemas_detectados = []
	solucoes_sugeridas = []

	print(Fore.CYAN + "🔍 Iniciando diagnóstico de rede..." + Style.RESET_ALL)
	time.sleep(1)

	# 1. Verificar conectividade com a internet
	print(Fore.YELLOW + "📡 Testando conectividade com a internet..." + Style.RESET_ALL)
	try:
		resposta = requests.get("https://www.google.com", timeout=10)
		if resposta.status_code == 200:
			print(Fore.GREEN + "✅ Conectividade com a internet: OK" + Style.RESET_ALL)
		else:
			problemas_detectados.append("Problema de conectividade com sites externos")
			solucoes_sugeridas.append("Verifique se o firewall não está bloqueando a conexão")
	except requests.exceptions.RequestException as e:
		problemas_detectados.append(f"Sem conexão com a internet: {str(e)}")
		solucoes_sugeridas.append("Verifique seu modem/roteador e cabos de rede")

	# 2. Verificar DNS
	print(Fore.YELLOW + "🌐 Testando resolução DNS..." + Style.RESET_ALL)
	try:
		socket.gethostbyname("www.google.com")
		print(Fore.GREEN + "✅ DNS: OK" + Style.RESET_ALL)
	except socket.gaierror:
		problemas_detectados.append("Problema com servidores DNS")
		solucoes_sugeridas.append("Tente usar DNS público (8.8.8.8 ou 1.1.1.1)")

	# 3. Verificar gateway padrão
	print(Fore.YELLOW + "🔄 Testando gateway de rede..." + Style.RESET_ALL)
	try:
		if os.name == 'nt':  # Windows
			resultado = subprocess.run(["ipconfig"], capture_output=True, text=True, timeout=10)
			if "Gateway Padrão" in resultado.stdout and "." in resultado.stdout:
				print(Fore.GREEN + "✅ Gateway de rede: OK" + Style.RESET_ALL)
			else:
				problemas_detectados.append("Gateway padrão não configurado")
				solucoes_sugeridas.append("Verifique as configurações de IP do adaptador de rede")
		else:  # Linux/Mac
			resultado = subprocess.run(["route", "-n"], capture_output=True, text=True, timeout=10)
			if "0.0.0.0" in resultado.stdout:
				print(Fore.GREEN + "✅ Gateway de rede: OK" + Style.RESET_ALL)
			else:
				problemas_detectados.append("Gateway padrão não configurado")
				solucoes_sugeridas.append("Verifique as configurações de IP do adaptador de rede")
	except Exception as e:
		problemas_detectados.append(f"Erro ao verificar gateway: {str(e)}")

	# 4. Verificar latência
	print(Fore.YELLOW + "⏱️ Testando latência..." + Style.RESET_ALL)
	try:
		inicio = time.time()
		requests.get("https://www.google.com", timeout=5)
		latencia = (time.time() - inicio) * 1000
		if latencia < 100:
			print(Fore.GREEN + f"✅ Latência: {latencia:.2f}ms (Boa)" + Style.RESET_ALL)
		elif latencia < 300:
			print(Fore.YELLOW + f"⚠️ Latência: {latencia:.2f}ms (Moderada)" + Style.RESET_ALL)
		else:
			print(Fore.RED + f"🔴 Latência: {latencia:.2f}ms (Alta)" + Style.RESET_ALL)
			problemas_detectados.append("Latência de rede alta")
			solucoes_sugeridas.append("Feche aplicações que usam muita banda ou reinicie o roteador")
	except:
		pass

	# 5. Verificar portas locais
	print(Fore.YELLOW + "🔌 Testando portas de rede..." + Style.RESET_ALL)
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.settimeout(2)
			resultado = s.connect_ex(('127.0.0.1', 80))
			if resultado == 0:
				print(Fore.GREEN + "✅ Porta local 80: OK" + Style.RESET_ALL)
			else:
				print(Fore.YELLOW + "⚠️ Porta 80 local não disponível" + Style.RESET_ALL)
	except:
		print(Fore.YELLOW + "⚠️ Erro ao testar porta 80" + Style.RESET_ALL)

	# Exibir relatório final
	print("\n" + "="*50)
	print(Fore.CYAN + "📊 RELATÓRIO DE DIAGNÓSTICO DE REDE" + Style.RESET_ALL)
	print("="*50)

	if not problemas_detectados:
		print(Fore.GREEN + "🎉 Nenhum problema grave detectado! Sua rede parece estar funcionando bem." + Style.RESET_ALL)
	else:
		print(Fore.RED + f"🔴 Problemas detectados: {len(problemas_detectados)}" + Style.RESET_ALL)
		for i, problema in enumerate(problemas_detectados, 1):
			print(Fore.RED + f"{i}. {problema}" + Style.RESET_ALL)

		print("\n" + Fore.GREEN + "💡 Soluções sugeridas:" + Style.RESET_ALL)
		for i, solucao in enumerate(solucoes_sugeridas, 1):
			print(Fore.GREEN + f"{i}. {solucao}" + Style.RESET_ALL)

		# Soluções gerais
		print("\n" + Fore.YELLOW + "🛠️ Ações gerais para tentar:" + Style.RESET_ALL)
		print("1. Reinicie o modem/roteador")
		print("2. Reinicie o computador")
		print("3. Verifique os cabos de rede")
		print("4. Desative e reative o adaptador de rede")
		print("5. Entre em contato com seu provedor de internet")


	print(f"\n{Fore.CYAN}Diagnóstico concluído em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
	input("pressione enter para sair")

# Exemplo de uso:
# diagnosticar_rede()

def internet_control():
	"""
	Função amigável para conectar e desconectar da internet
	Interface simples com menu para o usuário
	"""

	def mostrar_menu():
		print(f"\n{Fore.CYAN}=== CONTROLE DE INTERNET ==={Style.RESET_ALL}")
		print(f"{Fore.GREEN}1.{Style.RESET_ALL} Conectar à Internet")
		print(f"{Fore.RED}2.{Style.RESET_ALL} Desconectar da Internet")
		print(f"{Fore.YELLOW}3.{Style.RESET_ALL} Verificar Status da Conexão")
		print(f"{Fore.BLUE}0.{Style.RESET_ALL} Sair")
		print(f"{Fore.CYAN}{'='*28}{Style.RESET_ALL}")

	def conectar_internet():
		print(f"\n{Fore.GREEN}Conectando à Internet...{Style.RESET_ALL}")

		# Comandos para diferentes sistemas operacionais
		if os.name == 'nt':  # Windows
			commands = [
				'netsh interface set interface "Wi-Fi" enabled',
				'netsh interface set interface "Ethernet" enabled',
				'ipconfig /renew'
			]
		else:  # Linux/Mac
			commands = [
				'sudo systemctl start NetworkManager',
				'sudo service networking start',
				'sudo ifconfig eth0 up',
				'sudo ifconfig wlan0 up'
			]

		for cmd in commands:
			try:
				result = os.system(cmd)
				if result == 0:
					print(f"{Fore.GREEN}✓ Comando executado com sucesso{Style.RESET_ALL}")
				time.sleep(1)
			except Exception as e:
				print(f"{Fore.YELLOW}⚠ Aviso: {e}{Style.RESET_ALL}")

		print(f"{Fore.GREEN}✅ Tentativa de conexão concluída!{Style.RESET_ALL}")
		verificar_status()

	def desconectar_internet():
		print(f"\n{Fore.RED}Desconectando da Internet...{Style.RESET_ALL}")

		# Comandos para diferentes sistemas operacionais
		if os.name == 'nt':  # Windows
			commands = [
				'netsh interface set interface "Wi-Fi" disabled',
				'netsh interface set interface "Ethernet" disabled'
			]
		else:  # Linux/Mac
			commands = [
				'sudo systemctl stop NetworkManager',
				'sudo service networking stop',
				'sudo ifconfig eth0 down',
				'sudo ifconfig wlan0 down'
			]

		for cmd in commands:
			try:
				result = os.system(cmd)
				if result == 0:
					print(f"{Fore.GREEN}✓ Comando executado com sucesso{Style.RESET_ALL}")
				time.sleep(1)
			except Exception as e:
				print(f"{Fore.YELLOW}⚠ Aviso: {e}{Style.RESET_ALL}")

		print(f"{Fore.RED}🔌 Tentativa de desconexão concluída!{Style.RESET_ALL}")
		verificar_status()

	def verificar_status():
		print(f"\n{Fore.BLUE}Verificando status da conexão...{Style.RESET_ALL}")

		def testar_conexao(host="8.8.8.8", port=53, timeout=3):
			"""
			Testa a conectividade com a internet
			"""
			try:
				socket.setdefaulttimeout(timeout)
				socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
				return True
			except socket.error:
				return False

		# Teste de conexão
		if testar_conexao():
			print(f"{Fore.GREEN}✅ Internet: CONECTADA{Style.RESET_ALL}")
		else:
			print(f"{Fore.RED}❌ Internet: DESCONECTADA{Style.RESET_ALL}")

		# Informações adicionais
		try:
			hostname = socket.gethostname()
			print(f"{Fore.CYAN}📡 Hostname: {hostname}{Style.RESET_ALL}")
		except:
			pass

		hora_atual = pyOS_hora.hora() if 'pyOS_hora' in globals() else "N/A"
		print(f"{Fore.CYAN}🕐 Hora: {hora_atual}{Style.RESET_ALL}")

	# Loop principal do menu
	while True:
		mostrar_menu()

		try:
			opcao = input(f"\n{Fore.YELLOW}Escolha uma opção (0-3): {Style.RESET_ALL}").strip()

			if opcao == '1':
				conectar_internet()
			elif opcao == '2':
				# Confirmação para desconectar
				confirmar = input(f"{Fore.YELLOW}Tem certeza que deseja desconectar? (s/N): {Style.RESET_ALL}").strip().lower()
				if confirmar in ['s', 'sim', 'y', 'yes']:
					desconectar_internet()
				else:
					print(f"{Fore.BLUE}Operação cancelada.{Style.RESET_ALL}")
			elif opcao == '3':
				verificar_status()
			elif opcao == '0':
				print(f"{Fore.CYAN}Saindo do controle de internet...{Style.RESET_ALL}")
				break
			else:
				print(f"{Fore.RED}❌ Opção inválida! Escolha entre 0 e 3.{Style.RESET_ALL}")

		except KeyboardInterrupt:
			print(f"\n{Fore.YELLOW}Operação interrompida pelo usuário.{Style.RESET_ALL}")
			break
		except Exception as e:
			print(f"{Fore.RED}❌ Erro: {e}{Style.RESET_ALL}")


def abrirapp_c(app, ac="main", argv=[]):
		env = os.environ.copy()
		lpath = f"{os.getcwd()}/apps/{app}/lib"
		if env.get("LD_LIBRARY_PATH", ""):
				env["LD_LIBRARY_PATH"] += ":" + lpath
		else:
				env["LD_LIBRARY_PATH"] = lpath


		subprocess.run([sys.executable, f"{os.getcwd()}/apps/{app}/{ac}.py", *argv], cwd=f"{os.getcwd()}/workspace/{app}", env=env)
def abrirapp(app):
		os.system("clear")

		try:
				criar_barra(app)
				if callable(apps[app]):
						apps[app]()
				else:
						abrirapp_c(app)
		except KeyError:
				print(Fore.RED + "app não encontrado")
				time.sleep(3)
		os.system("clear")



def agenda():
	"""
	App de agenda com eventos, lembretes e datas
	"""
	import os
	import json
	from datetime import datetime, timedelta

	# Diretório de eventos (mesmo padrão do notes/)
	events_dir = "./events"
	os.makedirs(events_dir, exist_ok=True)

	def data_atual():
		"""Retorna a data atual formatada"""
		return datetime.now().strftime("%Y-%m-%d")

	def mostrar_data_atual():
		"""Mostra a data atual de forma bonita"""
		hoje = datetime.now()
		dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
		meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

		print(f"\n📅 {dias_semana[hoje.weekday()]}, {hoje.day} de {meses[hoje.month-1]} de {hoje.year}")
		print("=" * 40)

	def carregar_eventos():
		"""Carrega todos os eventos do arquivo"""
		eventos_file = os.path.join(events_dir, "eventos.json")
		if os.path.exists(eventos_file):
			with open(eventos_file, 'r', encoding='utf-8') as f:
				return json.load(f)
		return {}

	def salvar_eventos(eventos):
		"""Salva eventos no arquivo"""
		eventos_file = os.path.join(events_dir, "eventos.json")
		with open(eventos_file, 'w', encoding='utf-8') as f:
			json.dump(eventos, f, indent=2, ensure_ascii=False)

	def verificar_eventos_hoje():
		"""Verifica e mostra eventos do dia atual"""
		eventos = carregar_eventos()
		hoje = data_atual()

		eventos_hoje = []
		for evento_id, evento in eventos.items():
			if evento['data'] == hoje:
				eventos_hoje.append(evento)

		if eventos_hoje:
			print(f"\n🎯 EVENTOS PARA HOJE ({len(eventos_hoje)}):")
			for evento in eventos_hoje:
				print(f"   ⏰ {evento['hora']} - {evento['titulo']}")
				if evento['descricao']:
					print(f"	 📝 {evento['descricao']}")
		else:
			print("\n✅ Nenhum evento para hoje")

	def verificar_eventos_proximos():
		"""Verifica eventos próximos (próximos 3 dias)"""
		eventos = carregar_eventos()
		hoje = datetime.now()

		eventos_proximos = []
		for evento_id, evento in eventos.items():
			data_evento = datetime.strptime(evento['data'], "%Y-%m-%d")
			dias_restantes = (data_evento - hoje).days

			if 0 < dias_restantes <= 3:  # Próximos 3 dias (exclui hoje)
				eventos_proximos.append((dias_restantes, evento))

		if eventos_proximos:
			print(f"\n🔔 EVENTOS PRÓXIMOS:")
			for dias, evento in sorted(eventos_proximos):
				print(f"   📌 Em {dias} dia(s) - {evento['data']}")
				print(f"	  ⏰ {evento['hora']} - {evento['titulo']}")

	def adicionar_evento():
		"""Adiciona um novo evento"""
		print("\n➕ ADICIONAR EVENTO")

		titulo = input("Título do evento: ").strip()
		if not titulo:
			print("❌ Título é obrigatório!")
			return

		# Data
		while True:
			data = input("Data (YYYY-MM-DD ou Enter para hoje): ").strip()
			if not data:
				data = data_atual()
				break
			try:
				datetime.strptime(data, "%Y-%m-%d")
				break
			except ValueError:
				print("❌ Formato inválido! Use YYYY-MM-DD")

		# Hora
		while True:
			hora = input("Hora (HH:MM ou Enter para 00:00): ").strip()
			if not hora:
				hora = "00:00"
				break
			try:
				datetime.strptime(hora, "%H:%M")
				break
			except ValueError:
				print("❌ Formato inválido! Use HH:MM")

		descricao = input("Descrição (opcional): ").strip()

		# Salvar evento
		eventos = carregar_eventos()
		evento_id = str(len(eventos) + 1)

		eventos[evento_id] = {
			'titulo': titulo,
			'data': data,
			'hora': hora,
			'descricao': descricao,
			'criado_em': data_atual()
		}

		salvar_eventos(eventos)
		print("✅ Evento adicionado com sucesso!")

	def listar_eventos():
		"""Lista todos os eventos"""
		eventos = carregar_eventos()

		if not eventos:
			print("\n📭 Nenhum evento cadastrado")
			return

		# Ordenar por data
		eventos_ordenados = sorted(
			eventos.items(), 
			key=lambda x: (x[1]['data'], x[1]['hora'])
		)

		print(f"\n📋 TODOS OS EVENTOS ({len(eventos)}):")
		for evento_id, evento in eventos_ordenados:
			data_formatada = datetime.strptime(evento['data'], "%Y-%m-%d").strftime("%d/%m/%Y")
			print(f"\n🎯 {evento['titulo']}")
			print(f"   📅 {data_formatada} | ⏰ {evento['hora']}")
			if evento['descricao']:
				print(f"   📝 {evento['descricao']}")
			print(f"   🔑 ID: {evento_id}")

	def remover_evento():
		"""Remove um evento pelo ID"""
		eventos = carregar_eventos()

		if not eventos:
			print("❌ Nenhum evento para remover")
			return

		listar_eventos()
		evento_id = input("\nDigite o ID do evento a remover: ").strip()

		if evento_id in eventos:
			confirmar = input(f"Remover '{eventos[evento_id]['titulo']}'? (s/n): ")
			if confirmar.lower() == 's':
				del eventos[evento_id]
				salvar_eventos(eventos)
				print("✅ Evento removido!")
		else:
			print("❌ ID não encontrado!")

	# MAIN LOOP
	while True:
		mostrar_data_atual()
		verificar_eventos_hoje()
		verificar_eventos_proximos()

		print("\n" + "=" * 40)
		print("1. Adicionar evento")
		print("2. Ver todos os eventos") 
		print("3. Remover evento")
		print("0. Voltar ao menu principal")

		opcao = input("\nEscolha uma opção: ").strip()

		if opcao == "1":
			adicionar_evento()
		elif opcao == "2":
			listar_eventos()
			input("\nPressione Enter para continuar...")
		elif opcao == "3":
			remover_evento()
		elif opcao == "0":
			print("👋 Voltando ao menu principal...")
			break
		else:
			print("❌ Opção inválida!")

		input("\nPressione Enter para continuar...")

def python3():
		global pydir
		if 'pydir' not in globals():
				pydir = sys.executable
		os.makedirs(".python3", exist_ok=True)
		pypo = os.environ.get("PYTHONPATH")
		os.environ["PYTHONPATH"] = os.path.join(os.getcwd(), ".python3")
		if os.path.exists("./pydir.txt"):
				with open("./pydir.txt, ", "r") as f:
						pydir = f.read()
		print("""1. ver versao do python
2. abrir editor
3. instalar biblioteca
4. mudar diretorio do python
5. visualizar diretorio do python
0. sair
""")
		while True:
				esc = input("opcao: ")
				if esc == "1":
						os.system(f"python --version")
				elif esc == "2":
						abrirEditor()
				elif esc == "0":
						os.environ["PYTHONPATH"] = pypo
						break
				elif esc == "3":
						pacote = input("pacote: ")
						res = subprocess.run(["pip", "install", pacote], text=True)
						if res.stderr:
								print("erro")
						else:
								print("pacote instalado com sucesso, reiniciando...")
								os.execv(sys.executable, ['python3'] + sys.argv)
				elif esc == "4":
						pydir = input("novo dir: ")
						with open("pydir.txt", "w") as f:
								f.write(pydir)
				elif esc == "5":
						print(pydir)



import os
import sys
import tempfile
import curses
import colorama

def abrirEditor():
	"""
	Abre um editor de código TUI para Python
	Usa o Python do sistema e os.system para compatibilidade com input()
	"""
	# Inicializa colorama
	colorama.init()

	def main(stdscr):
		# Configurações iniciais do curses
		curses.curs_set(1)  # Mostra cursor
		stdscr.clear()

		# Cores (simples, sem syntax highlighting complexo)
		curses.start_color()
		curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal
		curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Título
		curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Status
		curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK) # Aviso

		# Dados do editor
		texto = [""]  # Lista de linhas
		arquivo_atual = None
		linha_atual = 0
		coluna_atual = 0
		mostrar_ajuda = True

		def desenhar_interface():
			"""Desenha a interface do editor"""
			height, width = stdscr.getmaxyx()

			# Área de título
			stdscr.attron(curses.color_pair(2))
			titulo = "Editor Python - F1: Ajuda | F2: Salvar | F3: Abrir | F4: Executar | F10: Sair"
			stdscr.addstr(0, 0, titulo[:width-1])
			stdscr.attroff(curses.color_pair(2))

			# Informação do arquivo
			status = f"Arquivo: {arquivo_atual or 'Não salvo'} | Python: {sys.executable}"
			stdscr.attron(curses.color_pair(3))
			stdscr.addstr(1, 0, status[:width-1])
			stdscr.attroff(curses.color_pair(3))

			# Área de edição (começa na linha 3)
			edit_y = 3
			edit_height = height - 6
			edit_width = width - 1

			# Desenha as linhas do texto
			stdscr.attron(curses.color_pair(1))
			for i in range(edit_height):
				line_y = edit_y + i
				if line_y >= height:
					break

				if i < len(texto):
					# Mostra número da linha
					num_linha = f"{i+1:3d} "
					try:
						stdscr.addstr(line_y, 0, num_linha)
					except:
						pass

					# Mostra conteúdo da linha
					linha = texto[i]
					if len(linha) > edit_width - 5:
						linha = linha[:edit_width - 8] + "..."

					try:
						stdscr.addstr(line_y, 4, linha)
					except:
						pass

					# Limpa o resto da linha
					for x in range(len(num_linha) + len(linha), edit_width):
						try:
							stdscr.addch(line_y, x, ' ')
						except:
							pass
				else:
					# Linha vazia
					try:
						stdscr.addstr(line_y, 0, f"{i+1:3d} ")
					except:
						pass

			# Posiciona cursor
			try:
				stdscr.move(edit_y + linha_atual, min(4 + coluna_atual, width - 2))
			except:
				pass

			# Barra de ajuda/status
			if mostrar_ajuda:
				ajuda_y = height - 2
				ajuda = "↑↓←→: Navegar | Entrar: Nova linha | Backspace: Apagar | Ctrl+S: Salvar | Ctrl+O: Abrir | Ctrl+R: Executar"
				stdscr.attron(curses.color_pair(4))
				try:
					stdscr.addstr(ajuda_y, 0, ajuda[:width-1])
				except:
					pass
				stdscr.attroff(curses.color_pair(4))

			# Barra de status do cursor
			status_cursor = f"Linha: {linha_atual+1}/{len(texto)} Col: {coluna_atual+1}"
			try:
				stdscr.addstr(height-1, 0, status_cursor[:width-1])
			except:
				pass

			stdscr.refresh()

		def salvar_arquivo():
			"""Salva o texto em um arquivo"""
			nonlocal arquivo_atual

			height, width = stdscr.getmaxyx()

			# Se não tem arquivo atual, pede nome
			if not arquivo_atual:
				stdscr.addstr(height-1, 0, "Nome do arquivo (com .py): ")
				stdscr.refresh()

				curses.echo()
				nome = ""
				try:
					nome = stdscr.getstr(height-1, 23, width-24).decode('utf-8')
				except:
					pass
				curses.noecho()

				if nome:
					arquivo_atual = nome

			# Salva o arquivo
			if arquivo_atual:
				try:
					with open(arquivo_atual, 'w', encoding='utf-8') as f:
						f.write('\n'.join(texto))

					# Mensagem de sucesso
					mensagem = f"Arquivo salvo: {arquivo_atual}"
					stdscr.addstr(height-1, 0, " " * (width-1))
					stdscr.addstr(height-1, 0, mensagem[:width-1])
					stdscr.refresh()
					stdscr.getch()
					return True
				except Exception as e:
					mensagem = f"Erro ao salvar: {str(e)}"
					stdscr.addstr(height-1, 0, " " * (width-1))
					stdscr.addstr(height-1, 0, mensagem[:width-1])
					stdscr.refresh()
					stdscr.getch()

			return False

		def abrir_arquivo():
			"""Abre um arquivo existente"""
			nonlocal texto, arquivo_atual

			height, width = stdscr.getmaxyx()

			stdscr.addstr(height-1, 0, "Nome do arquivo para abrir: ")
			stdscr.refresh()

			curses.echo()
			nome = ""
			try:
				nome = stdscr.getstr(height-1, 27, width-28).decode('utf-8')
			except:
				pass
			curses.noecho()

			if nome and os.path.exists(nome):
				try:
					with open(nome, 'r', encoding='utf-8') as f:
						texto = f.read().splitlines()

					arquivo_atual = nome

					# Mensagem de sucesso
					mensagem = f"Arquivo aberto: {nome}"
					stdscr.addstr(height-1, 0, " " * (width-1))
					stdscr.addstr(height-1, 0, mensagem[:width-1])
					stdscr.refresh()
					stdscr.getch()
					return True
				except Exception as e:
					mensagem = f"Erro ao abrir: {str(e)}"
					stdscr.addstr(height-1, 0, " " * (width-1))
					stdscr.addstr(height-1, 0, mensagem[:width-1])
					stdscr.refresh()
					stdscr.getch()

			return False

		def executar_codigo():
			"""Executa o código Python usando os.system para compatibilidade com input()"""
			nonlocal texto

			# Cria um arquivo temporário
			with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
				f.write('\n'.join(texto))
				temp_file = f.name

			try:
				# Sai do modo curses temporariamente para executar
				curses.endwin()

				print(f"\n{'='*60}")
				print("Executando código Python (pressione Ctrl+C para interromper)...")
				print(f"{'='*60}\n")

				# Executa com os.system - mantém stdin/stdout conectados ao terminal
				comando = f'{pydir} -S "{temp_file}"'
				return_code = os.system(comando)

				print(f"\n{'='*60}")
				print(f"Programa finalizado com código de retorno: {return_code}")
				print(f"{'='*60}")

				input("\nPressione Enter para voltar ao editor...")

			except KeyboardInterrupt:
				print("\n\n[Execução interrompida pelo usuário]")
				input("\nPressione Enter para voltar ao editor...")
			except Exception as e:
				print(f"\nErro durante execução: {e}")
				input("\nPressione Enter para voltar ao editor...")
			finally:
				# Volta para o modo curses
				stdscr.refresh()

				# Remove arquivo temporário
				try:
					os.unlink(temp_file)
				except:
					pass

		# Loop principal do editor
		while True:
			desenhar_interface()

			try:
				key = stdscr.getch()
			except:
				break

			# Processa teclas
			if key == curses.KEY_F10 or key == 27:  # F10 ou ESC
				break
			elif key == curses.KEY_F1:
				mostrar_ajuda = not mostrar_ajuda
			elif key == curses.KEY_F2 or key == 19:  # F2 ou Ctrl+S (ASCII 19)
				salvar_arquivo()
			elif key == curses.KEY_F3 or key == 15:  # F3 ou Ctrl+O (ASCII 15)
				abrir_arquivo()
			elif key == curses.KEY_F4 or key == 18:  # F4 ou Ctrl+R (ASCII 18)
				executar_codigo()

			# Navegação e edição
			elif key == curses.KEY_UP:
				if linha_atual > 0:
					linha_atual -= 1
					coluna_atual = min(coluna_atual, len(texto[linha_atual]))
			elif key == curses.KEY_DOWN:
				if linha_atual < len(texto) - 1:
					linha_atual += 1
					coluna_atual = min(coluna_atual, len(texto[linha_atual]))
			elif key == curses.KEY_LEFT:
				if coluna_atual > 0:
					coluna_atual -= 1
				elif linha_atual > 0:
					linha_atual -= 1
					coluna_atual = len(texto[linha_atual])
			elif key == curses.KEY_RIGHT:
				if coluna_atual < len(texto[linha_atual]):
					coluna_atual += 1
				elif linha_atual < len(texto) - 1:
					linha_atual += 1
					coluna_atual = 0
			elif key == curses.KEY_BACKSPACE or key == 127:
				if coluna_atual > 0:
					# Remove caractere na posição atual
					linha = texto[linha_atual]
					texto[linha_atual] = linha[:coluna_atual-1] + linha[coluna_atual:]
					coluna_atual -= 1
				elif linha_atual > 0:
					# Une com linha anterior
					linha_anterior = texto[linha_atual-1]
					linha_atual -= 1
					coluna_atual = len(linha_anterior)
					texto[linha_atual] += texto.pop(linha_atual+1)
			elif key == curses.KEY_ENTER or key == 10:
				# Quebra linha
				linha_atual += 1
				linha_antiga = texto[linha_atual-1]
				texto.insert(linha_atual, linha_antiga[coluna_atual:])
				texto[linha_atual-1] = linha_antiga[:coluna_atual]
				coluna_atual = 0
			elif 32 <= key <= 126:  # Caracteres imprimíveis
				# Insere caractere
				linha = texto[linha_atual]
				texto[linha_atual] = linha[:coluna_atual] + chr(key) + linha[coluna_atual:]
				coluna_atual += 1

		# Limpa colorama ao sair
		colorama.deinit()
		return '\n'.join(texto)

	# Executa o editor com curses
	try:
		return curses.wrapper(main)
	except KeyboardInterrupt:
		colorama.deinit()
		print("\nEditor fechado.")
		return ""
	except Exception as e:
		colorama.deinit()
		print(f"Erro ao iniciar editor: {e}")
		import traceback
		traceback.print_exc()
		return ""



def audio():
	"""
	App de áudio - Gravar e reproduzir arquivos de áudio
	"""
	import os
	import time
	import wave
	import pyaudio
	import threading

	# Configurações
	AUDIO_DIR = "./audio_files"
	os.makedirs(AUDIO_DIR, exist_ok=True)

	# Verificar se pyaudio está instalado
	try:
		import pyaudio
	except ImportError:
		print("📦 PyAudio não encontrado. Instalando...")
		try:
			import sys
			import subprocess

			# Instalar PyAudio
			subprocess.check_call([sys.executable, "-m", "pip", "install", "pyaudio"])

			# No Linux pode precisar de dependências extras
			if os.name != 'nt':
				try:
					subprocess.check_call(["sudo", "apt-get", "install", "portaudio19-dev", "-y"])
				except:
					try:
						subprocess.check_call(["sudo", "pacman", "-S", "portaudio", "--noconfirm"])
					except:
						pass

			print("✅ PyAudio instalado com sucesso!")
			import pyaudio
		except Exception as e:
			print(f"❌ Erro ao instalar PyAudio: {e}")
			print("Tente instalar manualmente:")
			print("  pip install pyaudio")
			print("Para Linux, talvez precise: sudo apt-get install portaudio19-dev")
			time.sleep(3)
			return

	def listar_audios():
		"""Lista todos os arquivos de áudio disponíveis"""
		arquivos = []
		for arquivo in os.listdir(AUDIO_DIR):
			if arquivo.endswith('.wav'):
				caminho = os.path.join(AUDIO_DIR, arquivo)
				tamanho = os.path.getsize(caminho)
				tamanho_mb = tamanho / (1024 * 1024)
				arquivos.append((arquivo, tamanho_mb))

		return arquivos

	def gravar_audio():
		"""Grava áudio do microfone e salva em arquivo WAV"""
		print("🎤 GRAVAR ÁUDIO")
		print("-" * 40)

		# Configurações de gravação
		FORMAT = pyaudio.paInt16  # 16-bit resolution
		CHANNELS = 1			  # Mono
		RATE = 44100			  # 44.1kHz sample rate
		CHUNK = 1024			  # Tamanho do buffer

		nome_arquivo = input("Nome do arquivo (sem .wav): ").strip()
		if not nome_arquivo:
			print("❌ Nome inválido!")
			return

		nome_arquivo = nome_arquivo + ".wav"
		caminho_arquivo = os.path.join(AUDIO_DIR, nome_arquivo)

		# Verificar se arquivo já existe
		if os.path.exists(caminho_arquivo):
			print(f"⚠️  Arquivo '{nome_arquivo}' já existe!")
			sobrescrever = input("Sobrescrever? (s/n): ").lower()
			if sobrescrever != 's':
				return

		duracao = input("Duração da gravação em segundos (ou Enter para 10s): ").strip()
		if duracao and duracao.isdigit():
			RECORD_SECONDS = int(duracao)
		else:
			RECORD_SECONDS = 10

		print(f"\n🎙️  Preparando para gravar {RECORD_SECONDS} segundos...")
		print("Pressione Enter para começar...")
		input()

		try:
			# Inicializar PyAudio
			audio = pyaudio.PyAudio()

			# Configurar stream de gravação
			stream = audio.open(
				format=FORMAT,
				channels=CHANNELS,
				rate=RATE,
				input=True,
				frames_per_buffer=CHUNK
			)

			print(f"\n🔴 GRAVANDO... (Duração: {RECORD_SECONDS}s)")
			print("Pressione Ctrl+C para parar antecipadamente")
			print("-" * 40)

			frames = []

			# Barra de progresso simples
			for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
				try:
					data = stream.read(CHUNK)
					frames.append(data)

					# Mostrar progresso a cada 10%
					progresso = int((i / (RATE / CHUNK * RECORT_SECONDS)) * 100)
					if progresso % 10 == 0 and i > 0:
						print(f"Progresso: {progresso}%", end='\r')
				except KeyboardInterrupt:
					print("\n⏹️  Gravação interrompida pelo usuário")
					break
				except Exception as e:
					print(f"\n⚠️  Erro durante gravação: {e}")
					break

			print("✅ Gravação concluída!")

			# Parar stream
			stream.stop_stream()
			stream.close()
			audio.terminate()

			# Salvar arquivo WAV
			with wave.open(caminho_arquivo, 'wb') as wf:
				wf.setnchannels(CHANNELS)
				wf.setsampwidth(audio.get_sample_size(FORMAT))
				wf.setframerate(RATE)
				wf.writeframes(b''.join(frames))

			tamanho_mb = os.path.getsize(caminho_arquivo) / (1024 * 1024)
			print(f"💾 Arquivo salvo: {nome_arquivo} ({tamanho_mb:.2f} MB)")

		except Exception as e:
			print(f"❌ Erro durante gravação: {e}")

		input("\nPressione Enter para continuar...")

	def reproduzir_audio():
		"""Reproduz um arquivo de áudio WAV"""
		print("🔊 REPRODUZIR ÁUDIO")
		print("-" * 40)

		arquivos = listar_audios()
		if not arquivos:
			print("❌ Nenhum arquivo de áudio encontrado!")
			print("Grave primeiro algum áudio.")
			time.sleep(2)
			return

		print("\n📋 Arquivos disponíveis:")
		for i, (arquivo, tamanho) in enumerate(arquivos, 1):
			print(f"{i:2d}. {arquivo} ({tamanho:.2f} MB)")

		try:
			escolha = input("\nDigite o número ou nome do arquivo: ").strip()

			if escolha.isdigit():
				index = int(escolha) - 1
				if 0 <= index < len(arquivos):
					nome_arquivo = arquivos[index][0]
				else:
					print("❌ Número inválido!")
					return
			else:
				if not escolha.endswith('.wav'):
					escolha += '.wav'

				# Verificar se arquivo existe
				arquivos_nomes = [a[0] for a in arquivos]
				if escolha not in arquivos_nomes:
					print(f"❌ Arquivo '{escolha}' não encontrado!")
					return
				nome_arquivo = escolha

			caminho_arquivo = os.path.join(AUDIO_DIR, nome_arquivo)

			try:
				# Abrir arquivo WAV
				wf = wave.open(caminho_arquivo, 'rb')

				# Inicializar PyAudio
				audio = pyaudio.PyAudio()

				# Configurar stream de reprodução
				stream = audio.open(
					format=audio.get_format_from_width(wf.getsampwidth()),
					channels=wf.getnchannels(),
					rate=wf.getframerate(),
					output=True
				)

				print(f"\n🎵 Reproduzindo: {nome_arquivo}")
				print("Pressione Ctrl+C para parar")
				print("-" * 40)

				# Ler e reproduzir dados em chunks
				data = wf.readframes(1024)
				while data:
					stream.write(data)
					data = wf.readframes(1024)

				# Finalizar
				stream.stop_stream()
				stream.close()
				audio.terminate()
				wf.close()

				print("✅ Reprodução concluída!")

			except KeyboardInterrupt:
				print("\n⏹️  Reprodução interrompida pelo usuário")
				try:
					stream.stop_stream()
					stream.close()
					audio.terminate()
					wf.close()
				except:
					pass

			except Exception as e:
				print(f"❌ Erro durante reprodução: {e}")

		except Exception as e:
			print(f"❌ Erro: {e}")

		input("\nPressione Enter para continuar...")

	def deletar_audio():
		"""Deleta um arquivo de áudio"""
		print("🗑️  DELETAR ÁUDIO")
		print("-" * 40)

		arquivos = listar_audios()
		if not arquivos:
			print("❌ Nenhum arquivo para deletar!")
			return

		print("\n📋 Arquivos disponíveis:")
		for i, (arquivo, tamanho) in enumerate(arquivos, 1):
			print(f"{i:2d}. {arquivo} ({tamanho:.2f} MB)")

		try:
			escolha = input("\nDigite o número ou nome do arquivo: ").strip()

			if escolha.isdigit():
				index = int(escolha) - 1
				if 0 <= index < len(arquivos):
					nome_arquivo = arquivos[index][0]
				else:
					print("❌ Número inválido!")
					return
			else:
				if not escolha.endswith('.wav'):
					escolha += '.wav'

				# Verificar se arquivo existe
				arquivos_nomes = [a[0] for a in arquivos]
				if escolha not in arquivos_nomes:
					print(f"❌ Arquivo '{escolha}' não encontrado!")
					return
				nome_arquivo = escolha

			caminho_arquivo = os.path.join(AUDIO_DIR, nome_arquivo)

			confirmar = input(f"\n⚠️  Tem certeza que deseja deletar '{nome_arquivo}'? (s/n): ").lower()
			if confirmar == 's':
				os.remove(caminho_arquivo)
				print(f"✅ Arquivo '{nome_arquivo}' deletado com sucesso!")
			else:
				print("❌ Operação cancelada!")

		except Exception as e:
			print(f"❌ Erro: {e}")

		input("\nPressione Enter para continuar...")

	def info_audio():
		"""Mostra informações técnicas sobre os arquivos de áudio"""
		print("📊 INFORMAÇÕES TÉCNICAS")
		print("-" * 40)

		arquivos = listar_audios()
		if not arquivos:
			print("❌ Nenhum arquivo de áudio encontrado!")
			return

		print(f"\nTotal de arquivos: {len(arquivos)}")
		print("-" * 40)

		for arquivo, tamanho_mb in arquivos:
			caminho = os.path.join(AUDIO_DIR, arquivo)
			try:
				with wave.open(caminho, 'rb') as wf:
					print(f"\n📁 {arquivo}")
					print(f"  Tamanho: {tamanho_mb:.2f} MB")
					print(f"  Canais: {wf.getnchannels()} {'(Mono)' if wf.getnchannels() == 1 else '(Estéreo)'}")
					print(f"  Sample Width: {wf.getsampwidth()} bytes")
					print(f"  Frame Rate: {wf.getframerate()} Hz")
					print(f"  Frames: {wf.getnframes()}")
					duracao = wf.getnframes() / wf.getframerate()
					print(f"  Duração: {duracao:.2f} segundos")
			except Exception as e:
				print(f"  ❌ Erro ao ler arquivo: {e}")

		input("\nPressione Enter para continuar...")

	# Menu principal
	while True:
		print("\n" + "="*50)
		print("🎵 APP DE ÁUDIO - pyOS")
		print("="*50)

		arquivos = listar_audios()
		if arquivos:
			print(f"\n📁 Arquivos disponíveis: {len(arquivos)}")
			for arquivo, tamanho in arquivos[:3]:  # Mostra apenas os 3 primeiros
				print(f"  • {arquivo} ({tamanho:.2f} MB)")
			if len(arquivos) > 3:
				print(f"  ... e mais {len(arquivos)-3} arquivos")
		else:
			print("\n📭 Nenhum arquivo de áudio ainda")

		print("\n📋 MENU:")
		print("1. 🎤 Gravar áudio")
		print("2. 🔊 Reproduzir áudio")
		print("3. 📊 Informações técnicas")
		print("4. 🗑️  Deletar arquivo")
		print("0. ↩️  Voltar ao menu principal")

		opcao = input("\nEscolha uma opção: ").strip()

		if opcao == "1":
			gravar_audio()
		elif opcao == "2":
			reproduzir_audio()
		elif opcao == "3":
			info_audio()
		elif opcao == "4":
			deletar_audio()
		elif opcao == "0":
			print("👋 Voltando ao menu principal...")
			break
		else:
			print("❌ Opção inválida!")
			time.sleep(1)



def uninstall():
	"""
	App para desinstalar o pyOS e seus componentes
	"""
	import shutil
	import json
	import sys
	from datetime import datetime

	# Cores para o terminal
	RED = '\033[91m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	BLUE = '\033[94m'
	MAGENTA = '\033[95m'
	CYAN = '\033[96m'
	BOLD = '\033[1m'
	RESET = '\033[0m'

	def mostrar_titulo():
		"""Mostra o título do desinstalador"""
		print(f"\n{BOLD}{RED}╔══════════════════════════════════════════════════════════╗{RESET}")
		print(f"{BOLD}{RED}║{RESET}{BOLD}				 DESINSTALADOR pyOS					{RESET}{RED}║{RESET}")
		print(f"{BOLD}{RED}║{RESET}{BOLD}			  Versão {version}						 {RESET}{RED}║{RESET}")
		print(f"{BOLD}{RED}╚══════════════════════════════════════════════════════════╝{RESET}\n")

	def criar_backup_config():
		"""Cria um backup das configurações do usuário"""
		backup_dir = "./pyOS_backup"
		os.makedirs(backup_dir, exist_ok=True)

		arquivos_backup = []

		# Configurações a serem salvas
		config_files = [
			("senha.txt", "Senha do sistema"),
			("passwordexist.txt", "Configuração de senha"),
			("./notes/", "Notas do usuário"),
			("./events/", "Eventos da agenda"),
			("./audio_files/", "Arquivos de áudio"),
			("./imgs/", "Imagens do usuário"),
			("msgs.json", "Mensagens"),
			("name_user.txt", "Usuários do chat"),
			("./apps/", "Apps instalados (exceto libs)"),
		]

		print(f"\n{BLUE}📦 Criando backup de configurações...{RESET}")

		for origem, descricao in config_files:
			if isinstance(origem, str):
				if os.path.exists(origem):
					try:
						if os.path.isdir(origem):
							# Copiar diretório
							destino = os.path.join(backup_dir, os.path.basename(origem.rstrip('/')))
							if os.path.exists(destino):
								shutil.rmtree(destino)
							shutil.copytree(origem, destino)
							print(f"  {GREEN}✓{RESET} {descricao}")
							arquivos_backup.append(origem)
						else:
							# Copiar arquivo
							destino = os.path.join(backup_dir, os.path.basename(origem))
							shutil.copy2(origem, destino)
							print(f"  {GREEN}✓{RESET} {descricao}")
							arquivos_backup.append(origem)
					except Exception as e:
						print(f"  {RED}✗{RESET} {descricao}: {e}")

		# Salvar lista de backup
		with open(os.path.join(backup_dir, "backup_info.json"), "w") as f:
			json.dump({
				"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
				"version": version,
				"arquivos": arquivos_backup
			}, f, indent=2)

		print(f"\n{GREEN}✅ Backup criado em: {backup_dir}{RESET}")
		return backup_dir

	def listar_dependencias():
		"""Lista dependências Python instaladas"""
		try:
			print(f"\n{CYAN}📋 Listando dependências instaladas...{RESET}")

			# Verificar requirements.txt se existir
			requirements_file = "./requirements.txt"
			if os.path.exists(requirements_file):
				with open(requirements_file, "r") as f:
					dependencias = [line.strip() for line in f if line.strip()]
				print(f"\nDependências do requirements.txt:")
				for dep in dependencias:
					print(f"  • {dep}")

			# Verificar módulos em apps/libs
			libs_dir = "./apps/libs"
			if os.path.exists(libs_dir):
				print(f"\nMódulos em apps/libs:")
				for item in os.listdir(libs_dir):
					if item.endswith(".py") or os.path.isdir(os.path.join(libs_dir, item)):
						print(f"  • {item}")

			# Verificar módulos do sistema
			system_modules = ["colorama", "requests", "pyfiglet", "psutil", "pyaudio", "PIL", "speech_recognition"]
			print(f"\nMódulos do sistema conhecidos:")
			for mod in system_modules:
				try:
					__import__(mod)
					print(f"  • {mod} {GREEN}(instalado){RESET}")
				except ImportError:
					print(f"  • {mod} {RED}(não instalado){RESET}")

		except Exception as e:
			print(f"{RED}❌ Erro ao listar dependências: {e}{RESET}")

	def desinstalar_completo():
		"""Desinstalação completa"""
		print(f"\n{RED}⚠️  ⚠️  ⚠️  ATENÇÃO: DESINSTALAÇÃO COMPLETA ⚠️  ⚠️  ⚠️{RESET}")
		print(f"{YELLOW}Esta operação irá:{RESET}")
		print(f"  1. {RED}Remover toda a estrutura do pyOS{RESET}")
		print(f"  2. {RED}Desinstalar dependências Python{RESET}")
		print(f"  3. {RED}Remover arquivos de configuração{RESET}")
		print(f"  4. {RED}Excluir todos os dados do usuário{RESET}")

		confirmar1 = input(f"\n{BOLD}Tem certeza ABSOLUTA? (digite 'CONFIRMAR'): {RESET}").strip()
		if confirmar1 != "CONFIRMAR":
			print(f"{GREEN}❌ Operação cancelada.{RESET}")
			return

		confirmar2 = input(f"\n{YELLOW}Esta ação é IRREVERSÍVEL! Digite 'SIM' para continuar: {RESET}").strip()
		if confirmar2 != "SIM":
			print(f"{GREEN}❌ Operação cancelada.{RESET}")
			return

		# Criar backup primeiro
		backup_dir = criar_backup_config()

		print(f"\n{RED}🗑️  Iniciando desinstalação completa...{RESET}")

		# 1. Remover estrutura pyOS
		print(f"\n{BOLD}1. Removendo estrutura do pyOS...{RESET}")
		dirs_to_remove = [
			"./pyOS",
			"./apps",
			"./notes",
			"./events",
			"./audio_files",
			"./imgs",
		]

		for dir_path in dirs_to_remove:
			if os.path.exists(dir_path):
				try:
					if os.path.isdir(dir_path):
						shutil.rmtree(dir_path)
						print(f"  {GREEN}✓{RESET} Removido: {dir_path}")
					else:
						os.remove(dir_path)
						print(f"  {GREEN}✓{RESET} Removido: {dir_path}")
				except Exception as e:
					print(f"  {RED}✗{RESET} Erro ao remover {dir_path}: {e}")

		# 2. Remover arquivos de configuração
		print(f"\n{BOLD}2. Removendo arquivos de configuração...{RESET}")
		files_to_remove = [
			"pyOS.py",
			"syscreated.txt",
			"senha.txt",
			"passwordexist.txt",
			"msgs.json",
			"name_user.txt",
			"requirements.txt",
			"pyOS_backup.zip",
		]

		for file_path in files_to_remove:
			if os.path.exists(file_path):
				try:
					os.remove(file_path)
					print(f"  {GREEN}✓{RESET} Removido: {file_path}")
				except Exception as e:
					print(f"  {RED}✗{RESET} Erro ao remover {file_path}: {e}")

		# 3. Desinstalar dependências
		print(f"\n{BOLD}3. Desinstalando dependências...{RESET}")
		dependencias = [
			"colorama",
			"requests",
			"pyfiglet",
			"bs4",
			"psutil",
			"pyaudio",
			"Pillow",
			"speechrecognition",
		]

		for dep in dependencias:
			try:
				os.system(f"{sys.executable} -m pip uninstall {dep} -y")
				print(f"  {GREEN}✓{RESET} Desinstalado: {dep}")
			except Exception as e:
				print(f"  {YELLOW}⚠{RESET} Não foi possível desinstalar {dep}: {e}")

		# 4. Limpar cache pip
		print(f"\n{BOLD}4. Limpando cache pip...{RESET}")
		try:
			os.system(f"{sys.executable} -m pip cache purge")
			print(f"  {GREEN}✓{RESET} Cache limpo")
		except:
			print(f"  {YELLOW}⚠{RESET} Não foi possível limpar cache")

		print(f"\n{GREEN}✅ Desinstalação completa concluída!{RESET}")
		print(f"\n{YELLOW}📦 Backup salvo em: {backup_dir}{RESET}")
		print(f"\n{BOLD}O pyOS foi completamente removido do sistema.{RESET}")
		print(f"{BOLD}Para reinstalar, execute novamente o pyOS.py{RESET}")

		input(f"\nPressione Enter para sair...")
		sys.exit(0)

	def desinstalar_parcial():
		"""Desinstalação parcial - mantém configurações"""
		print(f"\n{YELLOW}⚠️  DESINSTALAÇÃO PARCIAL{RESET}")
		print(f"{YELLOW}Esta operação irá:{RESET}")
		print(f"  1. {YELLOW}Remover estrutura do pyOS{RESET}")
		print(f"  2. {GREEN}Manter configurações do usuário{RESET}")
		print(f"  3. {GREEN}Manter dependências instaladas{RESET}")
		print(f"  4. {YELLOW}Remover arquivo principal pyOS.py{RESET}")

		confirmar = input(f"\n{BOLD}Continuar? (s/n): {RESET}").strip().lower()
		if confirmar != 's':
			print(f"{GREEN}❌ Operação cancelada.{RESET}")
			return

		print(f"\n{YELLOW}🗑️  Iniciando desinstalação parcial...{RESET}")

		# 1. Remover estrutura pyOS
		print(f"\n{BOLD}1. Removendo estrutura do pyOS...{RESET}")
		dirs_to_remove = [
			"./pyOS",
		]

		for dir_path in dirs_to_remove:
			if os.path.exists(dir_path):
				try:
					shutil.rmtree(dir_path)
					print(f"  {GREEN}✓{RESET} Removido: {dir_path}")
				except Exception as e:
					print(f"  {RED}✗{RESET} Erro ao remover {dir_path}: {e}")

		# 2. Remover arquivo principal
		print(f"\n{BOLD}2. Removendo arquivo principal...{RESET}")
		files_to_remove = [
			"pyOS.py",
			"syscreated.txt",
		]

		for file_path in files_to_remove:
			if os.path.exists(file_path):
				try:
					os.remove(file_path)
					print(f"  {GREEN}✓{RESET} Removido: {file_path}")
				except Exception as e:
					print(f"  {RED}✗{RESET} Erro ao remover {file_path}: {e}")

		print(f"\n{GREEN}✅ Desinstalação parcial concluída!{RESET}")
		print(f"\n{BOLD}O pyOS foi removido, mas:{RESET}")
		print(f"  • Configurações do usuário foram mantidas")
		print(f"  • Dependências continuam instaladas")
		print(f"  • Arquivos de apps em ./apps/ foram mantidos")

		input(f"\nPressione Enter para continuar...")

	def desinstalar_simples():
		"""Desinstalação simples - apenas o arquivo pyOS.py"""
		print(f"\n{BLUE}🗑️  DESINSTALAÇÃO SIMPLES{RESET}")
		print(f"{BLUE}Esta operação irá:{RESET}")
		print(f"  1. {BLUE}Remover apenas o arquivo pyOS.py{RESET}")
		print(f"  2. {GREEN}Manter tudo o mais{RESET}")

		confirmar = input(f"\n{BOLD}Remover pyOS.py? (s/n): {RESET}").strip().lower()
		if confirmar != 's':
			print(f"{GREEN}❌ Operação cancelada.{RESET}")
			return

		if os.path.exists("pyOS.py"):
			try:
				os.remove("pyOS.py")
				print(f"\n{GREEN}✅ pyOS.py removido com sucesso!{RESET}")
				print(f"\n{BOLD}Para reinstalar, basta copiar o pyOS.py novamente{RESET}")
			except Exception as e:
				print(f"{RED}❌ Erro ao remover pyOS.py: {e}{RESET}")
		else:
			print(f"{YELLOW}⚠️  Arquivo pyOS.py não encontrado{RESET}")

		input(f"\nPressione Enter para continuar...")

	def desinstalar_customizada():
		"""Desinstalação customizada"""
		print(f"\n{MAGENTA}⚙️  DESINSTALAÇÃO PERSONALIZADA{RESET}")
		print(f"{MAGENTA}Selecione o que deseja remover:{RESET}")

		opcoes = {
			'1': {'nome': 'Estrutura pyOS/', 'ativo': True},
			'2': {'nome': 'Diretório apps/', 'ativo': True},
			'3': {'nome': 'Configurações de senha', 'ativo': True},
			'4': {'nome': 'Notas do usuário', 'ativo': True},
			'5': {'nome': 'Eventos da agenda', 'ativo': True},
			'6': {'nome': 'Arquivos de áudio', 'ativo': True},
			'7': {'nome': 'Imagens do usuário', 'ativo': True},
			'8': {'nome': 'Mensagens e chats', 'ativo': True},
			'9': {'nome': 'Dependências Python', 'ativo': False},
			'10': {'nome': 'Arquivo pyOS.py', 'ativo': True},
		}

		while True:
			print(f"\n{BOLD}Opções de remoção:{RESET}")
			for key, value in opcoes.items():
				status = f"{GREEN}[✓]{RESET}" if value['ativo'] else f"{RED}[✗]{RESET}"
				print(f"  {key}. {status} {value['nome']}")

			print(f"\n{CYAN}Comandos:{RESET}")
			print(f"  [número] - Alternar opção")
			print(f"  listar - Ver detalhes do que será removido")
			print(f"  executar - Iniciar desinstalação")
			print(f"  sair - Cancelar")

			comando = input(f"\n{BOLD}Opção: {RESET}").strip().lower()

			if comando == 'sair':
				print(f"{GREEN}❌ Operação cancelada.{RESET}")
				return
			elif comando == 'listar':
				listar_itens_selecionados(opcoes)
			elif comando == 'executar':
				executar_desinstalacao_customizada(opcoes)
				break
			elif comando in opcoes:
				opcoes[comando]['ativo'] = not opcoes[comando]['ativo']
				print(f"{YELLOW}Opção {opcoes[comando]['nome']} alternada{RESET}")
			else:
				print(f"{RED}❌ Comando inválido{RESET}")

	def listar_itens_selecionados(opcoes):
		"""Lista itens que serão removidos na desinstalação customizada"""
		print(f"\n{MAGENTA}📋 ITENS SELECIONADOS PARA REMOÇÃO:{RESET}")

		itens_ativos = [op for op in opcoes.values() if op['ativo']]

		if not itens_ativos:
			print(f"  {YELLOW}Nenhum item selecionado{RESET}")
			return

		for i, item in enumerate(itens_ativos, 1):
			print(f"  {i}. {item['nome']}")

		print(f"\n{BOLD}Total: {len(itens_ativos)} itens serão removidos{RESET}")

		# Estimar tamanho
		tamanho_total = 0
		dirs_to_check = [
			("./pyOS", "Estrutura pyOS/"),
			("./apps", "Diretório apps/"),
			("./notes", "Notas do usuário"),
			("./events", "Eventos da agenda"),
			("./audio_files", "Arquivos de áudio"),
			("./imgs", "Imagens do usuário"),
		]

		for dir_path, nome in dirs_to_check:
			if os.path.exists(dir_path) and any(op['nome'] == nome for op in itens_ativos):
				try:
					for root, dirs, files in os.walk(dir_path):
						for file in files:
							file_path = os.path.join(root, file)
							if os.path.exists(file_path):
								tamanho_total += os.path.getsize(file_path)
				except:
					pass

		if tamanho_total > 0:
			tamanho_mb = tamanho_total / (1024 * 1024)
			print(f"{BOLD}Espaço liberado: {tamanho_mb:.2f} MB{RESET}")

	def executar_desinstalacao_customizada(opcoes):
		"""Executa a desinstalação customizada baseada nas opções selecionadas"""
		print(f"\n{MAGENTA}⚙️  Executando desinstalação personalizada...{RESET}")

		# Pedir confirmação final
		confirmar = input(f"{BOLD}Tem certeza? (s/n): {RESET}").strip().lower()
		if confirmar != 's':
			print(f"{GREEN}❌ Operação cancelada.{RESET}")
			return

		# Mapear opções para ações
		acoes = {
			'Estrutura pyOS/': lambda: remover_diretorio("./pyOS"),
			'Diretório apps/': lambda: remover_diretorio("./apps"),
			'Configurações de senha': lambda: remover_arquivos(["senha.txt", "passwordexist.txt"]),
			'Notas do usuário': lambda: remover_diretorio("./notes"),
			'Eventos da agenda': lambda: remover_diretorio("./events"),
			'Arquivos de áudio': lambda: remover_diretorio("./audio_files"),
			'Imagens do usuário': lambda: remover_diretorio("./imgs"),
			'Mensagens e chats': lambda: remover_arquivos(["msgs.json", "name_user.txt"]),
			'Dependências Python': lambda: desinstalar_dependencias(),
			'Arquivo pyOS.py': lambda: remover_arquivos(["pyOS.py", "syscreated.txt"]),
		}

		# Executar ações
		for op in opcoes.values():
			if op['ativo']:
				print(f"\n{BOLD}Removendo: {op['nome']}{RESET}")
				try:
					acoes[op['nome']]()
					print(f"  {GREEN}✓ Concluído{RESET}")
				except Exception as e:
					print(f"  {RED}✗ Erro: {e}{RESET}")

		print(f"\n{GREEN}✅ Desinstalação personalizada concluída!{RESET}")
		input(f"\nPressione Enter para continuar...")

	def remover_diretorio(caminho):
		"""Remove um diretório e seu conteúdo"""
		if os.path.exists(caminho):
			shutil.rmtree(caminho)

	def remover_arquivos(lista_arquivos):
		"""Remove uma lista de arquivos"""
		for arquivo in lista_arquivos:
			if os.path.exists(arquivo):
				os.remove(arquivo)

	def desinstalar_dependencias():
		"""Desinstala dependências Python"""
		dependencias = [
			"colorama", "requests", "pyfiglet", "bs4",
			"psutil", "pyaudio", "Pillow", "speechrecognition"
		]

		for dep in dependencias:
			try:
				os.system(f"{sys.executable} -m pip uninstall {dep} -y")
			except:
				pass

	# Menu principal do desinstalador
	while True:
		mostrar_titulo()

		print(f"{BOLD}Opções de desinstalação:{RESET}")
		print(f"  {RED}1.{RESET} {BOLD}Desinstalação completa{RESET} - Remove TUDO")
		print(f"  {YELLOW}2.{RESET} {BOLD}Desinstalação parcial{RESET} - Remove pyOS, mantém configurações")
		print(f"  {BLUE}3.{RESET} {BOLD}Desinstalação simples{RESET} - Remove apenas pyOS.py")
		print(f"  {MAGENTA}4.{RESET} {BOLD}Desinstalação customizada{RESET} - Escolha o que remover")
		print(f"  {GREEN}5.{RESET} {BOLD}Listar dependências{RESET} - Ver o que está instalado")
		print(f"  {CYAN}6.{RESET} {BOLD}Criar backup{RESET} - Backup das configurações")
		print(f"  {BOLD}0.{RESET} {BOLD}Sair{RESET} - Voltar ao menu principal")

		try:
			opcao = input(f"\n{BOLD}Escolha uma opção (0-6): {RESET}").strip()

			if opcao == "0":
				print(f"{GREEN}👋 Voltando ao menu principal...{RESET}")
				break
			elif opcao == "1":
				desinstalar_completo()
			elif opcao == "2":
				desinstalar_parcial()
			elif opcao == "3":
				desinstalar_simples()
			elif opcao == "4":
				desinstalar_customizada()
			elif opcao == "5":
				listar_dependencias()
				input(f"\nPressione Enter para continuar...")
			elif opcao == "6":
				backup_dir = criar_backup_config()
				input(f"\nPressione Enter para continuar...")
			else:
				print(f"{RED}❌ Opção inválida!{RESET}")
				time.sleep(1)

		except KeyboardInterrupt:
			print(f"\n\n{YELLOW}⚠️  Operação interrompida pelo usuário{RESET}")
			break
		except Exception as e:
			print(f"{RED}❌ Erro: {e}{RESET}")
			time.sleep(2)

import curses
import curses.ascii
from PIL import Image
import datetime
import os

def run_drawing_app(stdscr):
	# Configurações iniciais - com tratamento de erro para curs_set
	try:
		curses.curs_set(0)  # Tenta esconder o cursor
	except:
		pass  # Ignora se não for possível

	stdscr.nodelay(0)
	stdscr.timeout(100)

	# Inicializa cores
	curses.start_color()
	curses.use_default_colors()

	# Inicializa pares de cores se suportado
	if curses.has_colors():
		curses.init_pair(1, curses.COLOR_RED, -1)
		curses.init_pair(2, curses.COLOR_GREEN, -1)
		curses.init_pair(3, curses.COLOR_YELLOW, -1)
		curses.init_pair(4, curses.COLOR_BLUE, -1)
		curses.init_pair(5, curses.COLOR_MAGENTA, -1)
		curses.init_pair(6, curses.COLOR_CYAN, -1)

	# Área de desenho
	height, width = stdscr.getmaxyx()
	height -= 2  # Espaço para status

	# Canvas usando dicionário para posições desenhadas
	canvas = {}
	current_color = 1
	pen_down = True
	eraser_mode = False  # Novo modo borracha

	# Posição inicial do cursor
	cursor_y = min(height // 2, height - 1)
	cursor_x = min(width // 2, width - 1)

	# Cores disponíveis
	colors = [1, 2, 3, 4, 5, 6]
	color_index = 0

	# Nomes das cores
	color_names = {1: 'VERMELHO', 2: 'VERDE', 3: 'AMARELO', 
				  4: 'AZUL', 5: 'MAGENTA', 6: 'CIANO'}

	while True:
		# Limpa a tela
		stdscr.clear()

		# Desenha todos os pontos salvos
		for (y, x), color in list(canvas.items()):
			if 0 <= y < height and 0 <= x < width:
				try:
					if curses.has_colors():
						stdscr.addch(y, x, '█', curses.color_pair(color) | curses.A_BOLD)
					else:
						stdscr.addch(y, x, '#')
				except:
					pass

		# Desenha o cursor
		try:
			if 0 <= cursor_y < height and 0 <= cursor_x < width:
				if eraser_mode:
					cursor_char = '⌂'  # Cursor de borracha
				elif pen_down:
					cursor_char = '▓'
				else:
					cursor_char = '▒'

				if curses.has_colors() and not eraser_mode:
					stdscr.addch(cursor_y, cursor_x, cursor_char, 
							   curses.color_pair(current_color) | curses.A_BLINK)
				else:
					stdscr.addch(cursor_y, cursor_x, cursor_char)
		except:
			pass

		# Ação do cursor (desenhar ou apagar)
		if pen_down:
			if eraser_mode:
				# Modo borracha: remove o pixel
				if (cursor_y, cursor_x) in canvas:
					del canvas[(cursor_y, cursor_x)]
			else:
				# Modo desenho: adiciona pixel
				canvas[(cursor_y, cursor_x)] = current_color

		# Barra de status
		status_y = height
		status = f" COR: {color_names[current_color]} | "
		status += f"CANETA: {'▼' if pen_down else '▲'} | "
		status += f"BORRACHA: {'ON' if eraser_mode else 'OFF'} | "
		status += f"POS: ({cursor_x},{cursor_y}) | "
		status += "TAB:cor | ⬆⬇⬅↪:move | U/D:sobe/desce caneta | E:borracha | B:preenche | C:limpa | S:salva | Q:sair"

		try:
			stdscr.addstr(status_y, 0, status[:width-1], curses.A_REVERSE)
		except:
			pass

		stdscr.refresh()

		# Processa comandos
		key = stdscr.getch()

		# Controles de movimento: ⬆ ⬇ ⬅ ↪
		if key == ord('q') or key == ord('Q'):
			break

		# Seta para cima
		elif key == curses.KEY_UP:
			cursor_y = max(0, cursor_y - 1)
		# Seta para baixo
		elif key == curses.KEY_DOWN:
			cursor_y = min(height - 1, cursor_y + 1)
		# Seta para esquerda
		elif key == curses.KEY_LEFT:
			cursor_x = max(0, cursor_x - 1)
		# Seta para direita
		elif key == curses.KEY_RIGHT:
			cursor_x = min(width - 1, cursor_x + 1)

		# Controles da caneta
		elif key == ord('u') or key == ord('U'):
			pen_down = False
		elif key == ord('d') or key == ord('D'):
			pen_down = True

		# Controle da borracha (E)
		elif key == ord('e') or key == ord('E'):
			eraser_mode = not eraser_mode  # Alterna borracha on/off
			if eraser_mode:
				pen_down = True  # Automaticamente desce a caneta no modo borracha

		# TAB para mudar cor (desativado no modo borracha)
		elif key == ord('\t'):
			if not eraser_mode:  # Só muda cor se não estiver no modo borracha
				color_index = (color_index + 1) % len(colors)
				current_color = colors[color_index]

		# Limpar tela
		elif key == ord('c') or key == ord('C'):
			canvas.clear()

		# Preencher tela
		elif key == ord('b') or key == ord('B'):
			if not eraser_mode:  # Não permite preencher no modo borracha
				for y in range(height):
					for x in range(width):
						canvas[(y, x)] = current_color

		# Salvar (Shift + S)
		elif key == ord('S'):
			save_canvas(canvas, height, width, stdscr)

def save_canvas(canvas, height, width, stdscr):
	"""Salva o canvas como arquivo PNG"""
	try:
		# Mostra mensagem de salvamento
		try:
			stdscr.addstr(height, 0, "Salvando PNG...".ljust(width-1), curses.A_REVERSE)
			stdscr.refresh()
		except:
			pass

		# Cria diretório se não existir
		os.makedirs("desenhos", exist_ok=True)

		# Cria imagem RGB branca
		img = Image.new('RGB', (width, height), 'white')
		pixels = img.load()

		# Mapeia cores curses para RGB
		color_map = {
			1: (255, 0, 0),	  # Vermelho
			2: (0, 255, 0),	  # Verde
			3: (255, 255, 0),	# Amarelo
			4: (0, 0, 255),	  # Azul
			5: (255, 0, 255),	# Magenta
			6: (0, 255, 255),	# Ciano
		}

		# Desenha os pontos na imagem
		for (y, x), color in canvas.items():
			if 0 <= y < height and 0 <= x < width:
				pixels[x, y] = color_map.get(color, (0, 0, 0))

		# Salva arquivo
		timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
		filename = f"desenhos/desenho_{timestamp}.png"
		img.save(filename)

		# Mostra confirmação
		try:
			stdscr.addstr(height, 0, f"Salvo: {filename}".ljust(width-1), curses.A_REVERSE)
			stdscr.refresh()
			curses.napms(2000)
		except:
			pass

	except Exception as e:
		try:
			stdscr.addstr(height, 0, f"Erro ao salvar: {str(e)[:30]}".ljust(width-1), curses.A_REVERSE)
			stdscr.refresh()
			curses.napms(2000)
		except:
			pass

def paint():
	try:
		curses.wrapper(run_drawing_app)
	except KeyboardInterrupt:
		pass
	except Exception as e:
		print(f"Erro: {e}")

def rodar2(script, id):
		global rodando2
		time.sleep(0.7)
		null = subprocess.DEVNULL
		proc = subprocess.Popen([sys.executable, script], stdout=null, stdin=null, stderr=null)
		rodando2[id] = proc.pid
		#print(f"{id} como {proc.pid}")
		time.sleep(0.7)
		return proc

def init2():
	# Verificar se a pasta existe antes de tentar listar
	if not os.path.exists("./apps"):
		os.makedirs("./apps", exist_ok=True)
		return

	if not os.path.exists("app_boot_perms.json"):
		with open("app_boot_perms.json", "w") as f:
			f.write("{}")
		return

	with open("app_boot_perms.json", "r") as f:
		bp = json.load(f)

	for app in os.listdir("./apps"):
		path = f"./apps/{app}"
		if os.path.isdir(path):
				if os.path.exists(f"{path}/exec2.py"):
					if bp.get(app, False):
						rodar2(f"{path}/exec2.py", app)

if "--security-mode" not in sys.argv:
	init2()

apps = {
	"calculadora": calculadora,
	"notepad": notepad,
	"config": config,
	"terminal": terminal,
	"gerenciador de arquivos": fileManager,
	"navegador": navegador,
	"gerenciador de tarefas": taskmgr,
	"mensagens": messages,
	"fotos": images,
	"diagnostico de rede": diagnosticar_rede,
	"agenda": agenda,
	"controle de internet": internet_control,
	"python": python3,
	"audio": audio,
	"paint": paint,
	"antivirus": antivirus
}

def uplistinst():
		global apps
		for k, v in apps.copy().items():
				if v == "app":
						del apps[k]
		for app in os.listdir("./apps"):
				apps[app] = "app"



executando = True
def parar():
		global executando
		executando = False

def view_all():
	print("todos os aplicativos:")
	for i, a in enumerate(sorted(apps.keys())):
		print(f"{i}. {a}")
	op = input("app: ")
	if op in apps:
		abrirapp(op)
	if op.isdigit():
		if int(op) in atalhos:
			abrirapp(atalhos[int(op)])
	else:
		print(Fore.RED, "esse app não existe")
		time.sleep(0.5)
		
while executando:
		uplistinst()						
		print(colorconfig + "colorteste01")
		os.system("clear")
		try:
				importlib.reload(pyOS_system)
		except Exception:
				pass

		criar_barra("python-executive")

		print(Fore.CYAN + "=python==hora==fechar==hostsys=\n")
		print(colorconfig + "apps:")
		atalhos = {}
		for i, app in enumerate(sorted(apps.keys())):
				atalhos[i] = app
		nomes = list(sorted(apps.keys()))[:10]
		for i in range(0, len(nomes), 4):
				# Imprime até 4 apps por linha
				for j in range(4):
						if i + j < len(nomes):
								print(f"{i + j}. {nomes[i + j]}", end='  ')
				print()  # Adiciona uma quebra de linha após cada grupo de 4
		print("a. mostrar todos os apps")
		app = input("app: ")
		os.system("clear")
		if app == "func":
				os.system("clear")
				print(colorconfig + "colorteste")
				os.system("clear")
				criar_barra("python-executive")
				print(Fore.CYAN + "=python==hora==fechar==hostsys=")
				funcesc = input("func: ")
				if funcesc == "python":
						os.system("clear")
						print(Fore.CYAN + "=python==hora==fechar==hostsys=\n	 versão\n=	 pip_versão")
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
						quit()
				elif funcesc == "hostsys":
						os.system("clear")
						criar_barra("python-executive")
						print(Fore.CYAN + "=python==hora==fechar==hostsys=")
						print(Fore.CYAN + "												  desligar")
						print(Fore.CYAN + "												  reiniciar")
						subfuncesc = input("subfunc: ")
						if subfuncesc == "desligar":
								confirmar = input("desligar?(s/n):")
								if confirmar == "s":
										os.system("sh ./pyOS/system/hostsys/shutdown.sh")
						elif subfuncesc == "reiniciar":
								confirmar = input("reiniciar?(s/n): ")
								if confirmar == "s":
										os.system("sh ./pyOS/system/hostsys/restart.sh")
		elif app == "quit":
				quit()
		elif app in apps:
				abrirapp(app)
		elif app.isdigit():
				if int(app) in atalhos:
						abrirapp(atalhos[int(app)])
		elif app.lower() == "a":
			os.system('clear')
			criar_barra("python-executive")
			view_all()
		else:
				print(Fore.RED + "app não encontrado")
				time.sleep(3)