import random

"""
cont = 0

#Gerar números inteiros com a função randint

while cont < 5:
    numero_aleatorio = random.randint(0, 20)#Você chama a função "randint" e coloca padrões de onde vai pegar os números aleatórios.  
    print(f"O número aleatório gerado é {numero_aleatorio}")
    cont += 1



#Gerar números Float

valor = random.random() # Irá gerar um número aleatório do tipo Float(quebrado) entre 0 e 1 
print(f"Irá gerar um número aleatório entre 0 e 20 agora pois está * por 20{valor * 20}")

#Round

print(f"O valor é {round(valor*20, 2)}") # Aqui está sendo delimitada quantas casas a variavel "valor" tera, nesse exemplo colocamos 2 casas, só podemos faer isso usando o round. 



valor = random.uniform(1,20) # É tipo o randint só que para números quebrados. 
print(f"O valor aleatório é {round(valor, 3)}")


"""
#Aleatoriedade com listas 

lista = [0,2,8,10,24,34,50,69,72,200]
# n = random.choice(lista) #choice = escolido, ou sejá choice escolhe um número da listá 
# print(n)

# n = random.sample(lista, 3) # mesma coisa do choice, porém sua pecularidade é que ele pode definir quantos elementos serão pegos da lista(a resposta do print vai ser entregue em forma de lista)
# print(n)

#Embaralhar 

print(f" Lista normal ==> \n {lista}")
print("Lista embaralhada abaixo")
n = random.shuffle(lista)#Usamos o metodo shuffle que significa embaralhar. Obs tem que criar uma variavel para esse método.
print(lista)

