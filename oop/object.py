names = ['Lloyd']
# names é uma INSTANCIA de classe list
print(type(names))

# um TOYOTA é uma instancia da classe carro

class Car:
    # tudo dentro desse bloco serão coisas que pertencem à classe Car
    color = 'black' # atributos de cor, marca e modelo
    make = 'toyota'
    model = 'corolla'

print(Car.model)

# instanciando um objeto da classe Car

car1 = Car()
car2 = Car()
car1.color = 'pink'
print(car1.color)
print(car2.color)