import random

ls = ['Plov', 'Manty', 'Kuurdak', 'Lagman', 'Dymdama']
p = 0
m = 0
k = 0
l = 0
d = 0

for i in range(0, 100000):
    choice = random.choice(ls)
    print(choice)
    if choice.lower() == 'plov':
        p = p + 1  #p += 1 инкремент
    elif choice.lower() == 'manty':
        m += 1
    elif choice.lower() == 'kuurdak':
        k += 1
    elif choice.lower() == 'lagman':
        l += 1
    elif choice.lower() == 'dymdama':
        d += 1

# print(f'Plov: {p},\nManty: {m}\nKuurdak: {k},\nLagman: {l}')
dict_ = {'Plov': p, 'Manty': m, 'Kuurdak': k, 'Lagman': l, 'Dymdama': d}
print(dict_.items())
# def func(x: tuple): #('plov', 19550)
#     return x[1]
res = sorted(dict_.items(), key=lambda x:x[1])
winner = res[-1]
print(f'Победило блюдо: {winner[0]}, оно набрало: {winner[1]}')

# # lambda x: x[1]
# def func(x: tuple): #('plov', 19550)
#     return x[1]