#Крестики-нолики на терминале на базе одномерного массива (списка)
#Kirill Mikheev PDEV-41 2023

def exit_function():
    #функция "приставака-выходилка"
    yesno = input('Желаете выйти? (Y/N): ')
    if yesno == 'Y':
        print('Ну и иди!')
        return True
    elif yesno == 'N':
        print('Отлично, продолжаем!')
        return False
    else:
        return exit_function()


def check_filling(check_field):
    if '-' in check_field:
        return True
    print('Ходы закончились')
    return False


#Заполнение полей: игрового - прочерками, полей игроков - нулями
field = ["-"] * 9
x_field = [0] * 9
o_field = [0] * 9

#победные комбинации
wins = [[1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0]]

def win_check(check_field):
    #функция проверки на выигрышную комбинацию
    res = []
    for i in range(len(wins)):
        res = [x*y for x, y in zip(check_field, wins[i])]
        if res == wins[i]:
            return True
    return False


#Напечатаем пустое поле
for n in range(6, -1, -3):
    print(' '.join(field[n:n+3]))

#Приветствие
print('Давай сыграем в игру!\nИспользуй для выбора квадрата цифровую клавиатуру')

gamer = 'X' #первый всегда ходит Х

while check_filling(field):
    #выбор ячейки - ввод с клавиатуры
    num = int(input(f'Сделай свой ход, мистер {gamer}: ')) - 1

    #если ячейка пустая - заполняем его, иначе просим повторить
    if 0 <= num <= 8:
        if (field[num] == '-'):
            field[num] = gamer
            if gamer == 'X':
                x_field[num] = 1
            else:
                o_field[num] = 1

            # печать поля
            for n in range(6, -1, -3):
                print(' '.join(field[n:n + 3]))

            #Если собралась выигрышная комбинация, то заканчиваем и выходим
            if win_check(x_field) or win_check(o_field):
                print(f'Игрок {gamer} победил! Поздравляю!')
                break
            #А если прошли этот шаг, то меняем игрока
            gamer = 'O' if gamer == 'X' else 'X'
        else:
            #Если ячейка занята
            print('Ячейка уже занята. Выберете другую: ')
    else:
        #Если игрок не попал по цифровой клавиатуре, то спросим, не хочет ли он выйти
        print('Мимо!')
        if exit_function():
            break

#Выход из цикла - конец игры
print('Игра окончена! Спасибо!')



