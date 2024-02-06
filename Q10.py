frase = input('Digite uma frase:')
contador = 0
vogais = 'aeiouAEIOU'
for letra in frase:
    if letra in vogais:
        contador += 1
print(f'A frase digitada tem {contador} vogais')