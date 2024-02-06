largura = float(input("informe a largura da piscina:"))
comprimento = float(input("Informe o comprimento da piscina:"))
profundidade  = float(input("Informe a profundidade da piscina:"))


volume = largura * comprimento * profundidade
print(f'Volume da piscina = {volume:.2f} m cubicos')

tempo = volume/20
print(f'tempo pra se afogar : {tempo:.2f} minutos')