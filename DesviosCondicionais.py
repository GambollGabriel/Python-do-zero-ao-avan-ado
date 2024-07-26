#if; elif; else

nota = 0.0

nota = float(input("Qual é a sua nota?"))

if(nota >= 8):
    print("Aprovado")
elif(nota >= 5):
    print("Recuperação")
else:
    print("Reprovado")
