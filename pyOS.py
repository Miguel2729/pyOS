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
import re
import sys
from datetime import datetime
import importlib
import subprocess
import time
import threading
import shutil
import traceback
import tempfile
import curses
from pathlib import Path
import colorama
versionparts = [5, 32]
version = f"v{versionparts[0]}.{versionparts[1]}"
dir_original = os.getcwd()

def criar_barra(msg):
	try:
		print(f'{msg}                  {pyOS_system.winbtn}')
	except Exception:
		print(f'{msg}                  ? ? ?')

def exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    
    
    # Primeiro limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # depois chama a função criar_barra
    criar_barra("system error")
    
    # Deleta pastas dentro de ./pyOS/proc
    proc_path = "./pyOS/proc"
    if os.path.exists(proc_path):
        for item in os.listdir(proc_path):
            item_path = os.path.join(proc_path, item)
            if os.path.isdir(item_path):
                try: 
                    shutil.rmtree(item_path)
                except: 
                    pass
    
    # Printa o erro
    print("⚠️ " + str(exc_value))
    
    # Menu de opções
    print("[1] reiniciar o sistema | [2] desligar o sistema")
    
    while True:
        try:
            opcao = input("Opção: ").strip()
            if opcao == "1":
                python = sys.executable
                os.execl(python, python, *sys.argv)
            elif opcao == "2":
                print("Desligando o sistema...")
                quit()
            else:
                print("Opção inválida! Digite 1 ou 2.")
        except (KeyboardInterrupt, EOFError):
            print("\nDesligando o sistema...")
            quit()

sys.excepthook = exception_handler

if not shutil.which("git"):
	os.system("apt install git")
	if not shutil.which("git"):
		os.system("pacman -S git")
	else:
		pass
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
pyOSdir = os.getcwd()
colorconfig = Fore.WHITE
processos_ativos = {}
os.chdir("./")
os.makedirs("apps/libs", exist_ok=True)
print(Fore.YELLOW + "trabalhando em atualizaçoes...")
os.system("pip install --upgrade pip")
time.sleep(8)
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
	
	with open("pyOS_calc.py", 'w') as mod3:
		mod3.write("def calc(n1, op, n2):\n\tres = eval(f\"{n1} {op} {n2}\")\n\treturn res")
	
	# Módulo pyOS_proc para o sistema (processos em background)
	with open("pyOS_proc.py", 'w') as mod4:
		mod4.write("""import os
import subprocess
import sys
import threading
import time

processos_ativos = {}

def verprocbac():
	\"\"\"Verifica e mantém processos rodando em background sem mensagens\"\"\"
	processos_com_erro = set()

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
								f.write(f"Processo terminou com código de erro: {returncode}\\n")
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
							f.write(f"Erro ao iniciar processo: {e}\\n")
			
			# Limpar processos finalizados
			for pid in list(processos_ativos.keys()):
				if processos_ativos[pid].poll() is not None:
					returncode = processos_ativos[pid].returncode
					if returncode != 0:
						processos_com_erro.add(pid)
						pid_path = os.path.join(proc_dir, pid)
						error_file = os.path.join(pid_path, 'error.log')
						with open(error_file, 'w') as f:
							f.write(f"Processo terminou com código de erro: {returncode}\\n")
					del processos_ativos[pid]
					
		except Exception:
			# Ignorar todos os erros silenciosamente
			pass
		
		time.sleep(3)

def init():
	\"\"\"Inicia o sistema de processos em background\"\"\"
	thread_processos = threading.Thread(target=verprocbac, daemon=True)
	thread_processos.start()
	return thread_processos

def stopall():
	\"\"\"Encerra todos os processos ativos\"\"\"
	for pid, processo in processos_ativos.items():
		try:
			processo.terminate()
		except:
			pass
	processos_ativos.clear()
""")
	
	os.chdir(diratual)
	os.makedirs("apps/libs", exist_ok=True)
	os.chdir("./apps/libs")
	
	with open('pyOS_app.py', 'w') as mod1app:
		mod1app.write(f"""import pyfiglet
from colorama import Fore
ver = {versionparts}
def fonts(fonte, texto):
	text = pyfiglet.figlet.format(texto, font=fonte)

def colors(cor):
	if cor == 'azul':
		return Fore.BLUE
	if cor == 'ciano':
		return Fore.CYAN
	if cor == 'roxo':
		return Fore.MAGENTA
	if cor == 'amarelo':
		return Fore.YELLOW
	if cor == 'vermelho':
		return Fore.RED
	if cor == 'normal':
		return Fore.WHITE""")
	
	# pyOS_proc para apps (criação de processos)
	with open("pyOS_appproc.py", 'w') as mod2app:
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
	os.system(f"chmod -R 744 {proc_path}")
	
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
		return procpid, None
""")
	
	with open("pyOS_vm.py", "w") as mod3app:
		mod3app.write("""# pyOS_vm.py - EMULADOR REAL
import threading
import struct

