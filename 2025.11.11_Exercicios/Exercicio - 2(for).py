# --- Implementação Principal: Loop de Repetição ---

# O 'while True' cria um loop infinito. O código dentro dele
# continuará rodando até que a condição de saída (o 'break') seja atingida.
while True:
    
    # --- Coleta de Dados ---
    try:
        # Solicita um número ao usuário e o armazena.
        numero = int(input('\nDigite um número: '))
    except ValueError:
        # Garante que o usuário digitou um número válido.
        print("Entrada inválida. Por favor, digite um número inteiro.")
        continue # Volta para o início do loop
        
    # --- Variável de Controle (Contador) ---
    linha = 1  # Inicializa o contador para a primeira parte (Subida)

    # --- Parte 1: Subida (Enquanto 'linha' for menor ou igual a 5) ---
    while linha <= 5:
        # Imprime o número repetido 'linha' vezes
        print(str(numero) * linha)
        
        # Incrementa o contador
        linha = linha + 1

    # --- Parte 2: Descida (de 4 até 1) ---
    # Ajusta o contador para começar do 4
    linha = 4

    # O loop roda enquanto a linha for maior ou igual a 1
    while linha >= 1:
        # Imprime o número repetido 'linha' vezes
        print(str(numero) * linha)
        
        # Decrementa o contador
        linha = linha - 1
        
    # --- Opção de Recomeçar/Finalizar ---
    
    # Pede ao usuário que decida o que fazer em seguida
    repetir = input('\nDeseja rodar novamente? (s/n): ').lower()
    
    # Verifica a resposta:
    if repetir == 'n':
        # Se a resposta for 'n', a instrução 'break' encerra o loop 'while True'.
        print("Programa finalizado. Até mais! 👋")
        break 
    elif repetir == 's':
        # Se a resposta for 's', o código volta para o início do loop 'while True'.
        print("Reiniciando o programa...")
        continue # O 'continue' é opcional aqui, mas garante o retorno ao topo.
    else:
        # Trata respostas inválidas.
        print("Opção inválida. Reiniciando por padrão.")
        continue