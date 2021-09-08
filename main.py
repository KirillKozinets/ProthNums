import random


def input_int():
    while not (num := input()).isdigit():
        print("You must enter a number")
    return int(num)


def check_input(n, k):
    if n < 0:
        print("n must be > 0")
    elif k <= 0 or k >= 2 ** n:
        print("k must be between 0 and 2 raised to power n")
    elif k % 2 == 0:
        print("k must be odd")
    else:
        return True


def get_proth_num(n, k):
    return k * pow(2, n) + 1


def is_prime_num(prothNum):
    a = random.randrange(2, prothNum)
    b = a ** ((prothNum - 1) // 2) % prothNum
    if (b + 1) % prothNum == 0:
        return True
    elif (b - 1) % prothNum == 0:
        return is_prime_num(prothNum)
    return False


def is_need_continue():
    print("Do you want continue?(Y/n)", end='')
    is_need = input()
    if is_need == "Y":
        return True
    else:
        return False


def main():
    while is_need_continue():
        print("n: ", end='')
        n = input_int()
        print("k: ", end='')
        k = input_int()
        if check_input(n, k):
            prothNum = get_proth_num(n, k)
            isPrime = is_prime_num(prothNum)
            if isPrime:
                print(str(prothNum) + " is a prime number")
            else:
                print(str(prothNum) + " isn't a prime number")


main()

