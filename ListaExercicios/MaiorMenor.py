def numbers(numero1, numero2, numero3):
    maior = numero1

    if numero2 > maior:
        maior = numero2
    elif numero3 > maior:
        maior = numero3

    return maior

print(numbers(98, 1, 2))