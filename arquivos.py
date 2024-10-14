# Manipulação de arquivos de text; 

manipulador = open('Arquivo.txt', 'r', encoding='utf-8')

print(f'Método read():\n')
print(manipulador.read())


print(f'\nMétodo read():\n')
print(manipulador.readline())
print(manipulador.readline())