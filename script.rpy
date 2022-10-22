# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
define money = 7000
label start:
    $ spent_money = renpy.input("Сколько потратить денег?", length=4, allow="0123456789").strip() or "0"
    $ spent_money = int(spent_money)
    if spent_money > money:
        $ spent_money = money
    if spent_money == 0:
        "Вы не потратили ни копейки."
    elif spent_money == money:
        "Вы потратили все деньги."
    else:
        "Вы потратили [spent_money]."
    $ money = money - spent_money
    "У игрока осталось [money] монет."