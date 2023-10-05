def exit_function():
    #функция "приставака-выходилка"
    yesno = input('Введите Y, если хотите выйти, или N, если хотите продолжить: ')
    if yesno == 'Y':
        return True
    elif yesno == 'N':
        return False
    else:
        return exit_function()


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

#Напечатаем пустое поле
for row in field:
    print(' '.join(row))

#Приветствие
print('Давай сыграем в игру!\nИспользуй для выбора квадрата цифровую клавиатуру')

gamer = 'X' #первый всегда ходит Х

while True:
    #выбор квадратика - ввод с клавиатуры
    square = coordinates[int(input(f'Сделай свой ход, мистер {gamer}: '))]

    #если квадрат пустой - заполняем его, иначе передаём ход, нефиг ошибаться
    if field[square[0]][square[1]] == '-':
        field[square[0]][square[1]] = gamer
        if gamer == 'X':
            x_field[square[0]][square[1]] = 1
        else:
            o_field[square[0]][square[1]] = 1
    else:
        print('Плохой выбор( Переход хода')

    #печать поля
    for row in field:
        print(' '.join(row))
    for row in x_field:
        print(' '.join(map(str,row)))
    for row in o_field:
        print(' '.join(map(str,row)))

    #смена игрока
    gamer = 'O' if gamer == 'X' else 'X'

    if exit_function():
        break



