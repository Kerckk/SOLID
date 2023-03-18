#не правильный вид кода, так как я пытаюсь просмотреть
# список объектов Car, тем самым я нарушаю принцип
# подстановки Лисков, поскольку я не могу
# заменить объекты супертипа Car объектами
# подтипа PetrolCar внутри
# функции поиска красных автомобилей.
class Car():
  def __init__(self, type):
    self.type = type

class PetrolCar(Car):
  def __init__(self, type):
    self.type = type

car = Car("SUV")
car.properties = {"Color": "Red", "Gear": "Auto", "Capacity": 6}

petrol_car = PetrolCar("Sedan")
petrol_car.properties = ("Blue", "Manual", 4)

cars = [car, petrol_car]

def find_red_cars(cars):
  red_cars = 0
  for car in cars:
    if car.properties['Color'] == "Red":
      red_cars += 1
  #print(f'Number of Red Cars = {red_cars}')

#find_red_cars(cars)



#Правильный вид кода
class Car():
    def __init__(self, type):
        self.type = type
        self.car_properties = {}

    def set_properties(self, color, gear, capacity):
        self.car_properties = {"Color": color, "Gear": gear, "Capacity": capacity}

    def get_properties(self):
        return self.car_properties


class PetrolCar(Car):
    def __init__(self, type):
        self.type = type
        self.car_properties = {}


car = Car("SUV")
car.set_properties("Red", "Auto", 6)

petrol_car = PetrolCar("Sedan")
petrol_car.set_properties("Blue", "Manual", 4)

cars = [car, petrol_car]


def find_red_cars(cars):
    red_cars = 0
    for car in cars:
        if car.get_properties()['Color'] == "Red":
            red_cars += 1
    print(f'Number of Red Cars = {red_cars}')


find_red_cars(cars)