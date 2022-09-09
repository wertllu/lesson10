from game import game_help, game_get_random, game_get_result

print(game_help())


print( game_get_random())
print( game_get_random())
print( game_get_random())

print(game_get_result('камінь', 'ножиці'))
print(game_get_result('камінь', 'камінь'))
print(game_get_result('ножиці', 'камінь'))


user_option = 'камінь'
print(f'Ви обрали {user_option}')
ai_option = game_get_random()
print(f'Я обрала {ai_option}')
print(game_get_result(user_option, ai_option))

