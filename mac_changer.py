#!/usr/bin/env python

import random
import subprocess. # Запуск внешних процессов и работа с их выводами
import optparse # Парсер для параметров командной строки

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change it's MAC adress")
parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC adress")

(options, arguments) = parser.parse_args() # Метод parse_args возвращает два набора информации от пользователя: перменные и опции. Example (options:wlan0, arguments:--interface) 

interface = options.interface

random_list_for_mac_changer = []

def random_numbers_for_mac ():
    """
    Функция генерирует случайный набор двухзначных цифр от 10 до 99 и добовляет их в список random_list_for_mac_changer.
    """
    i = 0
    while i < 6:
        random_list_for_mac_changer.append(random.randrange(10, 99, 1))
        i += 1

def mac_changer ():
    """
    Функция изменяет mac адрес устройства с использованием shell команд, беря их из random_list_for_mac_changer.
    """
    subprocess.call("ifconfig {0} down".format(interface), shell = True)
    subprocess.call("ifconfig eth0 hw ether {0}:{1}:{2}:{3}:{4}:{5}".format(*random_list_for_mac_changer), shell = True)
    subprocess.call("ifconfig {0} up".format(interface), shell = True)

random_numbers_for_mac()
mac_changer()

print("Changing MAC adress for {} to {}".format(interface, random_list_for_mac_changer))