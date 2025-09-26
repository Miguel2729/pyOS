# 📊 Requisitos Mínimos de RAM - pyOS

## 🎯 Recomendações de Memória para Melhor Experiência

### **Resumo Rápido**
| Nível de Experiência | RAM Mínima Livre | Performance | Travamentos |
|---------------------|------------------|-------------|-------------|
| ⭐⭐⭐⭐⭐ Ideal | 512 MB+ | Fluida | Quase nenhum |
| ⭐⭐⭐☆ Aceitável | 384 MB | Boa | Ocasionais |
| ⭐⭐☆☆ Mínimo | 256 MB | Limitada | Frequentes |
| ⭐☆☆☆ Crítico | < 256 MB | Lenta | Constantes |

## 🔍 Análise Detalhada

### **Memória Necessária por Componente**
| Componente | RAM Consumida | Observações |
|------------|---------------|-------------|
| **pyOS Core** | 30-50 MB | Sistema básico + interface |
| **Apps Básicos** | +10-25 MB | Calculadora, Notepad, Config |
| **Terminal/File Manager** | +20-35 MB | Operações de sistema |
| **Navegador TUI** | +40-70 MB | 🔥 **Mais pesado** |
| **Processos Background** | +8-15 MB cada | Gerenciador de tarefas |
| **Múltiplos Apps** | +30-60 MB | Vários apps abertos |

### 🔴🟡🟢 consumo de ram aproximado no uso
| ação | consumo aproximado |
| ---------------------- | --------------- |
| em repouso | **90-160 MB** |
| com 1-2 apps abertos | **160-280 MB** |
| com vários apps abertos + navegador | **280-550 MB** |
| máximo | **400-650 MB** |
| uso normal | **220-380 MB** |

## ⚠️ Apps que Mais Consomem RAM

### **🔥 Alto Consumo (Evitar em RAM limitada)**
1. **Navegador TUI** - BeautifulSoup + requests
2. **App de Mensagens** - Sockets + threads
3. **Gerenciador de Arquivos** - Com muitos arquivos
4. **Apps Externos Complexos** - Dependências pesadas

### **💚 Baixo Consumo (Seguros)**
- Calculadora
- Notepad
- Configurações
- Terminal (comandos simples)

## 🛠️ Otimizações para Sistemas com Pouca RAM

### **Antes de Executar o pyOS**
```bash
# Liberar memória
sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches

# Fechar aplicativos pesados
pkill chrome firefox libreoffice thunderbird

# Verificar RAM disponível
free -h
