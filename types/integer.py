# Тип даных int()

# asdfkjhas -> так выглядят комментрии

number = 5 # -> переменная

# +
# a = 10
# b = 5
# result = a + b
# print(result) # -> функция для станадартного вывода

# 5 / 2 = 2.5 -> float()
# 5 // 2 = 2 -> целочисленное деление
# a = 5
# b = 2
# result = a // b
# print(result)

# * -> умножение

# % -> деление при котором мы получаем остаток
# a = 2
# b = 1
# result = a % b
# print(result)


# ** -> возведение в степень
# 5 ** 4 -> 625
# 2 ** 2 -> 4
# a = 5
# b = 2
# result = a ** b
# print(result)

# round() -> округляет число с плавающей точкой до ближайщего целого числа
# 5.49 -> round(5.49) -> 5

# a = 5.49
# result = round(a)
# print(result)

# pow(a, b) -> возводит число 'a' в степень 'b' -> pow(5, 2) -> 25

# a = 10
# b = 2
# result = pow(a, b)
# print(result)


# divmod(a, b) -> Она выводит два числа, первое число это результат целочисленного деления(//) 'a' на 'b'. А второе число модуль(%) при делении 'a' на 'b'.
# a = divmod(5, 2)
# print(a)

# abs() -> выводит абсолютное значение числа -> abs(-5) -> 5, abs(5) -> 5, |-5| -> 5
# a = abs(-10)
# print(a)

# import math

# a = 5
# result = math.sqrt(a)
# print(result)

# input() -> запрашивает что то ввести

# a = input("Enter something: ")
# print(a)

# множественное присваивание
# a = 3, b = 1, c = 2
a = 1
b = 2
c = 3
a, b, c = c, a, b
print(a)
print(b)
print(c)