# class Car:

#     @staticmethod
#     def get_class_details():
#         print('Это класс Car')


#     name = 'c200'
#     make = 'mercedez'
#     model = 2008
#     car_count = 0
    
#     def start(self, name, make, model):
#         print('Двигатель заведен')
#         self.name = name
#         self.make = make
#         self.model = model
#         Car.car_count += 1

#     def stop(self):
#         print('Отключаем двигатель')

# car_a = Car()
# car_a.start('Corrola', 'Toyota', 2015)
# print(car_a.name)
# print(car_a.car_count)

# car_b = Car()
# car_b.start('City', 'Honda', 2013)
# print(car_b.name)
# print(car_b.car_count)


# Car.get_class_details()


# class Square:

#     @staticmethod
#     def get_squares(a, b):
#         return a * a, b * b

# print(Square.get_squares(3, 5))


# class Car:

#     car_count = 0

#     def __str__(self) -> str:
#         return "Car class object"
    
#     def start(self):
#         print('Двигатель заведен')

#     def __init__(self) -> None:
#         Car.car_count += 1
#         print((Car.car_count))

# car_a = Car()
# car_b = Car()
# car_c = Car()
# print(car_a)


# class Car:
#     message1 = 'Dvigatel zaveden'

#     def start(self):
#         message2 = "Avtomobil zaveden"
#         return message2

# car_a = Car()
# print(car_a.message1)


# class Car:
#     def __init__(self):
#         print("Dvigatel zaveden")
#         self.name = "corolla"
#         self.__make = "toyota"
#         self._model = 1999

# car_a = Car()
# print(car_a.name)
# print(car_a.make)


# class Vehicle:
#     def vehicle_method(self):
#         print("Is a parent method of class Vehicle")

# class Car(Vehicle):
#     def car_method(self):
#         print("Is a method of dotch class")

# class Cycle(Vehicle):
#     def cycleMethod(self):
#         print("Is a dotch method of class Cycle")

# car_a = Car()
# car_a.vehicle_method()
# car_b = Cycle()
# car_b.vehicle_method()


# class Camera:
#     def camera_method(self):
#         print("Is aa parent method of class Camera")

# class Radio:
#     def radio_method(self):
#         print("Is a parent method of class Radio")

# class CellPhone(Camera, Radio):
#     def cell_phone_method(self):
#         print("Is a dotch method of class CellPhone")

# cell_phone_a = CellPhone()
# cell_phone_a.camera_method()
# cell_phone_a.radio_method()


# class Car:
#     def start(self, a, b=None):
#         if b is not None:
#             print(a + b)
#         else:
#             print(a)

# car_a = Car()
# car_a .start(10, 20)


# class Vehicle:
#     def vehicle_method(self):
#         print("Is a parent method of class Vehicle")

# class Car(Vehicle):
#     def vehicle_method(self):
#         print("Is a method of dotch class Car")

# class Cycle(Vehicle):
#     def vehicle_method(self):
#         print("Is a dotch method of class Cycle")


# car_a = Vehicle()
# car_a.vehicle_method()

# car_b = Car()
# car_b.vehicle_method()

# car_c = Cycle()
# car_c.vehicle_method()


class Car:

    def __init__(self, model):
        self.model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def getCarModel(self):
        return "Year born model " + str(self.model)

carA = Car(2088)
print(carA.getCarModel())


car_a = Car(2088)
print(car_a.getCarModel())