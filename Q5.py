# area quadrado
l = float(input("Informe o valor do lado do quadrado: "))
aq = l**2

# area trapezio
b = float(input("Informe o valor da base menor do trapezio:"))
B = float(input("Informe o valor da base maior do trapezio:"))
a = float(input("Informe o valor da altura do trapezio:"))
atrap = (b+B)*a/2

#area do triangulo
b = float(input("Informe o valor da base do triangulo:"))
a = float (input("Informe o valor da altura do triangulo:"))
atri = b*a/2

maior = max(aq,atrap,atri)
menor = min(aq,atrap,atri)

if aq == maior:
    print('Quadrado tem maior area')
if atri == maior:
    print('Triangulo tem maior area')
if atrap == maior:
    print('Trapezio tem maior area')

if aq == menor:
    print('Quadrado tem menor area')
if atri == menor:
    print('Triangulo tem menor area')
if atrap == menor:
    print('Trapezio tem menor area')

print(f'Area quadrado = {aq:.2f}')
print(f'Area trapezio = {atrap:.2f}')
print(f'Area triangulo = {atri:.2f}')
    