#Set --> Coleções não ordenadas com valores unico que sã usadas para armazenar multiplos itens dentro de um objto. Ele é mutavel porém não podemos editar os itens, não podms colocar valores duplicados tabmém. Os elementos aparecem fora de ordem tbm

planeta_anao = {'Plautão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(len(planeta_anao)) #Mostra a quantidade de itens
print('Ceres' in planeta_anao) #Da para ver se o item está no set
print('Ceres' not in planeta_anao) #Da para ver se o item não está no set

# for astro in planeta_anao:
#     print(astro.upper(), end=" ")

# astros = ['Lua', 'Marte', 'Vênus', 'Sirius', 'Lua'] 
# print(astros, end=" ")
# astros_set = set(astros) # Transforma a lista em um set
# print(astros_set)
 
astros1 = {'Lua', 'Marte', 'Vênus', 'Sirius', 'Lua', 'Io'}
astros2 = {'Lua', 'Marte', 'Vênus', 'Sirius', 'Lua', 'Cometa de Halley'}
print(astros1 | astros2) #União dos dois set
print(astros1.union(astros2)) #Outra forma de fazer uma união entre os dois set 

print(astros1 & astros2) #Faz uma intersecção dos dois set, pegando só oquee les tem em comun
print(astros1.intersection(astros2)) #Outra forma de fazer intersecção

print(astros1 ^ astros2) #Pega o elementos que não são pegos em ambos os conjuntos
print(astros1.symmetric_difference(astros2)) #Outra forma de pegar os elementos que não são pegos em ambos os conjuntos

#Adcionar e excluir elementos a um conjunto 

astros1.add('Urano')
astros2.add('Sol')# Adciona um elemento ao set 
astros1.remove('Io')# Remove um elemento do set
astros1.discard('Io')# Outra forma de remover um elmento do set
astros1.pop()# Retira de forma aleatria o elemento do set. 
astros1.clear()# Limpa todo o meu set 
print(astros1)
print(astros2)
