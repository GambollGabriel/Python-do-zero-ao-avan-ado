n1 = n2 = n3 = True #podemos aribuir o mesmo valor para varias variaveis e uma unica linha.
print(type(n1))     #podemos descobrir qual é o tipo da variavel.

nome, idade, sim = 'Socram', 16, True #Podemos fazer isso tbm.

print(type(nome))
print(type(idade))
print(type(sim))
print(type(2*4j))  # Fica no tipo Complexo, aparentmente só acita a letra "j".

# Função isinstance()
a = 10
b = 'Sol'
print(isinstance(a, (int, float))) # isistance, ira pegar a variavel 'a' e ira verificar se ela é do tipo que você passou na frente.
