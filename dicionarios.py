# Dicionarios 

elemento = {
    'Z': 3, 
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(elemento['Z']) #Pega o elemento da lista
print(elemento['nome']) #Pega o elemento da lista
print(f'O dicionario tem {len(elemento)} elementos') #Pega o número de elemento dentro do dicionario

#Atualizar uma entrada
elemento['grupo'] = 'Alcalinos' #modificar o elemento da biblioteca 
print(elemento)

#Adicionar uma entrada
elemento['periodo'] = 1 #Será criada porquê não existe na biblioteca
print(elemento)

# Exclussão de itens em dicionarios 

del elemento['periodo'] #removi o periodo 
print(elemento)

# elemento.clear() #Apagar todo conteudo do dicionario, mas não apaga o dicionario 
# print(elemento)

# del elemento #apaga o dicionario, ele deixa de existir 
# print(elemento)

print(elemento.items()) #Ira mostrar o dicionario como Tuplas 

for i in elemento.items():
    print(i)

print(elemento.keys()) #Pega a chave dos elementos do dicionarios
for i in elemento.keys():
    print(i)

print(elemento.values()) #Mostra os elementos do dicionario 
for i in elemento.values():
    print(i)

for i, j in elemento.items():
    print(f"{i}: {j}")
    