#!/bin/bash

echo "🐧 Instalando pyOS - Compatível com qualquer distro Linux"
echo "========================================================"

# Detectar gerenciador de pacotes
if command -v apt &> /dev/null; then
    echo "📦 Distro: Debian/Ubuntu/Mint"
    sudo apt update
    sudo apt install -y git python3 python3-pip
    
elif command -v pacman &> /dev/null; then
    echo "📦 Distro: Arch/Manjaro"
    sudo pacman -Syu --noconfirm git python python-pip
    
elif command -v dnf &> /dev/null; then
    echo "📦 Distro: Fedora/RHEL/CentOS"
    sudo dnf install -y git python3 python3-pip
    
elif command -v zypper &> /dev/null; then
    echo "📦 Distro: openSUSE"
    sudo zypper install -y git python3 python3-pip
    
elif command -v apk &> /dev/null; then
    echo "📦 Distro: Alpine"
    sudo apk update
    sudo apk add git python3 py3-pip
    
elif command -v emerge &> /dev/null; then
    echo "📦 Distro: Gentoo"
    echo "⚠️  No Gentoo, você já sabe o que está fazendo!"
    sudo emerge --ask dev-vcs/git dev-lang/python dev-python/pip
    
else
    echo "❌ Gerenciador de pacotes não reconhecido!"
    echo "Instale manualmente: git, python3, pip"
    exit 1
fi

# Clonar ou atualizar pyOS
if [ -d "pyOS" ]; then
    echo "📁 Atualizando pyOS existente..."
    cd pyOS
    git pull
else
    echo "📥 Clonando repositório pyOS..."
    git clone https://github.com/Miguel2729/pyOS
    cd pyOS
fi

# Instalar dependências Python
echo "🐍 Instalando dependências Python..."
pip3 install --user colorama requests pyfiglet

# Opcionais (pergunta ao usuário)
read -p "📸 Instalar suporte a imagens (Pillow)? [s/N]: " img
if [[ $img =~ ^[Ss]$ ]]; then
    pip3 install --user pillow
fi

read -p "🎤 Instalar reconhecimento de voz? [s/N]: " voz
if [[ $voz =~ ^[Ss]$ ]]; then
    pip3 install --user SpeechRecognition
    echo "⚠️  Pode precisar de: sudo apt install portaudio19-dev (Debian)"
fi

read -p "🌐 instalar suporte a sites? [s/N]: " sites
if [[ $sites =~ ^[Ss]$ ]]; then
    pip3 install --user beautifulsoup4
    echo "⚠️ pode precisar de: sudo apt install portaudio19-dev (Debian)"
fi

read -p "🔊instalar suporte a reprodução de áudio e gravação de áudio? [s/N 
]: " audio

if [[ $audio =~ ^[Ss]$ ]]; then
    pip3 install --user pyaudio
fi

read -p "🎯 instalar suporte a gerenciamento de processos do sistema real?(psutil) [s/N]: " proc
if [[ $proc =~ ^[Ss]$ ]]; then
    pip3 install --user psutil
fi

read -p "▶️ deseja configurar o sistema para executar o pyOS automaticamente? [s/N]" autoexec
if [[ $autoexec =~ ^[Ss]$ ]]; then
    echo "cd $HOME/pyOS\npython3 pyOS.py" >> ./bashrc
fi

echo ""
echo "✅ INSTALAÇÃO COMPLETA!"
echo "======================="
echo "Para executar:"
echo "  cd pyOS"
echo "  python3 pyOS.py"
echo ""
echo "Dicas:"
echo "  •Use 'func' no menu para opções do sistema"
echo "  • 'terminal' abre um terminal protegido"
echo "  • 'quit' para sair"
