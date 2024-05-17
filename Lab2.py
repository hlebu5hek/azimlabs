'''
Натуральные числа.
Выводит на экран четные числа, меняя в них местами каждые
две соседние цифры пока не встретит число из К подряд идущих нулей.
После чего вывод идет без смены и прописью.
'''
import re
dc_cifr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'} #Словарь с цифрами
file_name = "text.txt" #Выбор файла
k = int(input("Число К = "))
k0 = False #Встретилось ли число, состоящее из нулей
with open(file_name, 'r') as file:
    f = file.readlines()
    for i, gived_num in enumerate(f):
        gived_num = gived_num.replace('\n', '')
        if gived_num == '0' * k:
            k0 = True
            continue
        if re.match("^[0-9]+$", gived_num) and re.match("^[02468]+$", gived_num[-1]):
            if k0:
                for i in gived_num: print(dc_cifr[i], end=' ')
            else:
                for i in range(0, len(gived_num) - 1, 2):
                    gived_num = gived_num[:i] + gived_num[i + 1] + gived_num[i] + gived_num[i + 2:]  # Меняются местами не попарно
                print(gived_num, end='')
            print()
