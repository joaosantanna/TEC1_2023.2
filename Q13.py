m = 'jan,fev,mar,apr,may,jun,jul,aug,sep,oct,nov,dez'
m = m.split(',')
d = dict()
for k,v in enumerate(m):
    d[k+1] = v
mes = int(input('Informe o mes que vc quer pesquisar:'))
if mes in d.keys():
    print(f'o mes correspondente ao valor {mes} = {d[mes]}')
else:
    print('Valor de mes é invalido ')

