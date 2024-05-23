'''
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона),
сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие
минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
Вариант 2. В холодильнике 10 брикетов мороженого разного вида.
Ребенку разрешается взять вечером не более 2 брикетов.
Подготовьте различные варианты поедания мороженного ребенком на неделю.
На следующий день нельзя есть больше мороженного, чем в предыдущий
'''
import itertools
import math

def shufleOrder(pool, order):
    global orders
    if len(pool) < 1:
        orders.append(order)
        return
    for i in pool:
        npool = []
        npool.extend(pool)
        npool.remove(i)
        norder = []
        norder.extend(order)
        norder.append(i)
        shufleOrder(npool, norder)

def shufleCounts(summ, count, j):
    global counts
    if j < 1:
        counts.append(count)
        return
    if summ < 1:
        count.append(0)
        shufleCounts(summ, count, j-1)
    elif summ < 2:
        count.append(1)
        shufleCounts(summ-1, count, j-1)
    else:
        ncount = []
        ncount.extend(count)
        ncount.append(1)
        shufleCounts(summ-1, ncount, j-1)
        if j == 7:
            count.append(2)
            shufleCounts(summ - 2, count, j - 1)
        elif count[-1] == 2:
            count.append(2)
            shufleCounts(summ-2, count, j-1)

bricks = ["Брикет 1", "Брикет 2", "Брикет 3", "Брикет 4", "Брикет 5", "Брикет 6", "Брикет 7", "Брикет 8", "Брикет 9", "Брикет 10"]
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
c = int(input("Количество выводимых вариантов : "))

orders = []
counts = []

shufleOrder(bricks, [])
shufleCounts(10, [], 7)

print('Результат работы алгоритма : ')
i = 0
for order in orders:
    if i >= c: break
    for count in counts:
        if i >= c: break
        print('Случай {:} : '.format(i+1))
        i += 1
        j = 0
        for day, count in enumerate(count):
            print(' | ', days[day], end=' : ')
            for k in range(count):
                print(order[j], end=' ')
                j += 1
        print()


ordersit = list(itertools.permutations(bricks, 10))
countsit = list(itertools.combinations_with_replacement([2,1,0], 7))

print('\nРезультат работы itertools : ')
i = 0
for order in ordersit:
    if i >= c: break
    for count in countsit:
        if i >= c: break
        if sum(count) > 10: continue
        print('Случай {:} : '.format(i+1))
        i += 1
        j = 0
        for day, count in enumerate(count):
            print(' | ', days[day], end=' : ')
            for k in range(count):
                print(order[j], end=' ')
                j+=1
        print()