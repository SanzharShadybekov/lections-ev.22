# Инкапсуляция: 
# 1. Связь данных с методами которые этими данными управляет.
# 2. Набор инструментов для управления доступа к методам и данным.

# Инкапсуляция как связь
# class Phone:
#     number = '+996 707 707 707'

#     def print_number(self):
#         print(f'Мой номер: {self.number}')

# my_phone = Phone()
# my_phone.print_number()

# Инкапсуляция как сокрытые данных
# Уровни доступа в питоне:
# 1. Публичный(public, age)
# 2. Защищенный(protected, _age)
# 3. Приватный(private, __age)

# class Phone:
#     username = 'John' #public
#     _caller = 'Mike' #protected
#     __count_rings = 0 #private

#     def call(self):
#         print(f'Тебе звонит: {self._caller}!')
    
#     def __turn_on(self):
#         self.__count_rings += 1
#         print(f'Вы созванивались {self.__count_rings}')

# phone = Phone()
# phone.call()
# print(phone._caller)
# print(phone._Phone__count_rings)
# phone._Phone__turn_on()

# class Number(Phone):
#     pass

# number = Number()
# print(number.username)
# print(number._caller)

# class Test(Number):
#     pass

# test = Test()
# print(test.username)
# print(test._caller)

# # getter & setter
# Они используются для получения и установки значения, чтобы добавить логигу проверки при получении данных.
# Еще чтобы избежать прямого доступа к защищенному атрибуту класса

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f'Imya: {self.name}\nVozrast: {self.age}!')

# john = Person('John', 23)
# print(john.name)
# print(john.age)
# john.display_info()
# john.age = -18
# john.display_info()



# class Person:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.__age = 0

#     def display_info(self):
#         print(f'Imya: {self.name}\nVozrast: {self.__age}!')
    
#     def set_age(self, age): #setter
#         if 0 < age < 140: self.__age = age
#         else: print('Invalid age')

#     def get_age(self):
#         print(self.__age)

# john = Person('John')
# john.display_info()
# john.set_age(5)
# john.set_age(-18)
# john.set_age(6)
# john.get_age()

# Аннотации свойств
# @property

# class Person:
#     __name = 'John'
#     __age = 25

#     @property
#     def name(self):
#         print(self.__name)
    
#     @name.setter
#     def name(self, name):
#         self.__name = name
    
#     @property
#     def age(self):
#         print(self.__age)
    
#     @age.setter
#     def age(self, age):
#         if 0 < age <140:
#             self.__age = age 
#         else:
#             print('Недопустимый возраст!')

# obj = Person()
# obj.name #obj.get_name()
# obj.name = 'Tom' #obj.set_name('Tom')
# obj.name
# obj.age
# obj.age = 18
# obj.age
# obj.age = 1000
# obj.age = 25
# obj.age


# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня
# заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 %
# заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.
from datetime import datetime, timedelta
from time import sleep

class Phone:
    def __init__(self, imei, os) -> None:
        self._imei = imei
        self._os = os
        self.__battery_level = 100
    
    def get_info(self):
        if self.__battery_level <= 0.5:
            raise Exception('Телефон разряжен')
        
        self.__battery_level -= 0.5
        print(
            f'OS: {self._os}\nIMEI: {self._imei}')
        
    def play_music(self):
        if self.__battery_level <= 5:
            raise Exception('Телефон разряжен')
        self.__battery_level -= 5
        print('Слушаем Atabekova!')
            
    def play_video(self):
        if self.__battery_level <= 10:
            raise Exception('Телефон разряжен')
        self.__battery_level -= 7
        print('Смотрим  Топлес!')

    def charge_battery(self, sec):
        now = datetime.now
        end_time = (now() + timedelta(seconds=sec)).strftime('%M:%S')
        # print(now())
        # print(end_time)
        while now().strftime('%M:%S') != end_time:
            sleep(1)
            if self.__battery_level < 100:
                self.__battery_level += 1
            print(f'Идет зарядка! Ваш уровень батареи: {self.__battery_level}')

phone = Phone(17181920, 'Android')
phone.play_video()
phone.play_video()
phone.play_video()
phone.play_video()
phone.play_video()
phone.play_video()
phone.play_music()
phone.charge_battery(29)