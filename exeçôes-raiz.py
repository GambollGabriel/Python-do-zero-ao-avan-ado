from math import sqrt

class NumeroNegativoError(Exception): # Define uma nova classe de exceção personalizada chamada 'NumeroNegativoError'.
    def __init__(self):
        pass

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente.
    try:
        num = int(input("Digite um número possitivo"))
        if num < 0:
            raise NumeroNegativoError  # Se o número for negativo, levanta a exceção personalizada 'NumeroNegativoError'.
    except NumeroNegativoError: # Captura a exceção 'NumeroNegativoError' se ela for levantada.
        print(f"Foi fornecido ukm número negativo")
    else:
        print(f"A raiz quadrada de {num} é {sqrt(num)}")
    finally:
        print(f"Fim do cálculo.")
