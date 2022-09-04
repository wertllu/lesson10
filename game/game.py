import random


print('гра "камінь, ножиці, папір", зробіть свій вибір')
i = input('1 - камінь, 2 - ножиці, 3 - папір: ')
# i = '3'

if i == '1':
    print('ви обрали камінь')

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
        print('я обрала камінь')

    elif f == 2:
        print('я обрала ножиці')

    elif f == 3:
        print('я обрала папір')

    else:
        print('вийшла якась помилка')

    a = int(i)

    if f == a:
        print('нічия!')
    elif (a == 2 and f == 1 ) or ( a == 3 and f == 2 ) or (a == 1 and f == 3):
        print('я виграла')
    else:
        print('ви виграли')
        