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

## events/(5.28+)
- Armazena eventos da agenda

## system/

| subpasta | função
| -------- | ------ |
| hostsys | Armazenar arquivos sh para interagir com o sistema host |
| modules | Armazena módulos do pyOS(exemplos: pyOS_hora.py, pyOS_system.py, pyOS_proc.py, pyOS_calc.py) |
| tmp | arquivos temporários do pyOS(tmp, tmpdir, temp) |

## arquivos do pyOS
- passwordexist.txt(permissão 600): configuração que a senha foi configurada como sim ou não
- senha.txt(permissão 600): senha

# systemRes/
- voice_input.py
#### como usar voice_input.py:
exemplo: 
```python
import voice_input
fala = voice_input.get_voice_input()
print(fala)
```
- ascii_image_display.py
#### como usar ascii_image_display.py:
```python
import ascii_image_display as aid
aid.display_ascii_image("fotos/foto1.png")
```

# como criar apps pro pyOS
### método de script simples
 crie um script.py e de uma URL dd download a ele
#### instalar:
 no appsInstalados selecione 4
 e depois digite a url
#### executar
 no AppsInstalados digite 2 e depois o nome do arquivo python sem o .py
### método de repositório github
crie um repositório github com os arquivos do app
#### instalar:
 no appsInstalados digite 6 e depois a url para git clone
#### executar
 digite 7 e depois o nome do repositório que foi clonado
 se der erro de arquivo não encontrado digite 8 e defina o arquivo main do app, desde que seja .py

## como fazer processo em Segundo Plano no seu app
 importe o módulo na pasta libs/(dentro de apps/ onde os apps são instalados) pyOS_proc.py. para criar o processo no código:
 pyOS_proc.criarproc(script, nome)

 - substituindo script pelo script do processo(string) e nome pelo nome do processo(também string)

## como app pode verificar a versão do pyOS no pyOS?:
 usando a variável ver do pyOS_app
 exemplo:
 ```python 
sys.path.insert(0, "./libs")
from pyOS_app import ver
if ver[0] >= 5 and ver[1] >= 25:
    print("compatível")
else:
    print("use pyOS v5.25 ou superior para usar o app")
    quit()
# código se não cair no else...
```
 o índice 0 da lista version é o major e o índice 1 é o minor
