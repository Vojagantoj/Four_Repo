# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задconfig_sw1ания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    with open(config_filename) as f:
        trunk = dict()
        access = dict()
        rf = list()
        for line in f:
            if line.count('Fast') != 0:
                key = line[line.find('Fast')::].rstrip()
            elif line.count('allowed vlan') != 0:
                value = line[line.find('vlan') + 5::].rstrip().split(',')
                nw = []
                for n in value:
                    nw.append(int(n))
                trunk[key] = nw
            elif line.count('access vlan') != 0:
                value1 = int(line[line.find('vlan') + 5::].rstrip())
                access[key] = value1
        rf.append(access)
        rf.append(trunk)
        result = tuple(rf)
    return result