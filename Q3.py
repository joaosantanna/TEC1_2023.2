'''
esse programa recebe duas variaveis de entrada e troca seus
valores , eu sei é facil mas eles não sabiam fazer

'''
x = int(input("Enter a X: "))
y = int(input("Enter a Y:"))
#primeira versao usando o tradicional troca em 3 etapas
# tmp = x
# x = y
# y = tmp

x,y = y,x

print(f' x = {x}')
print(f' y = {y}')
