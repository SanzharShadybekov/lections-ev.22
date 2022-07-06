# """
# 1. Сгенерируйте рандомный пароль который будет следовать следующим требованиям: пароль должен содержать 2 символа верхнего регистра, одно число и один спец.символ. Подсказка: Используйте библиотеки random и string.
# """
# import random
# import string

# letter1 = random.choice(string.ascii_uppercase)
# letter2 = random.choice(string.ascii_uppercase)
# number = random.randint(1,10)
# simbol = random.choice(string.punctuation)

# password = [letter1, letter2, str(number), simbol]
# random.shuffle(password)
# password = ''.join(password)

# print(password)
# print(type(password))

# --------------------------------
# Counting Valleys Haccerrank
# 12 steps
# path -> 'DDUUDDUDUUUD' -> 2 valleys
def countingValleys(steps, path):
    dolina = 0
    sea_level = 0 
    for x in path:
        if x == 'U':
            sea_level += 1
            if sea_level == 0:
                dolina += 1
        elif x == 'D':
            sea_level -= 1
    return dolina

print(countingValleys(100, 'DUDUUUUUUUUDUDDUUDUUDDDUUDDDDDUUDUUUUDDDUUUUUUUDDUDUDUUUDDDDUUDDDUDDDDUUDDUDDUUUDUUUDUUDUDUDDDDDDDDD'))
