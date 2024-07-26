# Lista: representa uma sequência de valores. 

#Sentaxe: nome_lista = [Valores]

n1 = [2,4,6,8,10]
n2 = [1,3,5,7,9,11]
lista = n1+n2 #União de listas, não estou somando
lista[2] = 3 # Vai pegar o valor da posição 2 (que é 6) e mudar para 3 
print(lista)
print(lista[-1]) #-1 pega o ultimo valor da lista, -2 pega o penultimo valo da lista, assim sucessivamente.
print(lista[2:10]) # Fala que vai imprimir apartir da posição 2 até a posição 10. Também podemos fazer "-2:", dessa forma pegara os dois ultimos valores da lista.


#---Funções---

print(len(lista)) # Imprime a quantidade de elementos que tem na lista. 
print(sorted(lista)) # Imprime os valores em ordem crescente 
print(sorted(lista, reverse=True)) # Imprime os valores em ordem decrescente 
print(sum(lista)) # Soma os valores da lista 
print(min(lista)) # Encontra o valor minimo da lista 
print(max(lista)) # Encontra o valor maximo da lista 



#metodos para manipular os dados da lista 

lista.append(13) # Acresenta um valor na lista, esse valor acresentado vai ser o ultimo a imprimir 
print(lista)
lista.pop() # Tira o último elemento da lista 
print(lista)
lista.pop(5) # Tira o elemento 5° elemento da lista
print(lista)
lista. insert(5, 19) # Coloca o valor 19 na pisição 5 
print(lista)
print(12 in lista) #É uma pergunta "12 em lista?" Quer saber se o valor 12 está na lista



#Laços de repetção junto com listas

planetas = ['Mercurio', 'Vênus', 'Marte', 'Terra', 'Urano', 'Netuno']

for planeta in planetas:
    print(planeta)



#EXERCÍCIO

lista_bebidas = []

for bebida in range(5):
    pergunta = input('Qual é a sua bebida favoritas?')
    lista_bebidas.append(pergunta)
ordem = sorted(lista_bebidas)
for imprimir in ordem:
    print(imprimir)
