#exeção é um objeto que representa um erro que ocorreu ao executar o programa.
# Bloco try ... except
# try --> tentar [Colocar o bloco que pode estar dando erro]
#except --> exeção [Colocar o tratamento, captura desse erro]
# else --> Código que irá mostrar caso não ocorra nenhum erro. 
#Finally --> Sempre irá mostrar no fim caso ocorra um erro ou não. 
#O python já capturam algum tipos de erros para você ver.


def div(k, j):
    return round(k / j, 2)

while True:
    try:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
        break
    except ValueError:
        print("O correu um erro ao ler o valor. Tente novamente")
    
try:
    r = div(n1, n2)
except ZeroDivisionError:  #Exeção pontual 
    print("Não é possivel dividir por zero!")
except: 
    print("Ocorreu um erro descohecido!")
else:
    print(f"Resultado {r}")
finally:            
    print("Fim")