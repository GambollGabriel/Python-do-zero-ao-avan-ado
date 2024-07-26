# Funções builtin (Internas)

valores = [2,5,8,-3,20,912]
print(max(valores))
print(min(valores))
a = 2
b = 3
print(abs(a))#Valor absoluto, a distancia do número de 0 
print(pow(a, b))#pow é a exponenciação, o expoente nesse exeplo é o 'b' 
pi = 3.14159265358979323846
print(round(pi, 2))#Ele coloca um limite de casas depois do ponto, nesse exemplo ira mostrar 3.14. Se você colocar 1 casa decimal ele arredondara o valor, nesse exemplo mostrara 3,1.


import math

x = 8
y = 100

raiz_quadrada = math.sqrt(x)
print(round(raiz_quadrada, 2))#Arredonda o número (round=arredodo)
print(math.ceil(raiz_quadrada)) #Arredonda o valor para cima (ceil = teto)
print(math.floor(raiz_quadrada)) #Arredonda o valor para baixo (floor = chão)



logaritimo = math.log10(y) #Logaritimo é o número ao qual eu irei elevar o valor para chegar a outro valor
print(logaritimo)

print(math.pi) # Pega o número de pi
print(math.factorial(y)) #Pega  fatorial 
print(x / math.inf) #numero infiito (Não sei usar ;-;, ainda...)
