# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan = int(input('Введите номер VLAN: '))
all = []
with open('CAM_table.txt') as f:
    for line in f:
        if line == '\n':
            pass
        else:
            line = line.split()
            if line[0].isdigit():
                line.remove('DYNAMIC')
                line[0] = int(line[0])
                all.append(line)
            else:
                continue
    all.sort()
    for st in all:
        if vlan == st[0]:
            print("{:>15} {:>15} {:>15}".format(st[0], st[1], st[2]))