class VMEmulator:
	def __init__(self, ram_size=1024):  # 1MB RAM
		# MEMÓRIA FÍSICA (emulação real)
		self.ram = bytearray(ram_size * 1024)  # 1MB em bytes
		
		# REGISTRADORES REAIS (x86-like)
		self.registers = {
			'EAX': 0, 'EBX': 0, 'ECX': 0, 'EDX': 0,
			'ESI': 0, 'EDI': 0, 'EBP': 0, 'ESP': 0x1000,  # Stack pointer
			'EIP': 0x100,  # Instruction pointer
			'EFLAGS': 0
		}
		
		# INSTRUÇÕES SUPORTADAS (opcodes reais)
		self.instructions = {
			0x88: self.mov_rm8_r8,    # MOV [mem], reg
			0x89: self.mov_rm32_r32,  # MOV [mem], reg32
			0xB8: self.mov_eax_imm32, # MOV EAX, immediate
			0x01: self.add_rm32_r32,  # ADD [mem], reg
			0x83: self.add_rm32_imm8, # ADD [mem], immediate8
			0xEB: self.jmp_rel8,      # JMP short
		}
		
		self.running = False
		self.cpu_thread = threading.Thread(target=self.cpu_cycle)
	
	def start(self):
		\"\"\"Inicia a emulação REAL\"\"\"
		self.running = True
		self.cpu_thread.start()
		print(\"CPU Emulator iniciado!\")
	
	def stop(self):
		self.running = False
	
	def cpu_cycle(self):
		\"\"\"Ciclo de fetch-decode-execute REAL\"\"\"
		while self.running:
			# FETCH: Busca opcode da memória no EIP
			eip = self.registers['EIP']
			if eip >= len(self.ram):
				break
				
			opcode = self.ram[eip]
			
			# DECODE: Identifica instrução
			if opcode in self.instructions:
				# EXECUTE: Executa instrução
				self.instructions[opcode]()
			else:
				print(f\"Instrução não implementada: 0x{opcode:02X}\")
				self.registers['EIP'] += 1
	
	# --- INSTRUÇÕES IMPLEMENTADAS ---
	
	def mov_rm8_r8(self):
		\"\"\"MOV byte [mem], reg8 - Opcode 0x88\"\"\"
		eip = self.registers['EIP']
		modrm = self.ram[eip + 1]  # ModR/M byte
		
		# Decodifica endereço e registrador
		reg = (modrm >> 3) & 0x07
		rm = modrm & 0x07
		
		# Simples: MOV [EDI], AL
		if rm == 7:  # EDI
			address = self.registers['EDI']
			if reg == 0:  # AL
				self.ram[address] = self.registers['EAX'] & 0xFF
		
		self.registers['EIP'] += 2
	
	def mov_eax_imm32(self):
		\"\"\"MOV EAX, immediate32 - Opcode 0xB8\"\"\"
		eip = self.registers['EIP']
		
		# Lê 4 bytes do immediate
		immediate = struct.unpack('<I', bytes(self.ram[eip+1:eip+5]))[0]
		self.registers['EAX'] = immediate
		
		self.registers['EIP'] += 5
	
	def add_rm32_imm8(self):
		\"\"\"ADD [mem], immediate8 - Opcode 0x83\"\"\"
		eip = self.registers['EIP']
		modrm = self.ram[eip + 1]
		immediate = self.ram[eip + 2]
		
		# ADD [EAX], imm8
		if (modrm & 0xC7) == 0x00:
			address = self.registers['EAX']
			current = struct.unpack('<I', bytes(self.ram[address:address+4]))[0]
			result = (current + immediate) & 0xFFFFFFFF
			self.ram[address:address+4] = struct.pack('<I', result)
		
		self.registers['EIP'] += 3
	
	def jmp_rel8(self):
		\"\"\"JMP short - Opcode 0xEB\"\"\"
		eip = self.registers['EIP']
		offset = self.ram[eip + 1]
		
		# Calcula salto relativo
		if offset > 127:
			offset -= 256  # Complemento de 2
		
		self.registers['EIP'] += 2 + offset
	
	def load_binary(self, data, address=0x100):
		\"\"\"Carrega código binário REAL na memória\"\"\"
		for i, byte in enumerate(data):
			if address + i < len(self.ram):
				self.ram[address + i] = byte
		
		self.registers['EIP'] = address
		print(f\"Programa carregado em 0x{address:04X}\")
""")
	
	os.chdir(diratual)
	print("Módulos instalados com sucesso!")

def instalar_hostsys():
    diroriginal = os.getcwd()
    os.chdir("./pyOS/system/hostsys")
    
    # Scripts de reinício e desligamento
    with open("restart.sh", 'w') as restart_sys:
        restart_sys.write('#!/bin/bash\nclear\nreboot')
    
    with open("shutdown.sh", 'w') as quit_sys:
        quit_sys.write("#!/bin/bash\nclear\npoweroff")
    
    # Script de rede corrigido
    with open("network.sh", "w") as net_sys:
        net_sys.write(r"""#!/bin/bash

# networking.sh - Script completo para gerenciamento de rede em Linux
# Autor: Auto-generated
# Versão: 1.0

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para mostrar uso
show_usage() {
    echo -e "${GREEN}Networking.sh - Script de Gerenciamento de Rede${NC}"
    echo "Uso: $0 [opção]"
    echo ""
    echo "Opções:"
    echo "  status      - Mostrar status da rede"
    echo "  interfaces  - Listar interfaces de rede"
    echo "  ip          - Mostrar endereços IP"
    echo "  routes      - Mostrar tabela de roteamento"
    echo "  dns         - Mostrar servidores DNS"
    echo "  ports       - Mostrar portas abertas"
    echo "  connections - Mostrar conexões de rede"
    echo "  restart     - Reiniciar serviço de rede"
    echo "  test        - Testar conectividade"
    echo "  all         - Executar todas as verificações"
    echo "  --help      - Mostrar esta ajuda"
    echo ""
}

# Função para verificar se é root
check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo -e "${YELLOW}Aviso: Alguns comandos podem requerer privilégios de root${NC}"
        return 1
    fi
    return 0
}

# Função para mostrar status da rede
show_status() {
    echo -e "${BLUE}=== STATUS DA REDE ===${NC}"
    ip link show
    echo ""
}

# Função para listar interfaces
show_interfaces() {
    echo -e "${BLUE}=== INTERFACES DE REDE ===${NC}"
    echo -e "${GREEN}Interfaces disponíveis:${NC}"
    ip -o link show | awk -F': ' '{print $2}'
    echo ""
    
    echo -e "${GREEN}Interfaces com detalhes:${NC}"
    ip addr show
    echo ""
}

# Função para mostrar endereços IP
show_ip() {
    echo -e "${BLUE}=== ENDEREÇOS IP ===${NC}"
    
    # IPv4
    echo -e "${GREEN}Endereços IPv4:${NC}"
    ip -4 addr show | grep -E "inet " | awk '{print $2 " on " $NF}'
    echo ""
    
    # IPv6
    echo -e "${GREEN}Endereços IPv6:${NC}"
    ip -6 addr show | grep -E "inet6 " | awk '{print $2 " on " $NF}'
    echo ""
    
    # IP público (requer internet)
    echo -e "${GREEN}IP Público:${NC}"
    curl -s ifconfig.me 2>/dev/null || echo "Não foi possível obter IP público"
    echo -e "\n"
}

# Função para mostrar rotas
show_routes() {
    echo -e "${BLUE}=== TABELA DE ROTEAMENTO ===${NC}"
    
    echo -e "${GREEN}Tabela de roteamento IPv4:${NC}"
    ip -4 route show
    echo ""
    
    echo -e "${GREEN}Tabela de roteamento IPv6:${NC}"
    ip -6 route show
    echo ""
}

# Função para mostrar DNS
show_dns() {
    echo -e "${BLUE}=== SERVIDORES DNS ===${NC}"
    
    # Verificar resolv.conf
    if [ -f /etc/resolv.conf ]; then
        echo -e "${GREEN}/etc/resolv.conf:${NC}"
        grep -E "nameserver|search|domain" /etc/resolv.conf
    fi
    echo ""
    
    # Verificar systemd-resolve (se disponível)
    if command -v systemd-resolve &> /dev/null; then
        echo -e "${GREEN}systemd-resolve --status:${NC}"
        systemd-resolve --status 2>/dev/null | grep -A5 "DNS Servers" || echo "Não foi possível obter status do systemd-resolve"
    fi
    
    # Testar resolução DNS
    echo -e "${GREEN}Teste de resolução DNS:${NC}"
    nslookup google.com 2>/dev/null | grep "Server\|Address" || echo "Falha no teste DNS"
    echo ""
}

# Função para mostrar portas abertas
show_ports() {
    echo -e "${BLUE}=== PORTAS ABERTAS ===${NC}"
    
    if command -v ss &> /dev/null; then
        echo -e "${GREEN}Portas listening (ss):${NC}"
        ss -tuln | head -20
    elif command -v netstat &> /dev/null; then
        echo -e "${GREEN}Portas listening (netstat):${NC}"
        netstat -tuln | head -20
    else
        echo -e "${RED}Erro: nem ss nem netstat encontrados${NC}"
    fi
    echo ""
}

# Função para mostrar conexões
show_connections() {
    echo -e "${BLUE}=== CONEXÕES DE REDE ===${NC}"
    
    if command -v ss &> /dev/null; then
        echo -e "${GREEN}Conexões estabelecidas (ss):${NC}"
        ss -tun | head -20
    elif command -v netstat &> /dev/null; then
        echo -e "${GREEN}Conexões estabelecidas (netstat):${NC}"
        netstat -tun | head -20
    fi
    echo ""
}

# Função para reiniciar rede
restart_network() {
    check_root
    echo -e "${BLUE}=== REINICIANDO SERVIÇO DE REDE ===${NC}"
    
    if systemctl is-active NetworkManager &> /dev/null; then
        echo -e "${GREEN}Reiniciando NetworkManager...${NC}"
        systemctl restart NetworkManager
    elif systemctl is-active network &> /dev/null; then
        echo -e "${GREEN}Reiniciando network service...${NC}"
        systemctl restart network
    elif command -v service &> /dev/null; then
        echo -e "${GREEN}Reiniciando networking service...${NC}"
        service networking restart
    else
        echo -e "${RED}Erro: Não foi possível identificar o gerenciador de rede${NC}"
    fi
    echo ""
}

# Função para testar conectividade
test_connectivity() {
    echo -e "${BLUE}=== TESTES DE CONECTIVIDADE ===${NC}"
    
    # Teste de loopback
    echo -e "${GREEN}Teste de loopback:${NC}"
    ping -c 2 127.0.0.1 >/dev/null 2>&1 && echo -e "${GREEN}✓ Loopback OK${NC}" || echo -e "${RED}✗ Loopback FALHOU${NC}"
    echo ""
    
    # Teste de gateway
    gateway=$(ip route show default 2>/dev/null | awk '/default/ {print $3}')
    if [ -n "$gateway" ]; then
        echo -e "${GREEN}Teste de gateway ($gateway):${NC}"
        ping -c 2 $gateway >/dev/null 2>&1 && echo -e "${GREEN}✓ Gateway OK${NC}" || echo -e "${RED}✗ Gateway FALHOU${NC}"
    else
        echo -e "${YELLOW}Gateway não encontrado${NC}"
    fi
    echo ""
    
    # Teste de DNS
    echo -e "${GREEN}Teste de DNS (google.com):${NC}"
    ping -c 2 google.com >/dev/null 2>&1 && echo -e "${GREEN}✓ DNS OK${NC}" || echo -e "${RED}✗ DNS FALHOU${NC}"
    echo ""
    
    # Teste de internet
    echo -e "${GREEN}Teste de internet:${NC}"
    curl -s --connect-timeout 5 http://www.example.com > /dev/null && \
        echo -e "${GREEN}✓ Internet OK${NC}" || echo -e "${RED}✗ Internet FALHOU${NC}"
    echo ""
}

# Função para mostrar todas as informações
show_all() {
    show_status
    show_interfaces
    show_ip
    show_routes
    show_dns
    show_ports
    show_connections
    test_connectivity
}

# Tratamento de argumentos
case "$1" in
    "status")
        show_status
        ;;
    "interfaces")
        show_interfaces
        ;;
    "ip")
        show_ip
        ;;
    "routes")
        show_routes
        ;;
    "dns")
        show_dns
        ;;
    "ports")
        show_ports
        ;;
    "connections")
        show_connections
        ;;
    "restart")
        restart_network
        ;;
    "test")
        test_connectivity
        ;;
    "all")
        show_all
        ;;
    "--help"|"-h"|"help")
        show_usage
        ;;
    *)
        echo -e "${RED}Erro: Opção inválida${NC}"
        echo ""
        show_usage
        exit 1
        ;;
