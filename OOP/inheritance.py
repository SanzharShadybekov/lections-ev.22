# Принципы в ООП:
# 1. Наследование
# 2. Инкапсуляция
# 3. Полиморфизм

# 4. Абстракция
# 5. Композиция
# 6. Агрегация

# Наследование - позволяет принимать родительские методы, атрибуты и поведение

# Родительский класс
# Дочерний класс
# -------------------------------------

# class Animal:
#     def say(self):
#         print('I\'m Animal!')

# class Croco(Animal):
#     pass

# croco = Croco()
# croco.say()

# --------------------------------------

# class Employee:
#     bonus = 1.5
#     def __init__(self, name, last_name, salary):
#         self.name = name
#         self.last_name = last_name
#         self.salary = salary

#     def get_full_name(self):
#         return f'{self.name} {self.last_name}'

#     def give_bonus(self):
#         self.salary = self.salary * self.bonus

# emp1 = Employee('John', 'Snow', 2000)
# print(emp1.get_full_name())
# print(emp1.salary)
# emp1.give_bonus()
# print(emp1.salary)

# ----------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'Меня зовут {self.name}, и мне {self.age} лет.')

# class Student(Person):
#     def __init__(self, name, age, univer):
#         super().__init__(name, age)
#         self.univer = univer

#     def info(self):
#         super().info()
#         print(f'Я учусь в университете {self.univer}')

# mike = Student('Mike', 18, 'AUCA')
# mike.info()
# print(mike.name)

# -------------------------
# class Employee:
#     bonus = 1.5
#     def __init__(self, name, last_name, salary):
#         self.name = name
#         self.last_name = last_name
#         self.salary = salary

#     def get_full_name(self):
#         return f'{self.name} {self.last_name}'

#     def give_bonus(self):
#         self.salary = self.salary * self.bonus

# class Developer(Employee):
#     def __init__(self, name, last_name, salary, prog_lang):
#         super().__init__(name, last_name, salary)
#         self.lang = prog_lang

# class Manager(Employee):
#     def __init__(self, name, last_name, salary, emps=None):
#         super().__init__(name, last_name, salary)
#         if emps == None:
#             self.emps = []
#         else:
#             self.emps = emps

#     def add_emp(self, emp):
#         if emp not in self.emps:
#             self.emps.append(emp)
#         else:
#             print('Employee already is in!')

#     def show_emps(self):
#         result = []
#         for emp in self.emps:
#             result.append(emp.get_full_name())
#         return result

# dev1 = Developer('John', 'Snow', 1500, 'Pyhton')
# dev2 = Developer('Steve', 'Wozniak', 2000, 'JS')
# dev3 = Developer('Lary', 'Page', 1000, 'JS')
# dev4 = Developer('Jamie', 'Lanister', 1500, 'Pyhton')
# manager1 = Manager('Ivan', 'Ivanov', 3000, emps=[dev2, dev3])
# manager2 = Manager('Aibek', 'Velikiy', 1500)

# manager2.add_emp(dev1)
# manager2.add_emp(dev4)
# manager2.add_emp(dev1)

# print(manager1.show_emps())
# print(manager2.show_emps())

# print(f'Manager {manager1.get_full_name()}, has {manager1.show_emps()} developers. His salay is {manager1.salary}')
# manager2.give_bonus()
# print(f'Manager {manager2.get_full_name()}, has {manager2.show_emps()} developers. His salay is {manager2.salary}')

# -----------------------------------

class Post:
    def __init__(self, user) -> None:
        self.user = user
        self. posts = []
        self.id = 0

    #CRUD
    def create_post(self, title, body, image):
        self.id += 1
        post = dict(id=self.id, title=title, body=body, image=image)
        self.posts.append(post)
        return {'status': 201, 'msg': 'successfully created!'}
    
    def retrieve_post(self, post_id):
        for post in self.posts:
            if post.get('id') == post_id:
                return post
        return {'status': 404, 'msg': 'Not found!'}
    
    def update_post(self, post_id, **kwargs):
        for post in self.posts:
            if post.get('id') == post_id:
                post.update(kwargs)
                return {'status': 200, 'msg': 'Updated'}
        return {'status': 404, 'msg': 'Not found!'}

    def delete_post(self, post_id):
        for post in self.posts:
            if post.get('id') == post_id:
                index_post = self.posts.index(post)
                self.posts.pop(index_post)
                return {'status': 204, 'msg': 'No content, deleted!'}
        return {'status': 404, 'msg': 'Not found!'}

acc1 = Post('JohnSnow')
acc2 = Post('JamieLanister')

acc1.create_post('Good News', 'Moya sestra Sansa rodila dochku!!!', 'https://foto.jpg')
acc1.create_post(
    'Na progulke', 'Segodnya otlichnaya pogoda, vywel na progulku!', 'https://foto123.jpg'
)
acc1.create_post(
    'Na chile!', 'Edu otdyhat\' v Egipet!', 'https://foto123.jpg'
)

print(acc1.user)
print(acc1.posts)

print(acc1.retrieve_post(2))
print(acc1.retrieve_post(5))

print(acc1.update_post(2, title='Progulka updated', body='Seginya obnovil progulku!', image='https://image.jpg'))

print(acc1.retrieve_post(2))
print(acc1.delete_post(2))

print(acc1.posts)
print(acc2.user)
print(acc2.posts)

