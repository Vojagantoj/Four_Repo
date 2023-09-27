# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
add = input('Введите адрес в формате X.X.X.X: ')
addr = add.split('.')
ad = False
while not ad:
    if add.count('.') == 3 and len(addr) == 4 and ''.join(addr).isdigit():
        for oct in addr:
            if oct != '' and 0 <= int(oct) <= 255:
                pass
            else:
                ad = True
                print('неправильный ip-адрес')
                break
        if 1 <= int(addr[0]) <= 223 and ad == False:
            print('unicast')
            break
        elif 224 <= int(addr[0]) <= 239 and ad == False:
            print('multicast')
            break
        elif int(addr[0]) == int(addr[1]) == int(addr[2]) == int(addr[3]) == 255 and ad == False:
            print('local broadcast')
            break
        elif int(addr[0]) == int(addr[1]) == int(addr[2]) == int(addr[3]) == 0 and ad == False:
            print('unassigned')
            break
        elif ad == False:
            print('unused')
            break
    else:
        print('неправильный ip-адрес')
        break
