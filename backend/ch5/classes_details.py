# static methods -> no impact on class or instance. helper function within class boundary
# class methods -> operate on class as a whole. counter of instances, population, factory methods
# instance methods


# access modifiers -> public, private (__beforeAttributeOrMethod), protected (_beforeAttributeOrMethod)


class Car:
  def __init__(self, make, model) -> None:
    self._make = make
    self._model = model


class ElectricCar(Car):
  def display_info(self):
    print(f"This electric car is a {self._make} {self._model}.") # accessing protected attribute from outside


# instances
my_ecar = ElectricCar("Tesla", "Model S")
my_ecar.display_info()



class Private_Car:
  def __init__(self, make, model) -> None:
    self.__make = make
    self.__model = model


  def __display_info(self):
    print(f"This car is a {self.__make} {self.__model}.")


  def public_method(self):
    self.__display_info() # to access private method from within the class


# instances
my_car = Private_Car("Toyota", "Supra")
my_car.public_method()
# my_car.__display_info()     # this gives attribute error 