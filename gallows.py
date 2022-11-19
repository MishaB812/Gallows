from random import choice


def gallow(error):
    if error == 0:
        print(' ' * 10, ' *********')
        print(' ' * 10, ' *       *')
        print(' ' * 10, ' O       *')
        print(' ' * 10, '         *')
        print(' ' * 10, '         *')
        print(' ' * 10, '         *')
    elif error == 1:
        print(' ' * 10, ' *********')
        print(' ' * 10, ' *       *')
        print(' ' * 10, ' O       *')
        print(' ' * 10, ' |       *')
        print(' ' * 10, '         *')
        print(' ' * 10, '         *')
    elif error == 2:
        print(' ' * 10, ' *********')
        print(' ' * 10, ' *       *')
        print(' ' * 10, ' O       *')
        print(' ' * 10, '/|       *')
        print(' ' * 10, '         *')
        print(' ' * 10, '         *')
    elif error == 3:
        print(' ' * 10, ' *********')
        print(' ' * 10, ' *       *')
        print(' ' * 10, ' O       *')
        print(' ' * 10, '/|\      *')
        print(' ' * 10, '         *')
        print(' ' * 10, '         *')
    elif error == 4:
        print(' ' * 10, ' *********')
        print(' ' * 10, ' *       *')
        print(' ' * 10, ' O       *')
        print(' ' * 10, '/|\      *')
        print(' ' * 10, ' |       *')
        print(' ' * 10, '         *')
    elif error == 5:
        print(' ' * 10, ' *********')
        print(' ' * 10, ' *       *')
        print(' ' * 10, ' O       *')
        print(' ' * 10, '/|\      *')
        print(' ' * 10, ' |       *')
        print(' ' * 10, '/        *')
    elif error == 6:
        print(' ' * 10, ' *********')
        print(' ' * 10, ' *       *')
        print(' ' * 10, ' O       *')
        print(' ' * 10, '/|\      *')
        print(' ' * 10, ' |       *')
        print(' ' * 10, '/ \      *')


word_list = ['авторша', 'варщица', 'данница', 'патруль', 'серость', 'хитрость', 'летчитца', 'поганка', 'артикль',
             'багажник', 'бакалавр', 'бедолага', 'геодезия', 'пергамент', 'каламбур', 'камнепад', 'наездник', 'шиншила',
             'шлепанцы', 'забвение']
while True:
    answer = input('Добро пожаловать в игру "Виселица"\nЖелаешь начать игру?: ')
    if answer.lower() == 'да' or answer.lower() == 'д':
        word = choice(word_list)
        word_prod = set(word)
        errors = 0
        while word_prod:
            user_char = input('Введите букву, чтобы угадать загаданное слово: ')
            print(word)
            if user_char in word_prod:
                print('Вы угадали! Продолжаем дальше...')
                word_prod.remove(user_char)
            else:
                print(f'Этой буквы нет в этом слове .( Осталось {6 - errors} попыток')
                gallow(errors)
                errors += 1
                if errors == 7:
                    print(f'Вы проиграли! Загаданное слово: "{word}"')
                    break
        else:
            print(f'Поздравляем! Вы выиграли! Загаданное слово {word}')
