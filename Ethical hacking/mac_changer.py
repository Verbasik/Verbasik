#!/usr/bin/env python

import random
import subprocess  # Запуск внешних процессов и работа с их выводами
import optparse    # Парсер для параметров командной строки


def random_numbers_for_mac():
    """
    Функция генерирует случайный набор двухзначных цифр от 10 до 99 и добовляет их в список random_list_for_mac_changer.
    """
    random_list_for_mac_changer = []
    i = 0
    while i < 6:
        random_list_for_mac_changer.append(random.randrange(10, 99, 1))
        i += 1
    return random_list_for_mac_changer


def get_arguments():
    """ 
    Функция считывает аргументы которые вводит пользователь, после чего парсит их.
    """
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change it's MAC adress") # Добавляем флаги для командной строки
    (options, arguments) = parser.parse_args() # Метод parse_args возвращает два набора информации от пользователя: перменные и опции. Example (options:wlan0, arguments:--interface)
    
    if not options.interface:
        parser.error("Пожалуйста, укажите название сетевого интерфейса. Для получения более детальной информации используйте команду --help")
    return options.interface


def mac_changer():
    """
    Функция изменяет mac адрес устройства с использованием shell команд, беря адрес из random_list_for_mac_changer.
    """
    subprocess.call("ifconfig {0} down".format(interface), shell = True)
    subprocess.call("ifconfig" + interface + "hw ether {0}:{1}:{2}:{3}:{4}:{5}".format(*random_list_for_mac_changer), shell = True)
    subprocess.call("ifconfig {0} up".format(interface), shell = True)


interface = get_arguments() # Доступ к значению переменной которую мы указали в dest = "interface"
random_list_for_mac_changer = random_numbers_for_mac()
mac_changer()
print("Changing MAC adress for {} to {}".format(interface, random_list_for_mac_changer))

