# As Tuplas são imutáveis 

hologenios = ('F', 'Cl', 'Br', 'I', 'At')
Gases_Nobres = ('He', 'Ne', 'Ar' , 'Xe', 'Kr', 'Rn')

lista_hologenios = list(hologenios)
lista_Gases_Nobres = list(Gases_Nobres)
print(type(lista_Gases_Nobres))
print(type(lista_hologenios))

tupla_hologenios = tuple(lista_hologenios)
tupla_Gases_Nobres = tuple(lista_Gases_Nobres)
print(type(tupla_Gases_Nobres))
print(type(tupla_hologenios))
