# POO = programação orientada a objetos: Paradigma de Programação
# Classes e objetos 

class Veiculos:  #O nome da classe tem que ter letra maiuscula 
    def movimentar(self):
        print(f'Sou um veículo e me desloco!')
    
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante  #Encapsulamento -> __fabricante
        self.__modelo = modelo
        self.__num_registro = None 

    #Setter
    def set_num_registro(self, registro):
        self.__num_registro = registro

    #Getter
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante {self.__fabricante}.\n')

    def get_num_registro(self):
        return self.__num_registro

#Herança

class Carro(Veiculos):
    #metodo __init__ será herdado
    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas!')

class Motocicleta(Veiculos):
    def movimentar(self):
        print(f'Corro muito!')

if __name__=='__main__':
    meu_veiculo = Veiculos('GM', 'Vadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro('234242-1')
    print(f'Registro: {meu_veiculo.get_num_registro()}\n')
   #print(meu_veiculo.fabricante) 

    meu_carro = Carro('volkswagen', 'Polo') 
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()

    seu_carro = Carro('Audi', 'A5 Sportback')
    seu_carro.movimentar()
    seu_carro.get_fabr_modelo()

    moto = Motocicleta('Harley-Davidson', 'Nightster Special')
    moto.movimentar()
    moto.get_fabr_modelo()