# questao alterada para usar o sistema de notas
# da UFRA
nap1 = float(input("Informe a nota do nap 1:"))
nap2 = float(input("Informe a nota do nap 2:"))
subs = float(input("Informe a nota da substitutiva:"))
menor = min(nap1, nap2, subs)
total = nap1 + nap2 + subs - menor
media_final = total/2
print(f"A media final da disciplina = {media_final:.2f}")

if media_final > 6:
    print("Aprovado")
else:
    print("Reprovado")
