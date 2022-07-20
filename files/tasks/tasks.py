# 1. У нас есть файл file.txt c тестом на латинице. Нужно написать программу, которая будет выводить статистику по тексту:

#     > количество букв латинского алфавита
#     > число слов
#     > число строк

# with open('file.txt') as file:
#     text = file.read()
#     # print(text)
#     letters = sum(map(str.isalpha, text))
#     # print(letters)
#     letters2 = len(list((filter(str.isalpha, text))))
#     # print(letters2)
#     # words = text.count(' ') + text.count('.')
#     # print(words)
#     words = len(text.split())
#     # print(words)
#     lines = text.count('\n') + 1
#     # print(lines)
#     file.seek(0)
#     lines2 = len(file.readlines())
#     # print(lines2)
#     print(f'Input file contains:')
#     print(f'{letters} - letters!')
#     print(f'{words} - words!')
#     print(f'{lines} - lines!')


"""Напишите программу, которая получает на вход строку с названием текстового файла, и выводит на экран содержимое этого файла, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
"""

# Input: "Hello, world! Python IS the programming language of thE future. My EMAIL is....
# PYTHON is awesome!!!!"

# Output: *****, ***ld! ****** ** *** programming language of *** future. My ***** **....
# ****** ** awesome!!!!

with open('forbidden_words.txt') as forbiden_file, open('input.txt') as text_file:
    forbidden_words = forbiden_file.read().split()
    text = text_file.read()
    text_lower = text.lower()
    # print(forbidden_words)
    # print(text)
    for word in forbidden_words:
        text_lower = text_lower.replace(word, '*' * len(word))
    # print(text)
    # print(text_lower)
    # x = 'L'
    # print(('a', 'b')[x == '*'])
    result = [(y, x)[x == '*'] for x, y in zip(text_lower, text)]
    # print(list(zip(text_lower, text)))
    # print(''.join(result))

with open('result.txt', 'w') as file:
    file.write(''.join(result))

1
  11
  11
  1

  1
  

