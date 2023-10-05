def exit_function():
    #функция "приставака-выходилка"
    yesno = input('Введите Y, если хотите выйти, или N, если хотите продолжить: ')
    if yesno == 'Y':
        return True
    elif yesno == 'N':
        return False
    else:
        return exit_function()


def check_filling(check_field):
    for i in range(3):
        if '-' in check_field[i]:
            return True
    print('Ходы закончились')
    return False



#Заполнение полей: игрового - прочерками, полей игроков - нулями
field = [["-"] * 3 for i in range(3)]
x_field = [[0] * 3 for i in range(3)]
o_field = [[0] * 3 for i in range(3)]

#Словарь с координатами массива в зависимости от выбранной цифры
coordinates = {
    7: (0, 0), 8: (0, 1), 9: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    1: (2, 0), 2: (2, 1), 3: (2, 2)}

#победные комбинации
wins = [[[1, 1, 1],
         [0, 0, 0],
         [0, 0, 0]],
        [[0, 0, 0],
         [1, 1, 1],
         [0, 0, 0]],
        [[0, 0, 0],
         [0, 0, 0],
         [1, 1, 1]],
        [[1, 0, 0],
         [1, 0, 0],
         [1, 0, 0]],
        [[0, 1, 0],
         [0, 1, 0],
         [0, 1, 0]],
        [[0, 0, 1],
         [0, 0, 1],
         [0, 0, 1]],
        [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]],
        [[0, 0, 1],
         [0, 1, 0],
         [1, 0, 0]]]


def win_check(check_field):
    #функция проверки на выигрышную комбинацию
    Res = [[], [], []]
    for i in range(len(wins)):
        for j in range(len(check_field)):
            #Res[j] = list(map(lambda x,y: x*y, check_field[j], wins[i][j]))
            Res[j] = [x*y for x, y in zip(check_field[j], wins[i][j])]
        if Res == wins[i]:
            return True
    return False


#Напечатаем пустое поле
for row in field:
    print(' '.join(row))

#Приветствие
print('Давай сыграем в игру!\nИспользуй для выбора квадрата цифровую клавиатуру')

gamer = 'X' #первый всегда ходит Х

while check_filling(field):
    #выбор квадратика - ввод с клавиатуры
    num = int(input(f'Сделай свой ход, мистер {gamer}: '))

    #если квадрат пустой - заполняем его, иначе передаём ход, нефиг ошибаться
    if 1 <= num <= 9:
        square = coordinates[num]
        if (field[square[0]][square[1]] == '-'):
            field[square[0]][square[1]] = gamer
            if gamer == 'X':
                x_field[square[0]][square[1]] = 1
            else:
                o_field[square[0]][square[1]] = 1
        else:
            print('Плохой выбор( Переход хода')
    else:
        print('Очень плохой выбор')
        if exit_function():
            print('Ну и иди!')
            break
        else:
            print('Отлично, продолжаем!')

    #печать поля
    for row in field:
        print(' '.join(row))

    if win_check(x_field) or win_check(o_field):
        print(f'Игрок {gamer} победил! Поздравляю!')
        break

    #смена игрока
    gamer = 'O' if gamer == 'X' else 'X'

print('Игра окончена! Спасибо!')



