# def <name_of_function>(<a, b> #параметры):
#     <body> #некий код, некая логика
#     <return #возвращаем что-то>

# <name_of_function>(<5, 6> #аргументы)

# Параметры функции - переменные которые будет принимат наша функция, для того что-бы мы смогли работать с данными которые передаются в эту функцию

# Аргументы - данные которые мы передае для параметров при вызове функции

# return нужен для того что-бы фукнция что то возвращала и для того что-бы мы могли рабоатть с рузельтатом действия функции, return является необязательным оператором(возвращает None - если не указать return)

# ls = []
# result = ls.append(1)
# print(ls)
# print('Результат действия:',result)

# result1 = ls.pop()
# print(ls)
# print('Результат действия:',result1)


# def sumTwoNums(num1, num2): #параметры
#     result = num1 + num2
#     # print(result)
#     return result

# print(sumTwoNums(5,5)) #аргументы

# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# a = 10
# b = int(input('Enter num: '))

# print(isEven(5))
# print(isEven(a))
# print(isEven(b))


# def isEven1(num: int) -> bool:
#     """
#     Наша функция проверяет является ли число, типа int, четным.
#     """
#     if num % 2 == 0:
#         return True
#     return False

# isEven()
# isEven1()
# dir()

# Anna, Ded, Kabak, Kazak, Walaw, ono,
# from typing import List

# def get_polindrom(words: List[str]) -> List[str]:
#     '''Функция возвращает список из полиндромов'''
#     result = []
#     for word in words:
#         if word.lower()==word[::-1].lower():
#             result.append(word)
#     return result

# some_words = ['John', 'Ono', 'kazak', 'peter', 'anna', 'Dovod', 'apa', 'Juice', 'piko', 'tenet']
# print(get_polindrom(some_words))
# get_polindrom()


# def func():
#     print('Hello world!')

# func()

# ----------------------------------
# default params

# def print_welcome(name:str='User') -> str:
#     print(f'Welcome, {name}!')

# print_welcome()

# '''Напишите функцию которая будет возвращать ваш депозит через определнное время с процентом 10%, возращать финальное количество денег. Мин период вложения 3 года. Мин ставка денек 30 000 сомов'''

# def get_percentage(money: float, period: int) -> float:
#     '''Return final amount of money!'''
#     if money < 30000:
#         raise Exception('вы ввели некоректное количесво денег, мин ставка 30000 сомов!')
#     if period < 3:
#         raise Exception('вы ввели некоректный срок для депозита, мин период вложения 3 года!')
#     i = 0
#     while i < period:
#         money = money + (money * 0.1)
#         # money * 1.1 
#         # money + (money / 100 * 10)
#         i += 1 # i = i + 1
#     return money

# money = float(input('Vvedite summu deneg: '))
# year = int(input('Vvedite srok vawego depozita: '))
# print(get_percentage(money, year))

# 'Hello world! My name is John, last name is Snow. Nice to meet you!

# you! meet to Nice Snow. is name

# hello john snow
# snow john hello

def get_reverse_string(text: str) -> str:
    '''return reversed string*'''
    print(text)
    spisok = text.split(' ')
    print(spisok[::-1])
    result = " ".join(spisok[::-1])
    print(result)
    return result

get_reverse_string('Hello world! My name is John, last name is Snow. Nice to meet you!')




