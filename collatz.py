import sys


def visualPrint(number):
    print('|'*int(number))


def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    return(int(result))


number = input('Enter integer number:    ')

try:
    number = float(number)
except:
    sys.exit("The integer number is only accepted.")


if (number).is_integer():   # attribute of float type
    # print(int(number))
    visualPrint(number)
    while number != 1:
        number = collatz(number)
        # print(number)
        visualPrint(number)
else:
    sys.exit("The integer number is only accepted.")

