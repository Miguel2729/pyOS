# 🛠 Manual de Instalação e Uso — pyOS v6.2

## 📥 Instalação

### Linux
1. Verifique a versão do Python:  
   - `python --version` ou `python3 --version`  
   - Deve ser 3.8 ou superior
2. Navegue até o diretório desejado:  
   - `cd [caminho desejado para o pyOS]`
3. Baixe o pyOS:
   - Via git: `git clone https://github.com/Miguel2729/pyOS.git`
   - Ou baixe o ZIP manualmente

### Windows
- use WSL

## ▶️ Executar o pyOS
- Dentro da pasta do pyOS, execute:  
  `python pyOS.py` ou `python3 pyOS.py`

---

## 📘 Manual de Uso

### Tela Inicial
- Barra superior com nome do sistema e controles
- Lista de aplicativos disponíveis (em ordem alfabética)
- Prompt para digitar o **número** ou **nome** do app desejado

### Como executar um app:
- **Pelo número:** Digite o número que aparece na frente (ex: 0 para agenda)
- **Pelo nome:** Digite o nome completo (ex: calculadora)
- **Sair:** Digite `quit`
- **Funções do sistema:** Digite `func`

---

## 📱 Aplicativos Disponíveis

Os aplicativos são listados em ordem alfabética no menu principal:

| Nº | Nome | Descrição |
|---|---|---|
| 0 | agenda | Gerenciar eventos e lembretes |
| 1 | antivirus | Analisar apps em busca de malware |
| 2 | audio | Gravar e reproduzir áudio (WAV) |
| 3 | calculadora | Operações matemáticas básicas |
| 4 | config | Configurações do sistema |
| 5 | controle de internet | Conectar/desconectar da internet |
| 6 | diagnostico de rede | Verificar problemas de rede |
| 7 | fotos | Visualizar imagens como arte ASCII |
| 8 | gerenciador de arquivos | Explorar arquivos e pastas |
| 9 | gerenciador de tarefas | Ver e gerenciar processos do sistema |
| 10 | mensagens | Chat P2P entre usuários na mesma rede |
| 11 | navegador | Navegador web TUI com suporte a mouse |
| 12 | notepad | Bloco de notas simples |
| 13 | paint | Editor de desenho ASCII |
| 14 | python | Ambiente Python com editor e gerenciador de pacotes |
| 15 | terminal | Terminal Linux com proteções de segurança |

---

## 📱 Descrição dos Aplicativos

### 1. 📅 Agenda
- Gerencia eventos e compromissos
- Mostra automaticamente:
  - Data atual formatada
  - Eventos de hoje
  - Eventos próximos (próximos 3 dias)
- Opções:
  - Adicionar evento (data, hora, título, descrição)
  - Ver todos os eventos
  - Remover evento

### 2. 🛡️ Antivírus
- Analisa aplicativos em busca de código malicioso
- Verifica padrões perigosos (os.system, eval, subprocess, etc.)
- Opções:
  - Analisar app específico
  - Analisar todos os apps
  - Colocar em quarentena
  - Restaurar da quarentena
  - Whitelist/Blacklist

### 3. 🎵 Áudio
- Grava áudio do microfone (formato WAV)
- Reproduz arquivos de áudio
- Informações técnicas dos arquivos
- Gerencia arquivos em ./audio_files/

### 4. 🧮 Calculadora
- Operações: +, -, *, /, **, //, %
- Exemplo: 5 + 3

### 5. ⚙️ Configurações
- 1: Configurações de internet
- 2: Gerenciar aplicativos instalados (espaço, dados, desinstalar)
- 3: Desinstalar o pyOS
- 4: Gerenciador de discos (formatar, particionar, montar)

### 6. 🌐 Controle de Internet
- 1: Conectar à internet
- 2: Desconectar da internet
- 3: Verificar status da conexão

### 7. 🔧 Diagnóstico de Rede
- Verifica automaticamente:
  - Conectividade com a internet
  - Servidores DNS
  - Gateway de rede
  - Latência
- Sugere soluções para problemas detectados

