""" Нахлдит n-ое число Прота и проверяет
    является ли оно простым
"""
import random


def input_int():
    """ Считывает целочисленное число """
    while not (num := input()).isdigit():
        print("You must enter a number")
    return int(num)


def check_input(num_n, num_k):
    """ Проверяет удовлетворяют ли n и k словиям
        0 <= n , 0 < k < 2 в степени n, k - чётное
    """
    if num_n < 0:
        print("n must be > 0")
        return False
    if num_k <= 0 or num_k >= 2 ** num_n:
        print("k must be between 0 and 2 raised to power n")
        return False
    if num_k % 2 == 0:
        print("k must be odd")
        return False
    return True


def get_proth_num(num_n, num_k):
    """ Вычисляет число прота по формуле  p = k * (2 в степени n) + 1 """
    return num_k * pow(2, num_n) + 1


def is_prime_num(proth_num):
    """ Проверяет является ли число прота простым """
    num_a = random.randrange(2, proth_num)
    num_b = num_a ** ((proth_num - 1) // 2) % proth_num
    if (num_b + 1) % proth_num == 0:
        return True
    if (num_b - 1) % proth_num == 0:
        return is_prime_num(proth_num)
    return False


def is_need_continue():
    """ Проверяет необходимсость продолжения работы программы """
    print("Do you want continue?(Y/n)", end='')
    is_need = input()
    if is_need == "Y":
        return True
    return False


def main():
    """ Вычисляет число прота и выводит информацию о
    том является ли это число простым"""
    while is_need_continue():
        print("n: ", end='')
        num_n = input_int()
        print("k: ", end='')
        num_k = input_int()
        if check_input(num_n, num_k):
            proth_num = get_proth_num(num_n, num_k)
            is_prime = is_prime_num(proth_num)
            if is_prime:
                print(str(proth_num) + " is a prime number")
            else:
                print(str(proth_num) + " isn't a prime number")


main()
