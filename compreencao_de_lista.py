numeros = [1,3,4,6, 10, 14, 16]

#em vez de ->
#quadrado = list(map(lambda num: num**2, numeros)) #Faça...
# quadrado = [num**2 for num in numeros]
# print(quadrado)

#Crie uma lista de números pares de 0 a 10

# pares = [num for num in range(11) if num %2 == 0]
# print(pares)

# frase = 'A lógica é apenas o principio da sabedoria, e não o seu fim.'
# vogais = ['a','e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
# lista_vogais = [v for v in frase  if v in vogais]
# print(f'A frase possui {len(lista_vogais)} vogais:')
# print(lista_vogais)


#Distributivas entre valores de duas listas
distributivas = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributivas) 