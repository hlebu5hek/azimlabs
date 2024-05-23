'''
Вариант 2. В холодильнике 10 брикетов мороженого разного вида.
Ребенку разрешается взять вечером не более 2 брикетов.
Подготовьте различные варианты поедания мороженного ребенком на неделю.
На следующий день нельзя есть больше мороженного, чем в предыдущий
'''
import itertools
import math
from tkinter import *
from tkinter import ttk

bricks = ["Брикет 1", "Брикет 2", "Брикет 3", "Брикет 4", "Брикет 5", "Брикет 6", "Брикет 7", "Брикет 8", "Брикет 9", "Брикет 10"]
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
c = 15
itstrs = []
funcstrs = []

orders = []
counts = []
ordersit = []
countsit = []

root = Tk()
root.geometry('1200x840')
root.resizable(False, False)

labelc = ttk.Label(text="Количество выводимых вариантов: ")
labelc.place(anchor=NW, x = 30, y = 20, height = 25)
entryc = ttk.Entry()
entryc.place(anchor=NW, x = 250, y = 20, height = 25, width = 80)

labelit = ttk.Label(text="Результат Itertools : ")
labelit.place(anchor=NW, x = 30, y = 60, height = 25, width = 240)

labelal = ttk.Label(text="Результат алгоритма : ")
labelal.place(anchor=NW, x = 30, y = 420, height = 25, width = 240)

def drawScroll():
    itlist = StringVar(value=itstrs)
    listboxd = Listbox(listvariable=itlist)
    listboxd.place(anchor=NW, x=30, y=90, width=1140, height=320)

    scrollbar = ttk.Scrollbar(orient="vertical", command=listboxd.yview)
    scrollbar.place(anchor=NW, y=90, x=1150, width=20, height=320)
    listboxd["yscrollcommand"] = scrollbar.set

    funclist = StringVar(value=funcstrs)
    listboxt = Listbox(listvariable=funclist)
    listboxt.place(anchor=NW, x=30, y=450, width=1140, height=320)

    scrollbar = ttk.Scrollbar(orient="vertical", command=listboxt.yview)
    scrollbar.place(anchor=NW, y=450, x=1150, width=20, height=320)
    listboxt["yscrollcommand"] = scrollbar.set


drawScroll()

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


def countAll():
    global orders
    global counts
    global ordersit
    global countsit

    shufleOrder(bricks, [])
    shufleCounts(10, [], 7)

    ordersit = list(itertools.permutations(bricks, 10))
    countsit = list(itertools.combinations_with_replacement([2, 1, 0], 7))


def mainAlg():
    try:
        c = int(entryc.get())
    except:
        return

    i = 0
    for order in orders:
        if i >= c: break
        for count in counts:
            if i >= c: break
            funcstrs.append('Случай {:} : '.format(i + 1))
            i += 1
            j = 0
            for day, count in enumerate(count):
                funcstrs[-1] += ' | ' + days[day] + ' : '
                for k in range(count):
                    funcstrs[-1] += order[j] + ' '
                    j += 1

    i = 0
    for order in ordersit:
        if i >= c: break
        for count in countsit:
            if i >= c: break
            if sum(count) > 10: continue
            itstrs.append('Случай {:} : '.format(i + 1))
            i += 1
            j = 0
            for day, count in enumerate(count):
                itstrs[-1] += ' | ' + days[day] + ' : '
                for k in range(count):
                    itstrs[-1] += order[j] + ' '
                    j += 1

    drawScroll()


countAll()

btn = ttk.Button(text="Рассчитать", command=mainAlg)
btn.place(anchor=NW, x = 380, y = 20, height = 25, width = 100)

root.mainloop()