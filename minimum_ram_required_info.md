# 📊 Requisitos Mínimos de RAM - pyOS v6.2

## 🎯 Recomendações de Memória para Melhor Experiência

### **Resumo Rápido**
| Nível de Experiência | RAM Mínima Livre | Performance | Travamentos |
|---------------------|------------------|-------------|-------------|
| ⭐⭐⭐⭐⭐ Ideal | 1 GB+ | Fluida | Quase nenhum |
| ⭐⭐⭐⭐ Bom | 768 MB | Muito boa | Raros |
| ⭐⭐⭐☆ Aceitável | 512 MB | Boa | Ocasionais |
| ⭐⭐☆☆ Mínimo | 384 MB | Limitada | Frequentes |
| ⭐☆☆☆ Crítico | < 256 MB | Lenta | Constantes |

## 🔍 Análise Detalhada

### **Memória Necessária por Componente**
| Componente | RAM Consumida | Observações |
|------------|---------------|-------------|
| **pyOS Core** | 50-80 MB | Sistema básico + interface |
| **Apps Básicos** | +15-30 MB | Calculadora, Notepad, Config |
| **Terminal/File Manager** | +25-45 MB | Operações de sistema |
| **Navegador TUI** | +60-100 MB | 🔥 **Mais pesado** (BeautifulSoup + requests) |
| **Antivírus** | +30-50 MB | Análise de código + SQLite |
| **Paint/Editor Python** | +25-40 MB | Curses + PIL |
| **Áudio** | +20-35 MB | PyAudio + gravação/reprodução |
| **Processos Background** | +10-20 MB cada | Gerenciador de tarefas, apps em segundo plano |
| **Múltiplos Apps** | +50-100 MB | Vários apps abertos simultaneamente |

### 🔴🟡🟢 Consumo de RAM Aproximado no Uso
| Ação | Consumo Aproximado |
| ---------------------- | --------------- |
| Em repouso (menu principal) | **120-200 MB** |
| Com 1-2 apps leves abertos | **200-350 MB** |
| Com vários apps abertos | **350-500 MB** |
| Com navegador + outros apps | **500-800 MB** |
| Com todos os recursos ativos | **800 MB - 1.2 GB** |
| Uso normal recomendado | **300-500 MB** |

## ⚠️ Apps que Mais Consomem RAM

### **🔥 Alto Consumo (Evitar em RAM limitada)**
1. **Navegador TUI** - BeautifulSoup + requests + renderização HTML
2. **Antivírus** - Análise estática + banco de dados SQLite
3. **Paint** - Curses + PIL (processamento de imagem)
4. **App de Mensagens** - Sockets + threads + rede
5. **Gerenciador de Tarefas** - Monitoramento contínuo de processos
6. **Áudio** - PyAudio + gravação em tempo real
7. **Gerenciador de Discos** - Operações com parted + lsblk

### **💚 Baixo Consumo (Seguros para RAM limitada)**
- Calculadora
- Notepad
- Configurações
- Agenda (eventos simples)
- Diagnóstico de Rede (testes pontuais)
- Controle de Internet
- Fotos (ASCII art)
- Terminal (comandos simples)

## 🆕 Novidades que Impactam RAM na v6.2

### **Novos Apps que Adicionaram Consumo**
| App | Consumo Adicional | Motivo |
|-----|------------------|---------|
| Antivírus | +30-50 MB | SQLite + análise estática |
| Áudio | +20-35 MB | PyAudio + buffers de áudio |
| Paint | +25-40 MB | PIL + curses |
| Gerenciador de Discos | +15-25 MB | parted + lsblk |

### **Melhorias de Performance**
- Otimização de imports lazy loading
- Cache de módulos reduzido
- Limpeza automática de memória em apps fechados

## 🛠️ Otimizações para Sistemas com Pouca RAM

### **Antes de Executar o pyOS**
```bash
# Liberar memória cache
sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches

# Fechar aplicativos pesados
pkill chrome firefox libreoffice thunderbird

# Verificar RAM disponível
free -h

# Desativar serviços desnecessários
sudo systemctl stop bluetooth cups avahi-daemon
```

### **Dentro do pyOS para Economizar RAM**
- Evite abrir o **navegador** e **antivírus** ao mesmo tempo
- Use o **terminal** em vez do **gerenciador de arquivos** quando possível
- Feche apps quando não estiver usando (não apenas minimize)
- Evite apps com **threads em background** desnecessárias
- Use o **modo de segurança** com `--security-mode` para desativar apps em segundo plano

### **Configurações Recomendadas para RAM Limitada**
1. Desative apps de inicialização automática no `app_boot_perms.json' ou desautorize todos pelas configuracoes
2. Use apenas um app por vez
3. Evite o navegador se tiver menos de 512 MB livres
4. Reinicie o pyOS periodicamente para liberar memória

## 📊 Comparativo por Versão

| Versão | RAM Mínima | RAM Recomendada | Apps Base |
|--------|-----------|-----------------|-----------|
| v5.x | 256 MB | 512 MB | 12 apps |
| v6.0 | 384 MB | 768 MB | 14 apps |
| v6.2 | 384 MB | 1 GB | 16 apps (novos: antivírus, áudio, paint) |

## ⚠️ Sinais de Pouca RAM
- Travamentos frequentes
- Apps demorando para abrir
- Interface lenta
- Mensagens de erro relacionadas a memória
- Sistema fechando apps instalados abertos sozinho

## 💡 Dica Final
Se você tem **menos de 384 MB de RAM livre**, recomenda-se:
1. Usar apenas apps leves (calculadora, notepad, agenda)
2. Evitar navegador, antivírus e paint
3. Fechar outros programas antes de executar o pyOS
4. Considerar usar o pyOS em modo texto puro sem recursos gráficos extras