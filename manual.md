# 🛠 Manual de Instalação e Uso — pyOS v5.22

## 📥 Instalação

### Linux
1. Execute: `apt install git` e `apt install python`  
   - Se der erro, tente: `apt install python3`
2. Se persistir o erro, pare aqui.
3. Verifique a versão do Python:  
   - `python --version` ou `python3 --version`  
   - Deve ser 3.6 ou superior
4. Navegue até o diretório desejado:  
   - `cd [caminho desejado para o pyOS]`
5. Clone o repositório:  
   - `git clone https://github.com/Miguel2729/pyOS.git`

### Windows
1. Clique em **Code**
2. Clique em **Download ZIP**
3. Extraia o arquivo ZIP
4. Instale o Python (se necessário): [python.org](https://www.python.org)
5. Acesse a pasta extraída
6. Execute com Python

## ▶️ Executar o pyOS (Linux)
- Dentro da pasta do pyOS, execute:  
  `python pyOS.py` ou `python3 pyOS.py`

---

## 📘 Manual de Uso

### Tela Inicial
- Barra superior com nome do sistema e controles
- Lista de aplicativos disponíveis
- Prompt para digitar o nome do app desejado

### 📱 Aplicativos e Funções

#### 1. 🧮 Calculadora
- Digite `calculadora` para abrir
- Operações: `+`, `-`, `*`, `/`
- Exemplo: `5 + 3`

#### 2. 📝 Notepad
- Digite `notepad` para abrir
- Opções:
  1. Ver todas as notas
  2. Adicionar nova nota
  3. Remover nota existente
  4. Sair
  5. ver conteudo de nota

#### 3. ⚙️ Configurações
- Digite `config` para abrir
- Alterar cores do texto:
  - 1: Azul, 2: Vermelho, 3: Amarelo, 4: Magenta, 5: Verde, 6: Normal
- Outras opções (digite 0):
  - Atualizar pip
  - Ver informações do sistema

#### 4. 💻 Terminal
- Digite `terminal` para abrir
- Comandos:
  - `cd [pasta]`
  - `ls`
  - `python -m http.server`
  - `quit`
- ⚠️ Comandos perigosos são bloqueados

#### 5. 📁 Gerenciador de Arquivos
- Digite `gerenciador de arquivos` para abrir
- Opções:
  1. Listar arquivos e pastas
  2. Criar novo arquivo
  3. Ler conteúdo de arquivo
  4. Deletar arquivo/pasta
  5. Mudar de diretório
  6. Voltar diretório anterior
  7. Editar arquivo existente
  0. Sair

#### 6. 📦 Apps Instalados
- Digite `appsInstalados` para abrir
- Gerenciar apps:
  1. Instalar dependências
  2. Executar apps simples (.py)
  3. Ver dependências
  4. Instalar app da internet
  5. Instalar biblioteca Python
  6. Instalar app completo (Git)
  7. Executar apps completos
  8. Configurar arquivo principal
  9. Ver arquivos de apps

#### 7. 🌐 Navegador TUI
- Digite `navegador` para abrir
- Digite URL ou termo de busca
- Renderiza:
  - Títulos e cabeçalhos
  - Parágrafos
  - Formulários interativos

#### 8. 📊 Gerenciador de Tarefas
- Digite `gerenciador de tarefas` para abrir
- Visualize e encerre processos
- Monitoramento automático
#### 9. 💬 mensagens
- Digite `mensagens` para abrir
- sistema de mensagens
-Opções:
 1. hospeda uma conversa
 2. entra numa conversa
 3. cria um usuário
 4. sai
#### 10. 🖼 fotos
- Digite `fotos` para abrir
- para ver suas fotos
- Armazene as fotos em imgs/
- Opções:
  - 1 ve as fotos,
  - 2 visualiza foto,
  - 0 sai


---

## 🔧 Funções Especiais

### Barra Superior
- Digite `func` para acessar:
  - `python`: versão do Python e pip
  - `hora`: horário atual
  - `fechar`: encerrar o pyOS
  - `hostsys`: controle do sistema
    - `desligar`
    - `reiniciar`

### 📋 Atalhos Rápidos
- `quit`: sair do pyOS
- `func -> fechar`: encerrar com segurança
- `Ctrl+C`: interromper operação

---

## 🔒 Segurança
- Senha opcional no início
- Bloqueio de comandos perigosos
- Execução segura em sandbox

---

## 💡 Dicas
1. Use `func -> fechar` para encerrar corretamente
2. Apps instalados ficam em `./apps/`
3. Processos rodam em background
4. Use o gerenciador de tarefas para monitorar
5. Personalize cores no menu de configurações

---

## 🆘 Solução de Problemas
- App não encontrado: verifique o nome
- Erro de permissão: execute com privilégios
- Dependência faltando: use `appsInstalados` → opção 1 ou 5

---

**FIM DO MANUAL DE USO**
