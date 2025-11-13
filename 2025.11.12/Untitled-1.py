'''
   Exemplo 01: Programa para contar quantas vogais existem em uma string 
   fornecida pelo usuário.
'''

str_Palavra = input("Digite uma palavra: ")


contador_Vogais = 0


vogais = "aeiouAEIOUáàãéèêíìîóòõúùû"

for letra in str_Palavra:
    
    if letra in vogais:
        contador_vogais += 1 

# Exibe o resultado
print(f"A palavra '{str_Palavra}' tem {contador_vogais} vogais.")