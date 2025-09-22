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
| **pyOS Core** | 25-40 MB | Sistema básico + interface |
| **Apps Básicos** | +10-20 MB | Calculadora, Notepad, Config |
| **Terminal/File Manager** | +15-25 MB | Operações de sistema |
| **Navegador TUI** | +30-50 MB | 🔥 **Mais pesado** |
| **Processos Background** | +5-10 MB cada | Gerenciador de tarefas |
| **Múltiplos Apps** | +20-40 MB | Vários apps abertos |

### **Uso Típico de RAM**
- **Uso Básico:** 50-80 MB
- **Uso Médio:** 80-120 MB  
- **Uso Avançado:** 120-200 MB
- **Uso Máximo:** 200-300 MB

## ⚠️ Apps que Mais Consomem RAM

### **🔥 Alto Consumo (Evitar em RAM limitada)**
1. **Navegador TUI** - BeautifulSoup + requests
2. **Gerenciador de Arquivos** - Com muitos arquivos
3. **Apps Externos Complexos** - Dependências pesadas

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
