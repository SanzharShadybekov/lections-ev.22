# Абстракция(Абстрактный класс) - его можно рассматривать как набор методов, которые должны быть созданы в любых дочерних классах, построенных на основе абстрактного класса(если наследуемся). 

# Абсрактный метод - это метод, у которого есть объявление, но нет реализации.

# from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):
#     def __init__(self, name) -> None:
#         self.name = name
    
#     @abstractmethod
#     def area(self): pass

#     def fact(self):
#         print('Я некая фигура в двумерной плоскости!')

# class Square(Shape):
#     def __init__(self, lenght) -> None:
#         super().__init__('Квадрат')
#         self.lenght = lenght
    
#     def area(self):
#         print(self.lenght ** 2)

#     def fact(self):
#         super().fact()
#         print('У меня все углы равны 90 градусам!')

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Окружность')
#         self.radius = radius

#     def area(self):
#         print(pi * (self.radius ** 2))


# a = Square(8)
# b = Circle(6)
# print(a.name)
# print(b.name)
# a.fact()
# b.fact()
# a.area()
# b.area()


# len() - полиморфная функция
# print(len('Makers'))
# print(len([1,2,3,4,5]))

# + - полиморфный оператор

# print(5 + 5)
# print('Hello ' + 'world!')

# Полиморфизм - суть использования заключается в том чтобы использовать единственную сущность(метод, функция, оператор) для представления различных типов, результатов в различных сценариях.

# *
# 5 * 5 # 25
# 'str' * 5 

# class Cat:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age 
    
#     def info(self):
#         print(f'Я кошка! Меня зовут {self.name} и мне {self.age}!')

#     def sound(self):
#         print('Мьяяууу!')


# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f'Я собака! Меня зовут {self.name} и мне {self.age}!')

#     def sound(self):
#         print('Гав гав!')

# cat = Cat('Garfild', 5)
# dog = Dog('Pluto', 9)

# for animal in (cat, dog):
#     animal.info()
#     animal.sound()

# ----------------------------------------
# Class methods, instance methods, static metods

# Методы экземпляра класса(Instance methods) - это те методы в ООП которые могут изменять состояние жкземпляра класса: def method(self)

# Методы класса(Class methods) - Это те методы которые могут изменять состояние самого класса или манипулировать самим классом:
# @classmethod - это декторатор который обозночает что метод будет являтся методом класса.
# def method(cls) - cls - это ссылка на сам класс

# Статические методы(Static methods) - это те методы которые не могут изменять состояние как экземпляра от класса так и состояние самого класса:
# @staticmethod - это декторатор который обозночает статический метод
# def method():

# class Person:
#     surname = 'Stark'

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birht_date(cls, name, year):
#         print(cls, '!!!!!!')
#         from datetime import date
#         cls.surname = 'Lanister'
#         age = date.today().year - year
#         return cls(name, age)

#     @staticmethod
#     def is_adult(age):
#         if age >= 18:
#             print('Person is adult!')
#         else:
#             print('Not adult!')


# john = Person('John', 24)
# print(john.name, john.surname)
# john.is_adult(john.age)
# Person.is_adult(john.age)

# jamie = Person.from_birht_date('Jamie', 1988)
# print(jamie.name, jamie.surname)
# print(jamie.age)
# Person.is_adult(jamie.age)