esac

exit 0
""")
    
    os.chmod("shutdown.sh", 0o755)
    os.chmod("restart.sh", 0o755)
    os.chmod("network.sh", 0o755)
    # Voltar ao diretório original
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

def rgb_to_ansi(r, g, b):
    return f"\\033[38;2;{r};{g};{b}m"

def pixels_to_ascii_colored(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        if isinstance(pixel, tuple):
            r, g, b = pixel[:3]
            char = ASCII_CHARS[sum(pixel[:3]) // 75]
            ansi_color = rgb_to_ansi(r, g, b)
            ascii_str += f"{ansi_color}{char}"
        else:
            char = ASCII_CHARS[pixel // 25]
            ascii_str += char
    return ascii_str

def display_ascii_image(path):
    if not os.path.exists(path):
        print("❌ Caminho da imagem inválido.")
        return
    
    try:
        image = Image.open(path)
        image = resize_image(image)
        
        if image.mode != 'RGB':
            image = image.convert('RGB')
            
        ascii_str = pixels_to_ascii_colored(image)
        img_width = image.width
        ascii_img = "\\n".join([ascii_str[i:i+img_width] for i in range(0, len(ascii_str), img_width)])
        print(ascii_img + "\\033[0m")
        
    except Exception as e:
        print(f"❌ Erro ao processar imagem: {e}")
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
    os.makedirs("./pyOS/proc", exist_ok=True)  # Este é o correto
    os.makedirs("./pyOS/systemRes", exist_ok=True)
    os.system("ln -s ../../systemRes ./pyOS/system/res")
    instalar_modulos()
    instalar_hostsys()
    gerar_recursos_sistema()
    with open("syscreated.txt", "w") as conclu:
    	conclu.write("True")

        


pyOS()

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


sys.path.insert(0, "pyOS/system/modules")
try:
	import pyOS_hora
	import pyOS_system
	import pyOS_calc
	import pyOS_proc
except Exception as e:
	print(f"erro ao importar modulos: {e}")
	
# aplicativos
def calculadora():
	print("operadores:")
	print("divisão: /")
	print("multiplicação: *")
	print("somar: +")
	print("subtrair: -")
	print("divisão inteira: //")
	print("potencia: **")
	print('resto de divisao: %')
	try:
		# apenas numeros
		n1 = float(input("numero 1: "))
		n2 = float(input("numero 2: "))
	except ValueError:
		print("não é número")
		time.sleep(5)
		return
	op = input("operador matematico: ")
	# sem divisão por zero
	if  n2 == 0 and op == "/":
		print("erro de divisão por zero")
		time.sleep(5)
		return
	# apenas operadores validos
	elif op == "/" or op == "*" or op == "+" or op == "-" or op == "//" or op == "**" or op == "%":
		res = pyOS_calc.calc(n1, op, n2)
		if str(res).endswith(".0"):
			res = int(res)
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
                print("conteudo:\n" + content.read())
            
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
		print("opcoes:\n1. atualizar o pip\n2. informacoes\n3. desinstalar")
		opcao = input("acao:")
		if opcao == "1":
			pyOS_system.upgpip()
		elif opcao == "2":
			print("info:")
			print("nome: pyOS")
			print(f"versão: {version}")
			print(f"desenvolvedor: miguel cabral")
			print("objetivo: ajudar pessoas com sistema linux sem interface grafica")
			time.sleep(2)
		elif opcao == "3":
			os.system("clear")
			criar_barra("desinstalar")
			uninstall()
	else:
		print("invalido!")
		
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
        
        if coman == "quit":
            os.chdir(dir_original)
            executing = False
            
        elif coman.startswith("cd "):
            dire = coman[3:]
            os.chdir(dire)
        elif coman == "unlock_sys":
            apps["system-mgr"] = sysmgr
            print("system-mgr unlocked")
        elif coman.startswith("noProtection "):
            os.system(coman[len("noProtection "):])
         
        
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
aeac = {}
def appsInstalados():
	global aeac
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

			app_path = os.path.join("apps", f"{app}.py")
			if os.path.exists(app_path):
				try:
					# CORREÇÃO: Adicionar o path correto para apps/libs
					libs_path = os.path.abspath("./apps/libs")
					
					res_path = os.path.abspath("./pyOS/systemRes")
					
					if libs_path not in sys.path:
						sys.path.insert(0, libs_path)
					if res_path not in sys.path:
						sys.path.insert(0, res_path)
					
					with open(app_path, 'r', encoding='utf-8') as f:
						codigo_app = f.read()
					
					# Executar o código do app
					exec(codigo_app, {"__builtins__": __builtins__}, {})
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
					libs_path = os.path.abspath("./apps/libs")
					if libs_path not in sys.path:
						sys.path.insert(0, libs_path)
					
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
def messages():
    """
    App de mensagens em rede - usuários podem conversar de qualquer lugar
    """
    
    # Arquivos de armazenamento
    MSGS_FILE = "msgs.json"
    USERS_FILE = "name_user.txt"
    
    # Configurações do servidor
    HOST = '0.0.0.0'  # Escuta em todas as interfaces
    PORT = 12345
    server_socket = None
    clients = {}  # {client_socket: {'id': id, 'name': name}}
    
    def inicializar_arquivos():
        """Inicializa os arquivos se não existirem"""
        if not os.path.exists(MSGS_FILE):
            with open(MSGS_FILE, 'w') as f:
                json.dump({}, f)
        
        if not os.path.exists(USERS_FILE):
            with open(USERS_FILE, 'w') as f:
                f.write("")
    
    def gerar_id():
        """Gera um ID único para o usuário"""
        return random.randint(1000, 9999)
    
    def carregar_usuarios():
        """Carrega os usuários do arquivo"""
        try:
            with open(USERS_FILE, 'r') as f:
                linhas = f.readlines()
            
            usuarios = {}
            for linha in linhas:
                if linha.strip():
                    id_user, nome = linha.strip().split('|')
                    usuarios[int(id_user)] = nome
            return usuarios
        except:
            return {}
    
    def salvar_usuario(id_user, nome):
        """Salva um novo usuário"""
        with open(USERS_FILE, 'a') as f:
            f.write(f"{id_user}|{nome}\n")
    
    def carregar_mensagens():
        """Carrega todas as mensagens"""
        try:
            with open(MSGS_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def salvar_mensagens(mensagens):
        """Salva todas as mensagens"""
        with open(MSGS_FILE, 'w') as f:
            json.dump(mensagens, f, indent=2)
    
    def adicionar_mensagem(remetente_id, destinatario_id, mensagem):
        """Adiciona uma nova mensagem"""
        mensagens = carregar_mensagens()
        
        chave = f"{min(remetente_id, destinatario_id)}_{max(remetente_id, destinatario_id)}"
        
        if chave not in mensagens:
            mensagens[chave] = []
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensagens[chave].append({
            'remetente': remetente_id,
            'mensagem': mensagem,
            'timestamp': timestamp
        })
        
        salvar_mensagens(mensagens)
        return mensagens[chave]
    
    def obter_mensagens(user1_id, user2_id):
        """Obtém mensagens entre dois usuários"""
        mensagens = carregar_mensagens()
        chave = f"{min(user1_id, user2_id)}_{max(user1_id, user2_id)}"
        
        if chave in mensagens:
            return mensagens[chave]
        return []
    
    def iniciar_servidor():
        """Inicia o servidor de mensagens"""
        global server_socket
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            server_socket.bind((HOST, PORT))
            server_socket.listen(5)
            print(f"🚀 Servidor iniciado em {HOST}:{PORT}")
            print("Aguardando conexões...")
            
            while True:
                client_socket, addr = server_socket.accept()
                print(f"✅ Nova conexão de {addr}")
                
                # Thread para lidar com o cliente
                client_thread = threading.Thread(
                    target=handle_client, 
                    args=(client_socket, addr)
                )
                client_thread.daemon = True
                client_thread.start()
                
        except Exception as e:
            print(f"❌ Erro no servidor: {e}")
    
    def handle_client(client_socket, addr):
        """Lida com as mensagens de um cliente"""
        try:
            # Receber dados de login
            login_data = client_socket.recv(1024).decode('utf-8')
            user_id, user_name = login_data.split('|')
            user_id = int(user_id)
            
            clients[client_socket] = {'id': user_id, 'name': user_name}
            print(f"👤 {user_name} (ID: {user_id}) conectado")
            
            # Enviar confirmação
            client_socket.send("CONNECTED".encode('utf-8'))
            
            while True:
                # Receber mensagem do cliente
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                
                if data.startswith("GET_MSGS|"):
                    # Cliente solicitando mensagens
                    destinatario_id = int(data.split('|')[1])
                    mensagens = obter_mensagens(user_id, destinatario_id)
                    client_socket.send(json.dumps(mensagens).encode('utf-8'))
                
                elif data.startswith("SEND_MSG|"):
                    # Cliente enviando mensagem
                    partes = data.split('|')
                    destinatario_id = int(partes[1])
                    mensagem = partes[2]
                    
                    adicionar_mensagem(user_id, destinatario_id, mensagem)
                    client_socket.send("MSG_SENT".encode('utf-8'))
                    
                    # Notificar destinatário se estiver online
                    notify_destinatario(user_id, destinatario_id, mensagem)
                
                elif data == "LIST_USERS":
                    # Listar usuários
                    usuarios = carregar_usuarios()
                    client_socket.send(json.dumps(usuarios).encode('utf-8'))
                
        except Exception as e:
            print(f"❌ Erro com cliente {addr}: {e}")
        finally:
            if client_socket in clients:
                print(f"👋 {clients[client_socket]['name']} desconectou")
                del clients[client_socket]
            client_socket.close()
    
    def notify_destinatario(remetente_id, destinatario_id, mensagem):
        """Notifica o destinatário sobre nova mensagem"""
        for client, info in clients.items():
            if info['id'] == destinatario_id:
                try:
                    client.send(f"NEW_MSG|{remetente_id}|{mensagem}".encode('utf-8'))
                except:
                    pass
    
    def conectar_como_cliente():
        """Conecta como cliente ao servidor"""
        try:
            server_host = input("Digite o IP do servidor (ou Enter para localhost): ").strip()
            if not server_host:
                server_host = 'localhost'
            
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_host, PORT))
            
            # Login
            usuarios = carregar_usuarios()
            
            if not usuarios:
                print("❌ Nenhum usuário cadastrado localmente!")
                return
            
            print("\n📋 Seus usuários locais:")
            for id_user, nome in usuarios.items():
                print(f"   ID: {id_user} - Nome: {nome}")
            
            try:
                user_id = int(input("\nDigite seu ID: "))
                if user_id not in usuarios:
                    print("❌ ID não encontrado!")
                    return
            except ValueError:
                print("❌ ID inválido!")
                return
            
            # Enviar dados de login
            login_data = f"{user_id}|{usuarios[user_id]}"
            client_socket.send(login_data.encode('utf-8'))
            
            # Aguardar confirmação
            response = client_socket.recv(1024).decode('utf-8')
            if response == "CONNECTED":
                print(f"✅ Conectado como {usuarios[user_id]}!")
                menu_cliente(client_socket, user_id, usuarios[user_id])
            else:
                print("❌ Falha na conexão!")
                
        except Exception as e:
            print(f"❌ Erro ao conectar: {e}")
    
    def menu_cliente(client_socket, user_id, user_name):
        """Menu do cliente conectado"""
        while True:
            print("\n" + "="*50)
            print(f"🌟 CHAT - {user_name} (ID: {user_id})")
            print("="*50)
            print("1. Conversar com usuário")
            print("2. Atualizar lista de usuários")
            print("3. Sair")
            
            opcao = input("\nDigite sua opção: ").strip()
            
            if opcao == '1':
                chat_usuario(client_socket, user_id, user_name)
            elif opcao == '2':
                listar_usuarios_online(client_socket)
            elif opcao == '3':
                print("👋 Saindo...")
                break
            else:
                print("❌ Opção inválida!")
    
    def listar_usuarios_online(client_socket):
        """Lista usuários online no servidor"""
        try:
            client_socket.send("LIST_USERS".encode('utf-8'))
            data = client_socket.recv(4096).decode('utf-8')
            usuarios = json.loads(data)
            
            print("\n📋 Usuários disponíveis:")
            for id_user, nome in usuarios.items():
                print(f"   ID: {id_user} - Nome: {nome}")
                
        except Exception as e:
            print(f"❌ Erro ao listar usuários: {e}")
    
    def chat_usuario(client_socket, user_id, user_name):
        """Interface de chat com outro usuário"""
        try:
            destinatario_id = int(input("\nDigite o ID do usuário para conversar: "))
            
            print(f"\n💬 Conversando... (Digite '/quit' para sair)")
            print("-" * 50)
            
            # Thread para receber mensagens em tempo real
            recebendo = True
            
            def receber_mensagens():
                while recebendo:
                    try:
                        client_socket.settimeout(1.0)
                        data = client_socket.recv(1024).decode('utf-8')
                        if data.startswith("NEW_MSG|"):
                            partes = data.split('|')
                            remetente_id = int(partes[1])
                            mensagem = partes[2]
                            print(f"\n💬 Nova mensagem de {remetente_id}: {mensagem}")
                            print("Digite sua mensagem: ", end="")
                    except socket.timeout:
                        continue
                    except:
                        break
            
            receiver_thread = threading.Thread(target=receber_mensagens)
            receiver_thread.daemon = True
            receiver_thread.start()
            
            # Carregar histórico
            client_socket.send(f"GET_MSGS|{destinatario_id}".encode('utf-8'))
            historico_data = client_socket.recv(4096).decode('utf-8')
            historico = json.loads(historico_data)
            
            for msg in historico:
                timestamp = msg['timestamp']
                remetente = msg['remetente']
                print(f"[{timestamp}] {remetente}: {msg['mensagem']}")
            
            # Loop de envio de mensagens
            while True:
                mensagem = input("Você: ").strip()
                
                if mensagem.lower() == '/quit':
                    recebendo = False
                    break
                elif mensagem:
                    client_socket.send(f"SEND_MSG|{destinatario_id}|{mensagem}".encode('utf-8'))
                    response = client_socket.recv(1024).decode('utf-8')
                    if response == "MSG_SENT":
                        print("✅ Mensagem enviada!")
                
        except Exception as e:
            print(f"❌ Erro no chat: {e}")
    
    def criar_usuario_local():
        """Cria um novo usuário local"""
        nome = input("Digite seu nome: ").strip()
        if not nome:
            print("Nome não pode estar vazio!")
            return
        
        usuarios = carregar_usuarios()
        
        # Gerar ID único
        while True:
            id_user = gerar_id()
            if id_user not in usuarios:
                break
        
        salvar_usuario(id_user, nome)
        print(f"\n✅ Usuário criado com sucesso!")
        print(f"📋 Seus dados:")
        print(f"   ID: {id_user}")
        print(f"   Nome: {nome}")
        print("\n⚠️  Anote seu ID, você precisará dele para conectar!")
    
    def menu_principal():
        """Menu principal do app"""
        inicializar_arquivos()
        
        while True:
            print("\n" + "="*50)
            print("🌟 APP DE MENSAGENS EM REDE")
            print("="*50)
            print("1. Iniciar como SERVIDOR (hospedar chat)")
            print("2. Conectar como CLIENTE (entrar no chat)")
            print("3. Criar usuário local")
            print("4. Sair")
            
            opcao = input("\nDigite sua opção: ").strip()
            
            if opcao == '1':
                print("\n🎯 Iniciando servidor...")
                print("⚠️  Compartilhe seu IP para outros se conectarem")
                iniciar_servidor()
                
            elif opcao == '2':
                print("\n🔌 Conectando como cliente...")
                conectar_como_cliente()
                
            elif opcao == '3':
                criar_usuario_local()
                
            elif opcao == '4':
                print("👋 Saindo do app...")
                break
            else:
                print("❌ Opção inválida!")
    
    # Iniciar o app
    menu_principal()

def images():
	sys.path.insert(0, "./pyOS/systemRes")
	import ascii_image_display as aid
	print("1. ver fotos\n2. visualizar fotos\n0. sair")
	escolha = input("escolha: ")
	if escolha == "1":
		os.chdir("imgs/")
		os.listdir()
		os.chdir("..")
	elif escolha == "2":
		caminho = "imgs/"+ input("foto(apenas o arquivo nome com extensão): ")
		aid.display_ascii_image(caminho)
		input("aperte enter para sair")
	elif escolha == "0":
		return

		



def sysmgr():
	print(f"pyOS {version} - {os.getcwd()}")
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
			
			
def abrirapp(app):
	os.system("clear")
	
	try:
		criar_barra(app)
		apps[app]()
	except KeyError:
		print(Fore.RED + "app não encontrado")
		time.sleep(3)



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
                    print(f"     📝 {evento['descricao']}")
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
                print(f"      ⏰ {evento['hora']} - {evento['titulo']}")
    
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
	print("""1. ver versao do python
