import random
from unittest import result

def game_help():
    return 'гра "камінь, ножиці, папір", зробіть свій вибір\n1 - камінь, 2 - ножиці, 3 - папір: '


def game_play(i):

    # print('гра "камінь, ножиці, папір", зробіть свій вибір')
    # print('гра "камінь, ножиці, папір", зробіть свій вибір')
    # i = input('1 - камінь, 2 - ножиці, 3 - папір: ')
    # i = '3'
        
    result=''

    if i == '1':
        result += 'ви обрали камінь'

    elif i == '2':
        result += 'ви обрали ножиці'

    elif i == '3':
        result += 'ви обрали папір'

    else:
        result += 'вийшла якась помилка'


    f = random.randint(1,3)
    # print(f)

    if f == 1:
        result += '\nя обрала камінь'

    elif f == 2:
        result += '\nя обрала ножиці'

    elif f == 3:
        result += '\nя обрала папір'

    else:
        result += '\nвийшла якась помилка'

    a = int(i)

    if f == a:
        result += '\nнічия!'
    elif (a == 2 and f == 1 ) or ( a == 3 and f == 2 ) or (a == 1 and f == 3):
        result += '\nя виграла!'
    else:
        result += '\nви виграли!'
            

    return result
            