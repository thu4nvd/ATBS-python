spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''

# print(spam.split('\n'))

def printPicnic(string, test=[]):
    test.append(string)
    return(test)

print(printPicnic('test'))
print(printPicnic('test2'))

# Pay attention the difference
def printVacant(string, hollow=None):
    if not hollow:
        hollow = []
    hollow.append(string)
    return hollow

print(printVacant('harry'))
print(printVacant('herminone'))