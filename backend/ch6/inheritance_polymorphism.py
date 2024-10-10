class Vehicle:
  def __init__(self, name, max_speed):
    self.name = name
    self.max_speed = max_speed


  def display_info(self):
    print(f"This vehicle is a {self.name}, with a maximum speed of {self.max_speed} km/h.")


class Car(Vehicle):
  def __init__(self, name, max_speed, mileage):
    super().__init__(name, max_speed)
    self.mileage = mileage


  def display_car_info(self):
    print(f"The car {self.name} runs at a maximum speed of {self.max_speed} km/h and has a mileage of {self.mileage} mpg.")

#
# MRO in python
#
class A:
  pass
class B(A):
  pass
class C(A):
  pass
class D(B, C):
  pass
print(D.mro())  


#
# Method Overriding -> polymorphism
# design patterns, such as the Template Method and Strategy patterns, which rely heavily on overriding methods 
# in subclasses.
#
class Animal:
  def speak(self):
    return "This animal does not have a specific sound."


class Dog(Animal):
  def speak(self):
    return "Woof!"


class Cat(Animal):
  def speak(self):
    return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
  print(animal.speak())


#
# multiple inheritance
#

class Base1:
  pass


class Base2:
  pass


class Derived(Base1, Base2):
  pass

print(Derived.mro())



#
# Duck typing in polymorphism
#

class Duck:
  def quack(self):
    return "Quack quack!"
  

class Person:
  def quack(self):
    return "I am pretending to be a duck!"
  

def make_it_quack(ducky):
  print(ducky.quack())


duck = Duck()
person = Person()

make_it_quack(duck)
make_it_quack(person)