# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

config = argv[1]
result = argv[2]

ignore = ["duplex", "alias", "configuration"]

with open(config) as f, open(result, 'w') as d:
    for line in f:
        if line.startswith("!") or line.count("duplex") == 1 or line.count('alias') == 1 or line.count("configuration") == 1:
            continue
        else:
            d.write(line)