#!/usr/bin/env python3
"""
Handler para arquivos .ppk - Abre o instalador com o arquivo selecionado
"""

import os
import sys
from pathlib import Path

# Adicionar diretório do app ao path
app_dir = Path(os.getcwd()).parent.parent / "apps" / "instalador de apps"
sys.path.insert(0, app_dir)

def main():
    """Abre o instalador com o arquivo .ppk"""
    if len(sys.argv) < 2:
        print("Uso: ppk.py <arquivo.ppk>")
        return
    
    arquivo_ppk = sys.argv[1]
    
    # Verificar se é .ppk
    if not arquivo_ppk.endswith('.ppk'):
        print(f"❌ {arquivo_ppk} não é um arquivo .ppk")
        return
    
    # Verificar se arquivo existe
    if not os.path.exists(arquivo_ppk):
        print(f"❌ Arquivo não encontrado: {arquivo_ppk}")
        return
    
    # Importar e executar o instalador
    try:
        from main import PPKInstaller
        installer = PPKInstaller()
        
        # Limpar tela e mostrar cabeçalho
        os.system('clear')
        installer.mostrar_cabecalho()
        
        print(f"📦 Abrindo: {os.path.basename(arquivo_ppk)}")
        print()
        
        # Instalar diretamente
        installer.instalar_ppk(arquivo_ppk)
        
        input("\nPressione Enter para sair...")
        
    except ImportError as e:
        print(f"❌ Erro ao carregar instalador: {e}")
        input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()