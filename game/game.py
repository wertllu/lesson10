import random


print('гра "каміння, ножиці, папір", зробіть свій вибір')
i = input('1 - каміння, 2 - ножиці, 3 - папір: ')
# i = '3'

if i == '1':
    print('ви обрали каміння')

elif i == '2':
    print('ви обрали ножиці')

elif i == '3':
    print('ви обрали папір')

else:
    print('вийшла якась помилка')

for z in range(1):
    f = random.randint(1,3)
    # print(f)

    if f == 1:
        print('я обрала каміння')

    elif f == 2:
        print('я обрала ножиці')

    elif f == 3:
        print('я обрала папір')

    else:
        print('вийшла якась помилка')

    a = int(i)

    if f == a:
        print('нічия!')

    if a == 2 and f == 1:
        print('я виграла')
    if a == 3 and f == 2:
        print('я виграла')
    if a == 1 and f == 3:
        print('я виграла')
    if a == 1 and f == 2:
        print('ви виграли')
    if a == 2 and f == 3:
        print('ви виграли')
    if a == 3 and f == 1:
        print('ви виграли')