
msg = 'Curso de Python '
nome = 'Marcos Gabriel'
print(msg + nome) #Concatenação de strings 
letra = nome[7] #Você pega a posição da letra dentro da string 
print(letra)
print(len(nome)) #Pega a quantidade de letra dentro da string
frase = 'Vamos aprender python Hoje!'
palavras = frase.split() #Tranforma os elementos da string em um lista, cada palavra vira um elemento. 
print(palavras[1]) #Podemos pegar o elemento da lista 

for palavra in palavras:
    print(palavra)

nome = 'Marcos Gabriel'
print(nome[0:6]) #Da para pegar a quantidade de letras que você deseja. 

email = input('Coloque o seu email: ')
arroba = email.find('@')
print(arroba)
usuario = email[0:arroba]
dominio = email[arroba+1:]
print(usuario)
print(dominio)


produtos = 'macarrão e frango'
print('macarrão' in produtos) #Verifica se a estring macarrão está na string produtos 
print('pizza' not in produtos) #Verifica se a string pizza não esta na string produtos 


item = 'hipoclorito'
pos = item.find('clor')
print(pos)
pos = item.find('flu')
print(pos) 


#Maiusculos e minusculos 

objeto_celeste = 'Galáxia esPirau M31'
print(objeto_celeste.upper()) #Deixa tudo em letra MAIUSCULA (upper = superior).
print(objeto_celeste.lower()) #Deixa tudo em letra minuscula (lower = mais baixo)
print(objeto_celeste.capitalize()) #Deixa a primeira letra da frase em MAIUSCULA e o resto não. 
print(objeto_celeste.title()) #Deixa a primeira letra de cada palavra em MAIUSCULA. 


suplemento = 'Cloreto de magnésio'
n_suplemento = suplemento.replace('magnésio', 'zinco')#(replace = substituir) você coloca a palavra que quer substituir e a palavra que é para substituir ela ou sejá, vai ficar cloreto de zinco em vez de cloreto de magnésio. 
print(suplemento)
print(n_suplemento)



#Remover espaços 

frase = '    ômega 3 é bom para a saude   '
print(frase)
print(frase.lstrip()) #(left = esquerda) --> tira os espaços da esquerda 
print(frase.rstrip()) #(right = direita) --> tira os espaços da direita
print(frase.strip())  #tira os espaços da direita e da esquerda 


#Alinhamento de texto para exibição

Fruta = 'Laranja'
print(Fruta)
print(Fruta.rjust(30)) #Da 30 espaços e justifica a direita
print(Fruta.center(30)) #Da 30 espaços e justifica no centro de 30
print(Fruta.ljust(30)) #Da 30 espaços e justifica a esquerda
print(Fruta.center(30, "-")) #Centraliza na medida que você passou e no resto coloca o que você mandou "-"

#Prefixo e Sufixo

p = 'Bóson Treinamentos'
print(p.startswith('Bó')) # Dentro da variavel 'p' começa com BÓ? 
print(p.endswith('Bó')) # Dentro da variavel 'p' termina com BÓ? 

# Docstrings -> strings para documentar  é o famoso 
texto = """
Docstrings -> Em resulmo é o coentario de varias linhas do python, ela respeita a identação e é multilinhas 
    Marcos
"""

print(texto)
