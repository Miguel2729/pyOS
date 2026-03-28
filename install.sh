#!/bin/bash

echo "🐧 Instalando pyOS - Compatível com qualquer distro Linux"
echo "========================================================"

# Detectar gerenciador de pacotes
if command -v apt &> /dev/null; then
    echo "📦 Distro: Debian/Ubuntu/Mint"
    sudo apt update
    sudo apt install -y git python3 python3-pip portaudio19-dev python3-dev nano
    
elif command -v pacman &> /dev/null; then
    echo "📦 Distro: Arch/Manjaro"
    sudo pacman -Syu --noconfirm git python python-pip portaudio nano
    
elif command -v dnf &> /dev/null; then
    echo "📦 Distro: Fedora/RHEL/CentOS"
    sudo dnf install -y git python3 python3-pip portaudio-devel python3-devel nano
    
elif command -v zypper &> /dev/null; then
    echo "📦 Distro: openSUSE"
    sudo zypper install -y git python3 python3-pip portaudio-devel python3-devel nano
    
elif command -v apk &> /dev/null; then
    echo "📦 Distro: Alpine"
    sudo apk update
    sudo apk add git python3 py3-pip portaudio-dev nano
    
elif command -v emerge &> /dev/null; then
    echo "📦 Distro: Gentoo"
    echo "⚠️  No Gentoo, você já sabe o que está fazendo!"
    sudo emerge dev-vcs/git dev-lang/python dev-python/pip media-libs/portaudio app-editors/nano
    
else
    echo "❌ Gerenciador de pacotes não reconhecido!"
    echo "Instale manualmente: git, python3, pip e portaudio19-dev(opcional)"
    exit 1
fi

PEPC=$(cat /usr/lib/python3.*/EXTERNALLY-MANAGED)

rm -f /usr/lib/python3.*/EXTERNALLY-MANAGED

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
pip3 install --user colorama requests

# Opcionais (pergunta ao usuário)
read -p "📸 Instalar suporte a imagens (Pillow)? [s/N]: " img
if [[ $img =~ ^[Ss]$ ]]; then
    pip3 install --user pillow==12.1.0
fi

read -p "🎤 Instalar reconhecimento de voz? [s/N]: " voz
if [[ $voz =~ ^[Ss]$ ]]; then
    pip3 install --user SpeechRecognition
    echo "⚠️  Pode precisar de: sudo apt install portaudio19-dev (Debian)"
fi

read -p "🌐 instalar suporte a sites? [s/N]: " sites
if [[ $sites =~ ^[Ss]$ ]]; then
    pip3 install --user beautifulsoup4
fi

read -p "🔊instalar suporte a reprodução de áudio e gravação de áudio? [s/N]: " audio
if [[ $audio =~ ^[Ss]$ ]]; then
    pip3 install --user pyaudio
fi

read -p "🎯 instalar suporte a gerenciamento de processos do sistema real?(psutil) [s/N]: " proc
if [[ $proc =~ ^[Ss]$ ]]; then
    pip3 install --user psutil
fi

read -p "▶️ deseja configurar o sistema para executar o pyOS automaticamente? [s/N]" autoexec
if [[ $autoexec =~ ^[Ss]$ ]]; then
    echo -e "cd $HOME/pyOS\npython3 pyOS.py" >> ~/.bashrc
    echo "✅ Configuração adicionada ao ~/.bashrc"
fi

echo -e $PEPC > /usr/lib/python3.*/EXTERNALLY-MANAGED

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
