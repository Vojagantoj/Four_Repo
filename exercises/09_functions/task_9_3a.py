# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    with open(config_filename) as f:
        trunk = dict()
        access = dict()
        rf = list()
        for line in f:
            if line.count('Fast') != 0:
                key = line[line.find('Fast')::].rstrip()
                access[key] = 1
            elif line.count('allowed vlan') != 0:
                value = line[line.find('vlan') + 5::].rstrip().split(',')
                nw = []
                for n in value:
                    nw.append(int(n))
                trunk.update({key: nw})
                del access[key]
            elif line.count('access vlan') != 0:
                value1 = int(line[line.find('vlan') + 5::].rstrip())
                access.update({key: value1})
        rf.append(access)
        rf.append(trunk)
        result = tuple(rf)
    return result