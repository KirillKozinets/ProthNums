import random


def input_int():
    num = input()
    if num.isdigit():
        return int(num)
    raise TypeError("You must enter a number")


def check_input(n, k):
    if n < 0:
        raise Exception("n must be > 0")
    if k <= 0 or k >= 2 ** n:
        raise Exception("k must be between 0 and 2 raised to power n")
    if k % 2 == 0:
        raise Exception("k must be odd")


def get_proth_num(n, k):
    return k * pow(2, n) + 1


def is_prime_num(prothNum):
    a = random.randrange(2, prothNum)
    if (a - 1) % prothNum != 0:
        b = pow(a, (prothNum - 1) / 2) % prothNum
        if (b + 1) % prothNum == 0:
            return True
        elif (b - 1) % prothNum == 0:
            return is_prime_num(prothNum)
        return False
    return is_prime_num(prothNum)


def is_need_continue():
    print("Do you want continue?(Y/n)", end='')
    is_need = input()
    if is_need == "Y":
        return True
    else:
        return False


def main():
    while True:
        try:
            print("n: ", end='')
            n = input_int()
            print("k: ", end='')
            k = input_int()
            check_input(n, k)
            prothNum = get_proth_num(n, k)
            isProth = is_prime_num(prothNum)
            if isProth:
                print(str(prothNum) + " is a prime number")
            else:
                print(str(prothNum) + " isn't a prime number")
            is_continue = is_need_continue()
            if not is_continue:
                return
        except Exception as ex:
            print(str(ex))


main()
