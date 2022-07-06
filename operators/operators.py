# Операторы сравнения
# Условные операторы
# Логические операторы

# Операторы сравнения:
# <, >, ==(равно), <=, >=, !=(не равно)

# num1 = 18
# num2 = 15
# stroka1 = 'Hello'
# print(ord('H'))
# stroka2 = 'World'
# print(ord('W'))
# result = stroka1 > stroka2
# print(result)
# print(chr(1080))

# bool -- True(1) or False(0)

# Условные операторы
# if 
# elif
# else


# if <condition>:
#     если в if приходит True
#     <body if>
# elif <condition>:
#     <body>
# else:
#     <body>

# string = input('Enter smt: ')

# if string == 'Hello':
#     print('Hello stranger!')
# elif string == 'Mercedes':
#     print('Mercedez-Benz S class')
# else:
#     print('Совпадений не найдено')

# print('Код закончился')


# sign up
# email = input('Enter email: ')
# password1 = input('Enter password: ')
# password2 = input('Enter password confirmation: ')

# if password1 != password2: 
#     raise Exception('Passwords didn\'t match!!!')
# else: 
#     print('Successfully signed Up!')

# age = input('Enter your age: ')
# # print(type(age))
# if age.isdigit():
#     age = int(age)
# else:
#     print('Введите корректные данные!!')
#     raise Exception('Value error!')

# if age < 18:
#     print(f'Chuvak prihodi cherez {18-age} goda/let!')
# else:
#     print('Vy podhodite po vozrastu!')


# Логические операторы
# 1. and -> логическое и
# 2. or -> лог или
# 3. not -> лог отрицание

# my_age = 20
# your_age = 18
# result = (my_age == 20) and (your_age == 18)
# print(result)

# result = my_age < 18 or your_age == 18
# print(result)

# result = not my_age > 25
# print(result)


# is_user_google_user = True
# is_user_github_user = True
# is_user_age_greater_21 = False
# user_accounts_coins = 8000

# if (is_user_google_user and is_user_github_user) and (is_user_age_greater_21 or user_accounts_coins > 5000):
#     print('You can enter the system Mr John Snow')
# else:
#     print('Sorry, you couldnt enter!!')


