def verificar_palindromo():
    palavra = input("Digite uma palavra: ").upper().strip()

    palavra_invertida = palavra[::-1]

    if palavra == palavra_invertida:
        print(f"A palavra '{palavra}' é um palíndromo!")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.")

verificar_palindromo()