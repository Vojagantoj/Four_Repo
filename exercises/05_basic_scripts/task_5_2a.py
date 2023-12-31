# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

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
ipadd = '''{0:08b}{1:08b}{2:08b}{3:08b}'''
net = input('Введите IP-сеть в формате X.X.X.X/X: ')
mask = net.split('/')[-1]
dec_mask = "1" * int(mask) + "0" * (32 - int(mask))
net = net[:net.find('/')].split('.')
ipadd = ipadd.format(int(net[0]), int(net[1]), int(net[2]), int(net[3]))[:int(mask)] + "0" * (32 - int(mask))
print(ip_template.format(int(ipadd[:8], 2), int(ipadd[8:16], 2), int(ipadd[16:24], 2), int(ipadd[24:], 2), mask, int(dec_mask[:8], 2), int(dec_mask[8:16], 2), int(dec_mask[16:24], 2), int(dec_mask[24:], 2)))
