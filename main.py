import sys
from controle_qualidade import ControleQualidade, Peca

# Inicializa o sistema de controle
controle = ControleQualidade()

def exibir_menu():
    """Exibe o menu de opções."""
    print("\n" + "="*40)
    print(" SISTEMA DE CONTROLE DE PRODUÇÃO E QUALIDADE ")
    print("="*40)
    print("1. Cadastrar nova peça (Inspecionar)")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar Relatório Final")
    print("0. Sair")
    print("="*40)

def cadastrar_peca():
    """Opção 1: Coleta dados e inspeciona a peça."""
    print("\n--- Cadastro de Nova Peça ---")
    try:
        peca_id = input("ID da Peça: ").strip()
        if not peca_id:
            raise ValueError("O ID da peça não pode ser vazio.")
        if peca_id in controle.pecas_inspecionadas:
            print(f"ERRO: A peça com ID '{peca_id}' já foi inspecionada. IDs devem ser únicos.")
            return

        peso = float(input("Peso (g, ex: 100.5): "))
        cor = input("Cor (Azul ou Verde): ").strip()
        comprimento = float(input("Comprimento (cm, ex: 15.0): "))
        
        if peso <= 0 or comprimento <= 0:
             raise ValueError("Peso e Comprimento devem ser valores positivos.")

        nova_peca = Peca(peca_id, peso, cor, comprimento)
        controle.inspecionar_peca(nova_peca)
        
        print("-" * 30)
        print(f"PEÇA CADASTRADA/INSPECIONADA:")
        print(nova_peca)
        print("-" * 30)

    except ValueError as e:
        print(f"\nERRO de entrada: {e}. Certifique-se de que os valores numéricos e o ID foram inseridos corretamente.")
    except Exception as e:
        print(f"\nERRO inesperado ao cadastrar: {e}")

def listar_pecas():
    """Opção 2: Lista peças aprovadas e reprovadas."""
    print("\n--- Peças Aprovadas ---")
    if controle.pecas_aprovadas:
        for peca in controle.pecas_aprovadas:
            print(f"- {peca}")
    else:
        print("Nenhuma peça aprovada até o momento.")

    print("\n--- Peças Reprovadas ---")
    if controle.pecas_reprovadas:
        for peca in controle.pecas_reprovadas:
            print(f"- {peca}")
    else:
        print("Nenhuma peça reprovada até o momento.")

def remover_peca():
    """Opção 3: Remove uma peça pelo ID."""
    print("\n--- Remoção de Peça ---")
    peca_id = input("Digite o ID da peça a ser removida: ").strip()
    
    if controle.remover_peca(peca_id):
        print(f"\nSUCESSO: Peça com ID '{peca_id}' removida do sistema.")
    else:
        print(f"\nERRO: Peça com ID '{peca_id}' não encontrada no sistema.")

def listar_caixas():
    """Opção 4: Lista o conteúdo das caixas fechadas e da caixa atual."""
    
    print("\n--- Caixas Fechadas ---")
    if controle.caixas_fechadas:
        for i, caixa in enumerate(controle.caixas_fechadas):
            print(f"\nCAIXA {i+1} (Fechada, {len(caixa)}/{controle.CAPACIDADE_CAIXA} peças):")
            for peca in caixa:
                print(f"  > ID: {peca.id} | Peso: {peca.peso}g")
    else:
        print("Nenhuma caixa foi fechada ainda.")

    print("\n--- Caixa Atual em Andamento ---")
    if controle.caixa_atual:
        print(f"CAIXA ATUAL (Aberta, {len(controle.caixa_atual)}/{controle.CAPACIDADE_CAIXA} peças):")
        for peca in controle.caixa_atual:
            print(f"  > ID: {peca.id} | Peso: {peca.peso}g")
    else:
        print("A caixa atual está vazia (aguardando aprovação de peças ou acabou de ser fechada).")

def gerar_relatorio_final():
    """Opção 5: Gera e exibe o relatório consolidado."""
    relatorio = controle.gerar_relatorio()

    print("\n" + "#"*50)
    print(" RELATÓRIO CONSOLIDADO DE PRODUÇÃO E QUALIDADE ")
    print("#"*50)
    
    print(f"\n[ GERAL ]")
    print(f"Total de Peças Inspecionadas: {len(controle.pecas_inspecionadas)}")
    print(f"Total de Peças Aprovadas: {relatorio['total_aprovadas']}")
    print(f"Total de Peças Reprovadas: {relatorio['total_reprovadas']}")
    
    print(f"\n[ CAIXAS ]")
    print(f"Quantidade de Caixas Fechadas: {len(controle.caixas_fechadas)}")
    print(f"Peças na Caixa Atual: {relatorio['pecas_na_caixa_atual']}/{controle.CAPACIDADE_CAIXA}")
    print(f"Total de Caixas Utilizadas (Fechadas + Atual): {relatorio['quantidade_caixas_utilizadas']}")

    print(f"\n[ MOTIVOS DE REPROVAÇÃO ]")
    if relatorio['motivos_reprovacao']:
        for motivo, quantidade in relatorio['motivos_reprovacao'].items():
            print(f"- {motivo}: {quantidade} peças")
    else:
        print("Nenhuma peça reprovada (todos os critérios atendidos).")
    
    print("#"*50)


# --- Loop Principal do Programa ---

def main():
    """Função principal que executa o menu interativo."""
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            cadastrar_peca()
        elif escolha == '2':
            listar_pecas()
        elif escolha == '3':
            remover_peca()
        elif escolha == '4':
            listar_caixas()
        elif escolha == '5':
            generar_relatorio_final()
        elif escolha == '0':
            print("\nSaindo do sistema. Relatório final gerado na opção 5.")
            sys.exit()
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()