# Protótipo de Automação Digital: Controle de Produção e Qualidade

Este projeto é um protótipo de sistema de automação digital desenvolvido em Python para auxiliar no controle de produção e qualidade de peças em uma linha de montagem industrial. O sistema recebe dados de peças e as avalia automaticamente contra critérios de qualidade, gerenciando o empacotamento em caixas de capacidade limitada.

## ⚙️ Funcionamento do Sistema

O sistema é baseado na classe `ControleQualidade` que gerencia o fluxo de trabalho:

1.  **Cadastro e Inspeção:** O usuário insere o ID, peso, cor e comprimento da peça. A função `inspecionar_peca` aplica a lógica de qualidade.
2.  **Lógica de Qualidade:**
    * **Aprovada** se:
        * Peso: entre 95g e 105g.
        * Cor: Azul ou Verde.
        * Comprimento: entre 10cm e 20cm.
    * **Reprovada** se falhar em qualquer critério. O motivo da reprovação é registrado.
3.  **Gerenciamento de Caixas:** Peças Aprovadas são adicionadas a uma caixa atual, com capacidade máxima de **10 peças**. Ao atingir o limite, a caixa é fechada e uma nova é iniciada.
4.  **Relatórios:** O sistema consolida o total de peças aprovadas, reprovadas e o uso de caixas, detalhando os motivos de falha.

## 🚀 Como Rodar o Programa (Passo a Passo)

Para executar o sistema, você precisará ter o Python instalado (versão 3.6+).

### 1. Preparação

Crie uma pasta para o projeto e salve os dois arquivos com os nomes abaixo:

| Arquivo | Conteúdo |
| :--- | :--- |
| `controle_qualidade.py` | Classes e lógica de negócio. |
| `main.py` | Menu interativo e loop principal. |

### 2. Execução

Abra o terminal (Prompt de Comando, PowerShell ou Terminal) e navegue até a pasta onde você salvou os arquivos.

Execute o arquivo principal com o seguinte comando:

```bash
python main.py