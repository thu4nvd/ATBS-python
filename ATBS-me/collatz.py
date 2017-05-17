import sys


def collatz(param):
    if (param % 2 == 0):
        return (param / 2)
    else:
        return (param * 3 + 1)


try:
    topval = int(sys.argv[1])
except ValueError:
    print('input is not integer, default value 10 will be chosen')
    topval = 10

for i in range(1, topval, 1):
    arg = i
#    chain = [int(arg)]
    chain = str(arg)
    while (arg != 1):
        arg = collatz(arg)
        chain = chain + '|'
    print(chain + str(len(chain)))