2. abrir editor
3. instalar biblioteca
0. sair
""")
	while True:
		esc = input("opcao: ")
		if esc == "1":
			os.system(f"python --version")
		elif esc == "2":
			abrirEditor()
		elif esc == "0":
			break
		elif esc == "3":
			pacote = input("pacote: ")
			res = subprocess.run(["pip", "install", pacote], shell=True, text=True)
			if res.stderr:
				print("erro")
			else:
				print("pacote instalado com sucesso, reiniciando...")
				os.execv(sys.executable, ['python3'] + sys.argv)




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
                comando = f'"{sys.executable}" "{temp_file}"'
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
        CHANNELS = 1              # Mono
        RATE = 44100              # 44.1kHz sample rate
        CHUNK = 1024              # Tamanho do buffer
        
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

def processos_sistema():
    """
    App para gerenciar processos do sistema operacional real
    Versão corrigida para problemas de permissão no Linux
    """
    import os
    import sys
    import time
    import platform
    from datetime import datetime
    
    def verificar_psutil():
        """Verifica se psutil está instalado, se não, instala"""
        try:
            import psutil
            return True
        except ImportError:
            print("📦 Instalando psutil para gerenciamento de processos...")
            try:
                import subprocess
                subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
                print("✅ psutil instalado com sucesso!")
                import psutil
                return True
            except Exception as e:
                print(f"❌ Erro ao instalar psutil: {e}")
                return False
    
    def obter_info_sistema_segura():
        """Obtém informações do sistema de forma segura (com tratamento de permissões)"""
        print("\n" + "="*60)
        print("💻 INFORMAÇÕES DO SISTEMA")
        print("="*60)
        
        # Informações básicas sempre disponíveis
        print(f"Sistema: {platform.system()} {platform.release()}")
        print(f"Arquitetura: {platform.machine()}")
        
        try:
            import psutil
            
            # CPU (com fallback)
            try:
                cpu_percent = psutil.cpu_percent(interval=0.5)
                cpu_count = psutil.cpu_count()
                print(f"CPU: {cpu_percent}% de uso ({cpu_count} núcleos)")
            except (PermissionError, FileNotFoundError) as e:
                print(f"CPU: Informação limitada (permissão negada)")
            
            # Memória (geralmente funciona mesmo sem permissões elevadas)
            try:
                mem = psutil.virtual_memory()
                mem_total_gb = mem.total / (1024**3)
                mem_used_gb = mem.used / (1024**3)
                mem_percent = mem.percent
                print(f"RAM: {mem_used_gb:.1f}GB / {mem_total_gb:.1f}GB ({mem_percent}%)")
            except:
                print(f"RAM: Informação não disponível")
            
            # Disco
            try:
                disk = psutil.disk_usage('/')
                disk_total_gb = disk.total / (1024**3)
                disk_used_gb = disk.used / (1024**3)
                disk_percent = disk.percent
                print(f"Disco: {disk_used_gb:.1f}GB / {disk_total_gb:.1f}GB ({disk_percent}%)")
            except:
                print("Disco: Informação não disponível")
            
            # Boot
            try:
                boot_time = datetime.fromtimestamp(psutil.boot_time())
                uptime = datetime.now() - boot_time
                print(f"Tempo ligado: {uptime}")
            except:
                pass
                
        except ImportError:
            print("⚠️  psutil não disponível - informações limitadas")
        
        print("="*60)
    
    def listar_processos_seguro(tipo="todos", limite=20):
        """Lista processos de forma segura, tratando erros de permissão"""
        processos = []
        
        try:
            import psutil
            
            if tipo == "ativos":
                # Processos ativos (com tratamento de erro)
                for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                    try:
                        pinfo = proc.info
                        # Usar get() para evitar KeyError
                        cpu = pinfo.get('cpu_percent', 0)
                        mem = pinfo.get('memory_percent', 0)
                        if cpu > 0.1 or mem > 0.1:
                            processos.append(pinfo)
                    except (psutil.NoSuchProcess, psutil.AccessDenied, PermissionError):
                        continue
                    except Exception:
                        continue
            
            elif tipo == "usuário":
                # Processos do usuário atual
                current_user = None
                try:
                    current_user = psutil.Process().username()
                except:
                    pass
                
                if current_user:
                    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent']):
                        try:
                            pinfo = proc.info
                            if pinfo.get('username') == current_user:
                                processos.append(pinfo)
                        except:
                            continue
            
            else:  # todos
                # Todos os processos que conseguimos acessar
                for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                    try:
                        processos.append(proc.info)
                    except (psutil.NoSuchProcess, psutil.AccessDenied, PermissionError):
                        continue
                    except Exception:
                        continue
        
        except ImportError:
            print("❌ psutil não está disponível")
            return []
        except Exception as e:
            print(f"⚠️  Erro ao listar processos: {e}")
            return []
        
        # Ordenar por uso de CPU (se disponível)
        try:
            processos.sort(key=lambda x: x.get('cpu_percent', 0), reverse=True)
        except:
            pass
        
        return processos[:limite]
    
    def mostrar_processos(processos):
        """Mostra lista de processos formatada"""
        if not processos:
            print("❌ Nenhum processo encontrado ou permissão insuficiente")
            return
        
        print("\n" + "="*90)
        print(f"{'PID':^8} {'NOME':<35} {'CPU%':^6} {'MEM%':^6} {'STATUS':<10}")
        print("="*90)
        
        for proc in processos:
            pid = str(proc.get('pid', 'N/A'))
            name = proc.get('name', 'Desconhecido')[:24]
            cpu = f"{proc.get('cpu_percent', 0):.1f}" if proc.get('cpu_percent') is not None else "N/A"
            mem = f"{proc.get('memory_percent', 0):.1f}" if proc.get('memory_percent') is not None else "N/A"
            
            # Tentar obter status (com tratamento de erro)
            status = "N/A"
            try:
                import psutil
                p = psutil.Process(proc['pid'])
                status = p.status()[:9]
            except:
                pass
            
            print(f"{pid:^8} {name:<25} {cpu:^6} {mem:^6} {status:<10}")
    
    def detalhes_processo_seguro(pid):
        """Mostra detalhes de um processo com tratamento de segurança"""
        try:
            import psutil
            p = psutil.Process(pid)
            
            print(f"\n🔍 DETALHES DO PROCESSO PID: {pid}")
            print("-" * 50)
            
            try:
                print(f"Nome: {p.name()}")
            except:
                print("Nome: Acesso negado")
            
            try:
                print(f"Usuário: {p.username()}")
            except:
                print("Usuário: Acesso negado")
            
            try:
                print(f"Status: {p.status()}")
            except:
                print("Status: Acesso negado")
            
            # Recursos (com tratamento)
            print(f"\n🔧 RECURSOS:")
            try:
                cpu_percent = p.cpu_percent(interval=0.1)
                print(f"CPU: {cpu_percent}%")
            except:
                print("CPU: Acesso negado")
            
            try:
                mem_info = p.memory_info()
                print(f"Memória RSS: {mem_info.rss / (1024**2):.1f} MB")
            except:
                print("Memória: Acesso negado")
            
            print("-" * 50)
            
        except psutil.NoSuchProcess:
            print(f"❌ Processo com PID {pid} não existe")
        except (psutil.AccessDenied, PermissionError):
            print(f"⚠️  Acesso negado ao processo {pid}")
            print("   Execute com privilégios elevados (sudo) para mais informações")
        except Exception as e:
            print(f"❌ Erro: {e}")
    
    def matar_processo_seguro(pid):
        """Tenta matar um processo com verificações de segurança"""
        try:
            import psutil
            p = psutil.Process(pid)
            
            # Tentar obter nome (pode falhar por permissão)
            nome = "Desconhecido"
            try:
                nome = p.name()
            except:
                pass
            
            print(f"\n⚠️  ATENÇÃO: Você está prestes a matar o processo:")
            print(f"PID: {pid}")
            print(f"Nome: {nome}")
            
            # Verificar se é um processo crítico do sistema
            processos_criticos = ['systemd', 'init', 'kernel', 'Xorg', 'gnome-shell', 'plasmashell']
            if any(critico in nome.lower() for critico in processos_criticos):
                print("🚨 ALERTA: Este parece ser um processo crítico do sistema!")
                print("   Matá-lo pode causar instabilidade ou travamento!")
            
            confirmar = input("\nTem certeza ABSOLUTA? (digite 'SIM' para confirmar): ")
            
            if confirmar.upper() == 'SIM':
                print(f"Encerrando processo {pid}...")
                
                try:
                    # Tenta terminar graciosamente
                    p.terminate()
                    time.sleep(1)
                    
                    # Verifica se ainda está rodando
                    if p.is_running():
                        print("Processo não respondeu, forçando...")
                        try:
                            p.kill()
                        except:
                            print("❌ Não foi possível forçar encerramento")
                    
                    print(f"✅ Processo {pid} encerrado")
                    
                except (psutil.AccessDenied, PermissionError):
                    print("❌ Permissão negada. Execute com sudo/administrador")
                except Exception as e:
                    print(f"❌ Erro ao encerrar: {e}")
            
            else:
                print("❌ Operação cancelada.")
                
        except psutil.NoSuchProcess:
            print(f"❌ Processo com PID {pid} não existe")
        except (psutil.AccessDenied, PermissionError):
            print(f"⚠️  Acesso negado (execute com privilégios elevados)")
        except Exception as e:
            print(f"❌ Erro: {e}")
    
    def monitorar_recursos_seguro():
        """Monitora recursos com tratamento de erros de permissão"""
        print("\n📊 MONITOR DE RECURSOS - Pressione Ctrl+C para sair")
        print("-" * 60)
        
        try:
            import psutil
        except ImportError:
            print("❌ psutil não disponível para monitoramento")
            return
        
        try:
            update_count = 0
            while True:
                # Limpa a tela
                print("\033[H\033[J", end="")
                
                print("📊 MONITOR DE RECURSOS EM TEMPO REAL")
                print("-" * 60)
                print(f"Atualização: #{update_count}")
                
                # CPU (com fallback)
                try:
                    cpu_percent = psutil.cpu_percent(interval=0.5)
                    print(f"\n💻 CPU: {cpu_percent:.1f}%")
                    bar_length = min(20, int(cpu_percent / 5))
                    bar = "█" * bar_length + "░" * (20 - bar_length)
                    print(f"  [{bar}]")
                except:
                    print("\n💻 CPU: Monitoramento não disponível")
                
                # Memória
                try:
                    mem = psutil.virtual_memory()
                    mem_percent = mem.percent
                    print(f"\n🧠 MEMÓRIA: {mem_percent:.1f}%")
                    bar_length = min(20, int(mem_percent / 5))
                    bar = "█" * bar_length + "░" * (20 - bar_length)
                    print(f"  [{bar}] {mem.used / (1024**3):.1f}GB / {mem.total / (1024**3):.1f}GB")
                except:
                    print("\n🧠 MEMÓRIA: Monitoramento não disponível")
                
                # Processos (limitado devido a permissões)
                try:
                    processos = []
                    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
                        try:
                            info = proc.info
                            if info.get('cpu_percent', 0) > 1.0:  # > 1% CPU
                                processos.append(info)
                        except:
                            continue
                    
                    # Ordenar e pegar top 5
                    processos.sort(key=lambda x: x.get('cpu_percent', 0), reverse=True)
                    
                    if processos:
                        print(f"\n🔥 PROCESSOS ATIVOS (top {min(3, len(processos))}):")
                        for proc in processos[:3]:
                            name = proc.get('name', 'N/A')[:20]
                            cpu = proc.get('cpu_percent', 0)
                            print(f"  {name:<20} CPU: {cpu:5.1f}%")
                except:
                    print("\n🔥 PROCESSOS: Monitoramento limitado")
                
                print(f"\n⏱️  {datetime.now().strftime('%H:%M:%S')} | Ctrl+C para parar")
                
                update_count += 1
                time.sleep(2)
                
        except KeyboardInterrupt:
            print("\n🛑 Monitoramento interrompido")
        except Exception as e:
            print(f"\n❌ Erro no monitoramento: {e}")
    
    def verificar_permissoes():
        """Verifica se temos permissões adequadas"""
        sistema = platform.system()
        
        print("\n🔐 VERIFICAÇÃO DE PERMISSÕES:")
        print("-" * 40)
        
        if sistema == "Linux":
            # Verifica se é root no Linux
            if os.geteuid() == 0:
                print("✅ Executando como root (sudo)")
                print("   Acesso completo aos processos do sistema")
                return True
            else:
                print("⚠️  Executando como usuário normal no Linux")
                print("   Algumas informações podem ser limitadas")
                print("\n💡 Dica: Execute com 'sudo' para acesso completo")
                return False
        elif sistema == "Windows":
            # No Windows, verifica se é administrador
            try:
                import ctypes
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin:
                    print("✅ Executando como Administrador")
                    return True
                else:
                    print("⚠️  Executando como usuário normal no Windows")
                    print("   Alguns recursos podem ser limitados")
                    return False
            except:
                print("ℹ️  Sistema Windows detectado")
                return True
        else:
            print(f"ℹ️  Sistema {sistema} detectado")
            return True
    
    # Verificar se psutil está instalado
    if not verificar_psutil():
        print("❌ Não é possível executar sem psutil.")
        time.sleep(3)
        return
    
    # Menu principal
    while True:
        print("\n" + "="*60)
        print("🖥️  GERENCIADOR DE PROCESSOS DO SISTEMA")
        print("="*60)
        
        # Verificar permissões
        tem_permissao = verificar_permissoes()
        
        # Obter informações do sistema (de forma segura)
        obter_info_sistema_segura()
        
        print("\n📋 MENU PRINCIPAL:")
        print("1. 📋 Listar processos (acesso disponível)")
        print("2. 🔥 Listar processos ativos")
        print("3. 🔍 Detalhes de processo (por PID)")
        print("4. 🚫 Matar processo (cuidado!)")
        print("5. 📊 Monitorar recursos")
        if not tem_permissao:
            print("6. 💡 Dicas para acesso completo")
        print("0. ↩️  Voltar ao menu principal")
        
        try:
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                processos = listar_processos_seguro("todos", 100)
                mostrar_processos(processos)
                input("\nPressione Enter para continuar...")
                
            elif opcao == "2":
                processos = listar_processos_seguro("ativos", 15)
                mostrar_processos(processos)
                input("\nPressione Enter para continuar...")
                
            elif opcao == "3":
                try:
                    pid_input = input("Digite o PID do processo (ou Enter para ver lista): ").strip()
                    if pid_input:
                        pid = int(pid_input)
                        detalhes_processo_seguro(pid)
                    else:
                        # Mostrar lista primeiro
                        processos = listar_processos_seguro("todos", 10)
                        mostrar_processos(processos)
                        try:
                            pid = int(input("\nDigite o PID para detalhes: "))
                            detalhes_processo_seguro(pid)
                        except ValueError:
                            print("❌ PID inválido")
                except ValueError:
                    print("❌ PID deve ser um número!")
                input("\nPressione Enter para continuar...")
                
            elif opcao == "4":
                try:
                    pid_input = input("Digite o PID do processo a matar: ").strip()
                    if pid_input:
                        pid = int(pid_input)
                        matar_processo_seguro(pid)
                    else:
                        print("❌ PID não pode estar vazio")
                except ValueError:
                    print("❌ PID deve ser um número!")
                input("\nPressione Enter para continuar...")
                
            elif opcao == "5":
                monitorar_recursos_seguro()
                
            elif opcao == "6" and not tem_permissao:
                print("\n💡 DICAS PARA ACESSO COMPLETO:")
                print("-" * 40)
                sistema = platform.system()
                if sistema == "Linux":
                    print("No Linux, execute o pyOS com sudo:")
                    print("  sudo python3 pyOS.py")
                    print("\nOu execute apenas este app com sudo:")
                    print("  sudo python3 -c 'import psutil; print(psutil.cpu_percent())'")
                elif sistema == "Windows":
                    print("No Windows, execute o terminal como Administrador:")
                    print("  1. Clique direito no terminal/CMD")
                    print("  2. Escolha 'Executar como Administrador'")
                    print("  3. Execute o pyOS normalmente")
                print("\n⚠️  ATENÇÃO: Execute com privilégios apenas se necessário!")
                print("   Processos do sistema podem ser críticos.")
                input("\nPressione Enter para continuar...")
                
            elif opcao == "0":
                print("👋 Voltando ao menu principal...")
                break
                
            else:
                print("❌ Opção inválida!")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Operação interrompida pelo usuário")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")
            time.sleep(2)

def uninstall():
    """
    App para desinstalar o pyOS e seus componentes
    """
    import shutil
    import json
    import sys
    
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
        print(f"{BOLD}{RED}║{RESET}{BOLD}                 DESINSTALADOR pyOS                    {RESET}{RED}║{RESET}")
        print(f"{BOLD}{RED}║{RESET}{BOLD}              Versão {version}                         {RESET}{RED}║{RESET}")
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

apps = {
    "calculadora": calculadora,
    "notepad": notepad,
    "config": config,
    "terminal": terminal,
    "gerenciador de arquivos": fileManager,
    "appsInstalados": appsInstalados,
    "navegador": navegador_tui,
    "gerenciador de tarefas": taskmgr,
    "mensagens": messages,
    "fotos": images,
    "diagnostico de rede": diagnosticar_rede,
    "agenda": agenda,
    "controle de internet": internet_control,
    "python": python3,
    "audio": audio,
    "processos-sistema": processos_sistema
}

try:
	pyOS_proc.init()
except Exception:
	pass
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
	
	criar_barra("python-executive")
	
	print(Fore.CYAN + "=python==hora==fechar==hostsys=\n")
	print(colorconfig + "apps:")
	nomes = sorted(apps.keys())
	for i in range(0, len(nomes), 4):
		# Imprime até 4 apps por linha
		for j in range(4):
			if i + j < len(nomes):
				print(nomes[i + j], end='  ')
		print()  # Nova linha após cada grupo de 
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
			pyOS_proc.stopall()
			quit()
		elif funcesc == "hostsys":
			os.system("clear")
			criar_barra("python-executive")
			print(Fore.CYAN + "=python==hora==fechar==hostsys=")
			print(Fore.CYAN + "                                                  desligar")
			print(Fore.CYAN + "                                                  reiniciar")
			subfuncesc = input("subfunc: ")
			if subfuncesc == "desligar":
				confirmar = input("desligar?(s/n):")
				if confirmar == "s":
					pyOS_proc.stopall()
					os.system("sh ./pyOS/system/hostsys/shutdown.sh")
			elif subfuncesc == "reiniciar":
				confirmar = input("reiniciar?(s/n): ")
				if confirmar == "s":
					pyOS_proc.stopall()
					os.system("sh ./pyOS/system/hostsys/restart.sh")
	elif app == "quit":
		pyOS_proc.stopall()
		quit()
	elif app in apps:
		abrirapp(app)
	else:
		print(Fore.RED + "app não encontrado")
		time.sleep(3)
