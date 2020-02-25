"""

Изначально у игрока и у компьютера есть карта
Затем игрок набирает карты, пока не скажет "Стоп"
После набирает компьютер до 17 очков.

"""

import random

name_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dama', 'korol', 'tyz']
name_mast = ['chervi', 'bybi', 'kresti', 'piki']

coloda = []

for num_1, val_1 in enumerate(name_cards):
    for num_2, val_2 in enumerate(name_mast):
        t = (val_1,val_2)
        coloda.append(t)


def point(t, sum):
    if t[0] == '2':
        return 2
    elif t[0] == '3':
        return 3
    elif t[0] == '4':
        return 4
    elif t[0] == '5':
        return 5
    elif t[0] == '6':
        return 6
    elif t[0] == '7':
        return 7
    elif t[0] == '8':
        return int(8)
    elif t[0] == '9':
        return 9
    elif t[0] == '10' or t[0] == 'valet' or t[0] == 'dama' or t[0] == 'korol':
        return 10
    elif t[0] == 'tyz':
        if sum >= 21:
            return 1
        else:
            return 11

def give_card_for_player(mas,sum):
    new_card = random.choice(coloda)
    mas.append(new_card)
    del coloda[coloda.index(new_card)]
    sum += point(new_card, sum)
    return sum, new_card


def run():
    print("The game was started")
    Tr = True
    sum_2 = 0
    sum_1 = 0
    one_card = []
    two_card = []
    tup = give_card_for_player(one_card,sum_1)
    sum_1 = tup[0]
    print("Карта игрока",tup[1])
    sum_2 = give_card_for_player(two_card,sum_2)[0]
    while (Tr == True):
        print("Сумма у игрока", sum_1)
        print("Введите 1 чтобы получить еще одну карту, 0 - если Вам больше не надо")
        a = int(input())
        if a == 1:
            tup_1 = give_card_for_player(one_card,sum_1)
            sum_1 = tup_1[0]
            print("Карта игрока", tup_1[1])
        else:
            print("Сумма игрока", sum_1)
            sum_2 = give_card_for_player(two_card, sum_2)[0]
            while sum_2 <=17:
                sum_2 = give_card_for_player(two_card, sum_2)[0]
            print("Сумма компьютера", sum_2)
            print("Игра окончена")
            if sum_1 > 21:
                if sum_2 > 21:
                    print("Победивших нет")
                elif sum_2 <=21:
                    print("Выиграл компьютер")
            elif sum_1 < 21:
                if sum_1 > sum_2 or sum_2 > 21:
                    print("Выиграл игрок")
                elif sum_2 > sum_1:
                    print("Выиграл компьютер")
                elif sum_1 == sum_2:
                    print("Победивших нет")
            elif sum_1 == 21:
                print("Выиграл игрок")
                if sum_2 == 21:
                    print("Проигравших нет")
            elif sum_2 == 21:
                print("Выиграл компьютер!")
            Tr = False

run()

