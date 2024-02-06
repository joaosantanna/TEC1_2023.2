conta = float(input('Digite o valor da conta:'))
gor = int(input('Digite o valor da gorjeta:'))

total_gor = conta * gor/100

total_final = conta + total_gor

print(f'O total da conta = R${total_final:.2f}')
print(f'sendo que desse total, R${total_gor:.2f} é Gorjeta')