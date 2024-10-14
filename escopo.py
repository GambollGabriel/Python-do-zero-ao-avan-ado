# Escopo Local e Global 

var_global = "Curso completo de Python"

def escreva_texto():
    global var_global # Fala que a variavel local abaixo é referente a uma variavel global que está fora da função. (IMPORTANTE).
    var_global = "Bancos de dados com SQL" #Quando tem duas variaveis com o mesmo nome, mas uma é dentro da função, ela resebera priridade na variavel printada dentro da função, porém na de fora é oposto, até porque a vaiavel normalmente não pegaria porque é local, (Sim, tem erro de português).
    var_local = "Fábio  dos reis"
    print(f"Variavel Global {var_global}")
    print(f"Variavel Local {var_local}")

print(f"Execultar a função escreve_texto()")
escreva_texto()

print("Testar acessar a variáeis diferentes")
print(f"Variavel Global {var_global}") #É acessivel em qualquer canto 
#print(f"Variavel Local {var_local}") # A variavel local não é acessivel fora da função 
