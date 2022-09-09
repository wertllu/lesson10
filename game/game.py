import random

all_options = ['камінь', 'ножиці', 'папір']

def game_help():
    return 'гра "камінь, ножиці, папір", зробіть свій вибір'

def game_get_random():
    f = random.randint(0,2)
    return all_options[f]

def game_get_result(u, ai):
    if u not in all_options:
        return 'перевірте чи правильно вписали свій вибір або виберіть його у меню'

    a = all_options.index(u) + 1
    f = all_options.index(ai) + 1

    if f == a:
        return 'нічия!'
    elif (a == 2 and f == 1 ) or ( a == 3 and f == 2 ) or (a == 1 and f == 3):
        return 'я виграла!'
    else:
        return 'ви виграли!'