def add(*args):
    # print(args)
    total = 0
    for n in args:
        total += n
    return total


sum1 = add(1, 2, 3, 4, 5)
sum2 = add(2, 3, 4, 6, 7, 1, 9, 2, 8, 20)

# print(sum1, sum2)

def calculate(n, **kwargs):
    print(n, kwargs)
    print(n)
    for key, value in kwargs.items():
        print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print("equals", n)

# calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.doors = kw.get("doors")
        self.seats = kw.get("seats")
        self.colour = kw.get("colour")

my_car = Car(colour="grey", make="Chevrolet", model="Orlando", seats=7)
# print(my_car.make, my_car.model, my_car.doors, my_car.seats, my_car.colour)

