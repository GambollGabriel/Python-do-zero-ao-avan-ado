# Funções --> Bloco de códigos que ira ser execultado quando for chamado. 
# Modularização, Reúso de Código, Legibilidade.
# def --> to define --> definir 
"""
def <nome_função> ([argumento]):  
    <instruções>
"""

"""
def mensagem(): # Criou a Função
    print('Marcos Gabriel Dias Fernandes') #Conteudo da função 
    print('administrador e programador.') #Conteudo da função 

mensagem() #Chamou a função 


#Função com argumentos
def soma(a, b):
    print(a+b)

soma(22, 9)

#--------------------------------------------

def mul(x, y):
    return x * y #Se a função return for executada o função para 

a = 9
b = 9
c = mul(a,b)
print(f" produto de {a} e {b} é igual a {c}")

#--------------------------------------------

def div(q,w):
    if w == 0:
        return "Não é possivel dividir por 0"
    else:
        return q/w

a = float(input("Informe o dividendo: "))
b = float(input("Informe o divisor: "))
c = div(a,b)
print(f"O resultado da divisão de {a} e {b} é igual a {int(c)}")

#--------------------------------------------

def quadrado(val):
    quadrado = []
    for x in val:
        quadrado.append(x ** 2)
    return quadrado

valores = [1,3,5,7,10,239]
resultados = quadrado(valores)
for g in resultados:
    print(g)
"""


#Funções parâmetros
 
def contar(caractere, num=11):
    for i in range(num):
        print(caractere)
 
contar('#', 8)  

z = 5
x = 6
y = 8

def soma_mult(a, b, c = 0):
    if c == 0:
        return a * b
    else:
        return a + b 

res = soma_mult(z, x, y)
print(res)
