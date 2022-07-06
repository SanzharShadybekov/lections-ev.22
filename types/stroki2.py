# Методы строк

# dir() - Фунцкия которая вытаскивает методы типов данных

# print(dir(str))

# '<соединитель>'.join(<массив который нужно соединить>) - Соединяет массив из строк по соединителю в одну строку.
# ls = ['Milk', 'Bread', 'Water', 'Apple', '5']
# joined = '###'.join(ls)
# print(joined)

# split(разделитель) -> Дробит строку по разделителю и возвращает тип данных list.
# text = 'Milk.Bread.Water.Apple'
# splited = text.split('a')
# print(splited)
# joined = ', '.join(splited)
# print(joined)


# replace(<old value>, <new value>, [count]) -> Меняет в строке значение old na new value, если вы укажете count, то он заменит count раз.

# text = 'ha ha ha ha ha'
# result = text.replace('ha', 'La')
# print(result)
# print(text)


# strip() -Убирает пробельные символы в начале и в конце строки.

# rstrip() - В конце удаляет
# lstrip() - В начале удаляет

# text = input('Введите ФИО: ')
# result = text.lstrip()
# print(text.strip())
# print(result)
# print(text)


# count('<simbol>') -> считает количество вхождений <simbol> в строку

# text = 'Hello world! I\'m from Earth!'
# result = text.count('_')
# print(result)

# index('<value>', [start], [end]) -> выводит индекс значения value в нашей строке.

text = 'Hello world! This is Makers!'
result = text.index('is')
print(result)
print(len(text))
print(text.find('T'))




