# PQA Automações: Controle de Produção e Qualidade

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

## 💡 Arquitetura e Boas Práticas de Programação

O projeto utiliza a **Programação Orientada a Objetos (POO)** e o princípio de **Modularização** para garantir um código escalável, manutenível e com responsabilidades bem definidas.

* **Modularização (Separação de Responsabilidades):**
    * `main.py`: Focado na **Interface de Usuário** (Menu Interativo e tratamento de entradas).
    * `controle_qualidade.py`: Focado na **Lógica de Negócio** (Classes, regras de validação e fluxo de empacotamento).
* **Classes Definidas:**
    * **`Peca`:** Modelagem da entidade fundamental do projeto.
    * **`ControleQualidade`:** Atua como o sistema de automação central, responsável por todas as regras e coleções de dados.
* **Robustez:** Uso de **tratamento de exceções (`try-except`)** para lidar com dados de entrada incorretos (não numéricos) e validação de **ID Duplicado**.

## 🚀 Como Rodar o Programa (Passo a Passo)

Para executar o sistema, você precisará ter o Python instalado (versão 3.6+).

### 1. Preparação

Crie uma pasta para o projeto e salve os dois arquivos com os nomes abaixo:

| Arquivo | Conteúdo |
| :--- | :--- |
| `controle_qualidade.py` | Classes e lógica de negócio. |
| `main.py` | Menu interativo e loop principal. |

## 🚀 Como Rodar o Programa (Passo a Passo)

Para executar o sistema, você precisará ter o **Python** instalado (versão 3.6+).

### 1. Preparação

Certifique-se de que os dois arquivos principais (`main.py` e `controle_qualidade.py`) estejam salvos no mesmo diretório.

### 2. Execução

Abra o terminal (Prompt de Comando, PowerShell ou Terminal) e navegue até a pasta do projeto.

Execute o arquivo principal com o seguinte comando:

```bash
python main.py
```

### 📋 Menu Interativo e Exemplos de Saída

O menu interativo permite que o usuário gerencie o fluxo de produção, com todas as opções totalmente funcionais:

| Opção | Funcionalidade |
| :--- | :--- |
| **1** | Cadastrar nova peça (Inspecionar) |
| **2** | Listar peças aprovadas/reprovadas |
| **3** | Remover peça cadastrada |
| **4** | Listar caixas fechadas |
| **5** | Gerar Relatório Final |
| **0** | Sair |

### Exemplo de Entradas e Status

Abaixo, exemplos de entradas e como o sistema as classifica com base nos critérios de qualidade:

| ID | Peso (g) | Cor | Comprimento (cm) | Status | Motivo de Reprovação (Console) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `001` | `100.0` | `azul` | `15.0` | APROVADA | - |
| `002` | `98.0` | `verde` | `12.0` | APROVADA | - |
| `003` | `102.0` | `azul` | `18.0` | APROVADA | - |
| `004` | `96.5` | `verde` | `10.5` | APROVADA | - |
| `005` | `104.0` | `azul` | `19.0` | APROVADA | - |
| `006` | `99.5` | `verde` | `15.5` | APROVADA | - |
| `007` | `100.0` | `azul` | `14.5` | APROVADA | - |
| `008` | `97.0` | `verde` | `16.0` | APROVADA | - |
| `009` | `101.5` | `azul` | `11.0` | APROVADA | - |
| `010` | `105.0` | `verde` | `20.0` | **APROVADA** | - (Fecha a Caixa 1) |
| `011` | `95.0` | `azul` | `10.0` | **APROVADA** | - (Inicia a Caixa 2) |
| `012` | `100.0` | `amarelo` | `15.0` | REPROVADA | FALHA NA COR |
| `013` | `90.0` | `azul` | `15.0` | REPROVADA | FALHA NO PESO |
| `014` | `100.0` | `verde` | `25.0` | REPROVADA | FALHA NO COMPRIMENTO |

### Exemplo de Saída do Relatório Final (Opção 5)

Este é um exemplo da saída consolidada no console (opção 5), após cadastrar as 14 peças acima:

```
##################################################
 RELATÓRIO CONSOLIDADO DE PRODUÇÃO E QUALIDADE 
##################################################

[ GERAL ]
Total de Peças Inspecionadas: 14
Total de Peças Aprovadas: 11
Total de Peças Reprovadas: 3

[ CAIXAS ]
Capacidade por Caixa: 10 peças
Quantidade de Caixas Fechadas: 1 
Peças na Caixa Atual: 1 
Total de Caixas Utilizadas (Fechadas + Atual): 2

[ MOTIVOS DE REPROVAÇÃO ]
Ocorrências de Reprovação (motivos múltiplos são contados separadamente):
- Cor (Amarelo) não é Azul ou Verde: 1 ocorrências
- Peso (90.0g) fora da faixa (95g-105g): 1 ocorrências
- Comp. (25.0cm) fora da faixa (10cm-20cm): 1 ocorrências
##################################################

```