# -----Função lambda (anônima)--------
# Sixtaze:
# Lambda argumentos: expressão

# quadrado = lambda x: x**2

# for  i in range(1, 11):
#     print(quadrado(i))

# par = lambda x: x%2 ==0 
# print(par(8))

# f_c = lambda f: (f - 32) * 5/9
# print(f_c(32))





#-----Função map()-----
#sintaxe
# map(função, iterável)

# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x*2, num))
# print(dobro)

# palavra = ["Python", "é", "uma", "linguagem", "de", "programação"]
# maiusculas = list(map(str.upper, palavra))
# print(maiusculas)




#----Função filter()----
# Sintaxe:
# filter (função, sequência)

# def numeros_pares(n):
#     return n % 2 == 0

# numeros = [1,2,3,4,5,6,7,8,9,]

# num_par = list(filter(numeros_pares, numeros))

# print(num_par)


# numeros = [1,2,3,4,5,6,7,8,9,]
# num_impar = list(filter(lambda x: x%2 != 0, numeros))
# print(num_impar)



# ----Função reduce()----
# sintaxe
#reduce(função, sequência, valor_inicial)

# from functools import reduce  #Chamar a função

# def mult(x,y):
#     return x*y

# numeros = [1,2,3,4,5,6]
# total = reduce(mult, numeros)
# print(total) 

#Soma cumulativa dos quadrados de valores, usando expressão lambda

from functools import reduce

# ((2² + 2²)² + 3²)² + 4²

numeros = [1,2,3,4]
total = reduce(lambda x,y: x** 2 + y**2, numeros)
print(total)
