'''
Натуральные числа.
Выводит на экран четные числа, меняя в них местами каждые
две соседние цифры пока не встретит число из К подряд идущих нулей.
После чего вывод идет без смены и прописью.
'''
#Словарь с цифрами
dc_cifr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
#Баффер
gived_num = '1'
#Выбор файла
file_name = "text.txt"
#Число K
k = 3

try:
    open(file_name, 'r')
except:
    print('Файл отсутствует в директории проекта')
    exit()

k0 = False
with open(file_name, 'r') as file:
    while 1:
        gived_num = file.readline().replace('\n', '')
        if not gived_num:
            #print('Файл закончился')
            break
        if not gived_num.isdigit():
            continue
        if int(gived_num) % 2 != 0:
            continue
        if gived_num == '0'*k:
            k0 = True
            continue

        if k0:
            for i in gived_num: print(dc_cifr[i], end=' ')
            print()
        else:
            for i in range(0, len(gived_num)-1, 2):
                print(gived_num[i+1] + gived_num[i], end='')
            if len(gived_num) % 2 != 0:
                print(gived_num[-1], end='')
            print()
