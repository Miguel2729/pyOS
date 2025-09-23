# Estrutura do pyOS

Os arquivos do pyOS são criados automaticamente.

### Diretórios do pyOS/

### systemRes/(v5.14+)
- As versões baseadas no pyOS ou apps podem usar arquivos aqui

### system/(v3.4+)
- Arquivos do sistema (hostsys, modules, tmp)

### proc/(v5.13+)
- Processos em background

### apps/(v2.3+)
Armazena os aplicativos instalados

#### apps/libs/(v2.3+)
- Armazena bibliotecas para apps

## notes/(v5.15+)
- notas do bloco de notas

## system/

| subpasta | função
| -------- | ------ |
| hostsys | Armazenar arquivos sh para interagir com o sistema host |
| modules | Armazena módulos do pyOS(exemplos: pyOS_hora.py, pyOS_system.py) |
| tmp | arquivos temporários do pyOS |

## arquivos do pyOS
- passwordexist.txt(permissão 600): configuração que a senha foi configurada como sim ou não
- senha.txt(permissão 600): senha
