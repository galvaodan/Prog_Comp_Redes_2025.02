
while True:
 try:

    umero = int(input('Digite um número: '))

    except ValueError:
        # Garante que o usuário digitou um número válido.
    print("Entrada inválida. Por favor, digite um número inteiro.")
    continue # Volta para o início do loop

for linha in range (1,6):
    print(str(numero) * linha) 
for linha in range(4, 0, -1):
    print(str(numero) * linha)

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