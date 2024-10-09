class Car:
  count = 0

  def __init__(self, color, make, year) -> None:
    self.color = color
    self.make = make
    self.year = year
    Car.count += 1


  def display_car_info(self):
    print(f"This is a {self.year} {self.make} with a {self.color} color.")


  @classmethod
  def number_of_cars(cls):
    return cls.count

# car objects
car1 = Car("Red","Toyota",2020)
car2 = Car("Blue", "Ford", 2018)
car3 = Car("Black", "Tesla", 2022)

# display info using methods
car1.display_car_info()
car2.display_car_info()
car3.display_car_info()

print(Car.number_of_cars())