### 8. 🖼 Fotos
- Visualiza imagens como arte ASCII
- Armazene as fotos em imgs/
- Opções:
  - Ver lista de fotos
  - Visualizar foto específica

### 9. 📁 Gerenciador de Arquivos
- Opções:
  1. Listar arquivos e pastas (com tamanhos)
  2. Criar novo arquivo
  3. Criar pasta
  4. Ler conteúdo de arquivo
  5. Deletar arquivo/pasta
  6. Mudar de diretório
  7. Voltar diretório anterior
  8. Editar arquivo (nano)
  9. Ativar/desativar mostrar arquivos ocultos
  10. Abrir arquivo com app específico

### 10. 📊 Gerenciador de Tarefas
- 1: Listar todos os processos
- 2: Top processos por CPU
- 3: Top processos por memória
- 4: Buscar processo por nome
- 5: Matar processo por PID
- 6: Matar processo por nome
- 7: Ver informações do sistema
- 8: Ver árvore de processos
- 9: Ver processos por usuário
- 10: Encontrar processo por porta
- 11: Iniciar novo processo

### 11. 💬 Mensagens
- Chat P2P entre dois usuários
- Opções:
  - 1: Criar sala (aguardar conexão)
  - 2: Entrar em sala existente
  - 3: Sair
- Use /sair para encerrar a conversa

### 12. 🌐 Navegador TUI
- Navegador web baseado em texto
- Atalhos:
  - U: Digitar URL
  - Tab: Selecionar elementos
  - Enter: Ativar link/botão
  - Setas: Navegar
  - M: Ativar/desativar mouse
  - R: Recarregar página
  - Q: Sair

### 13. 📝 Notepad
- Opções:
  1. Ver todas as notas
  2. Adicionar nova nota
  3. Remover nota existente
  4. Sair
  5. Ver conteúdo de nota específica

### 14. 🎨 Paint
- Editor de desenho ASCII
- Atalhos:
  - Setas: Mover cursor
  - U/D: Levantar/abaixar caneta
  - E: Alternar borracha
  - Tab: Mudar cor
  - B: Preencher tela
  - C: Limpar tela
  - S: Salvar como PNG

### 15. 🐍 Python
- 1: Ver versão do Python
- 2: Abrir editor Python
- 3: Instalar biblioteca
- 4: Mudar diretório do Python
- 5: Visualizar diretório atual

### 16. 💻 Terminal
- Terminal Linux com proteções
- Comandos bloqueados: rm -rf /, shutdown, etc.
- Comandos restritos só permitidos dentro da pasta ./pyOS
- Use quit ou exit para sair

---

## 🔧 Funções do Sistema (func)

No menu principal, digite `func` para acessar:

| Comando | Descrição |
|---------|-----------|
| python | Mostra versão do Python e pip |
| hora | Mostra horário atual |
| fechar | Encerra o pyOS |
| hostsys | Controle do sistema (desligar/reiniciar) |

### Exemplo:
app: func
func: hora

---

## 📁 Estrutura de Pastas

| Pasta | Descrição |
|-------|-----------|
| ./apps/ | Aplicativos instalados |
| ./workspace/ | Dados dos aplicativos |
| ./notes/ | Notas do bloco de notas |
| ./events/ | Eventos da agenda |
| ./audio_files/ | Arquivos de áudio |
| ./imgs/ | Imagens para visualização |
| ./pyOS/ | Arquivos do sistema (não modificar) |

---

## 🔒 Segurança

- Senha opcional na inicialização
- Comandos perigosos são bloqueados no terminal
- Acesso a arquivos do sistema é restrito
- Antivírus integrado para verificar apps
- Processos em background isolados

---

## 💡 Dicas

1. Use func -> fechar para encerrar corretamente
2. Apps instalados ficam em ./apps/
3. Use o gerenciador de tarefas para monitorar processos
4. Agenda: Adicione eventos com data no formato YYYY-MM-DD
5. Diagnóstico de rede: Use para solucionar problemas de conexão
6. Paint: Desenhos são salvos em ./desenhos/ como PNG
7. Áudio: Arquivos são salvos em formato WAV em ./audio_files/
8. use o aplicativo "instalador de apps" para instalar apps

---