# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_template = '''
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{4}
{5:<8}  {6:<8}  {7:<8}  {8:<8}
{5:08b}  {6:08b}  {7:08b}  {8:08b}
'''
net = input('Введите IP-сеть в формате X.X.X.X/X: ')
mask = net.split('/')[-1]
dec_mask = "1" * int(mask) + "0" * (32 - int(mask))
net = net[:net.find('/')].split('.')
print(ip_template.format(int(net[0]), int(net[1]), int(net[2]), int(net[3]), mask, int(dec_mask[:8], 2), int(dec_mask[8:16], 2), int(dec_mask[16:24], 2), int(dec_mask[24:], 2)))
