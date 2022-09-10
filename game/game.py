import random

all_options = ['камінь', 'ножиці', 'папір']

def game_help():
    return 'гра "камінь, ножиці, папір", зробіть свій вибір'

def game_get_random():
    f = random.randint(0,2)
    return all_options[f]

def game_get_result(u, ai):
    if game_option_index(u) == -1:
        return 'перевірте чи правильно вписали свій вибір або виберіть його у меню'

    a = game_option_index(u) + 1
    f = game_option_index(ai) + 1

    if f == a:
        return 'нічия!'
    elif (a == 2 and f == 1 ) or ( a == 3 and f == 2 ) or (a == 1 and f == 3):
        return 'я виграла!'
    else:
        return 'ви виграли!'


def game_option_index(u: str):
    for i in range(0,3):
        if u.find(all_options[i]) != -1: #
            return i
    return -1