""" 
Descriptors offer more flexibility and reusability than
properties. They're the mechanism underlying properties,
functions, and static and class methods. Descriptors are
suitable for creating reusable attribute management logic
that can be applied across multiple attributes or different
classes.

"""


class NonNegative:
  def __init__(self, name):
    self.name = name


  def __get__(self, instance, owner):
    return instance.__dict__[self.name]
  

  def __set__(self, instance, value):
    if value < 0:
      raise ValueError(f"{self.name} cannot be negative")
    instance.__dict__[self.name] = value


  def __delete__(self, instance):
    del instance.__dict__[self.name]


class Circle:
  radius = NonNegative('radius')


  def __init__(self, radius):
    self.radius = radius   # Calls NonNegative.__set__()