class Car:

    name = 'c200'
    make = 'mercedez'
    model = 2008
    car_count = 0
    
    def start(self, name, make, model):
        print('Двигатель заведен')
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

    def stop(self):
        print('Отключаем двигатель')

car_a = Car()
car_a.start('Corrola', 'Toyota', 2015)
print(car_a.name)
print(car_a.car_count)

car_b = Car()
car_b.start('City', 'Honda', 2013)
print(car_b.name)
print(car_b.car_count)