class Car:
    def __init__(self, color, make, model): # faz ser obrigatória a inclusão dos itens entre parênteses na instanciação de um objeto
        self.color = color # self faz com que qualquer alteração, nos parâmetros entre parênteses, seja feita para aquela instancia apenas, não para toda a classe
        self.make = make
        self.model = model
        # valores padrão para TODAS as instâncias da classe
        self.gas = 0 
    
def get_gas(self): # adiciona gas para o carro que está sendo referenciado
        self.gas += 10 

def check_gas(self): # veriifica quanto de gas eu tenho naquele carro 
   print(self.gas)

def random_thing():
    print('loook at me')
    

# instancia um objeto da classe Car
#car1 = Car('red', 'honda', 'nsx')
#car2 = Car('gray', 'mazda', 'rx7')
#print(car1.check_gas())
# car1.get_gas()
# print(car1.check_gas())

# print(f'Car1 has a color of {car1.color}, and Car2 has a color of {car2.color}')
