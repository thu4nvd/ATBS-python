# import copy

spam = ['apples', 'bananas', 'tofu', 'cats', 'thor', 'hulk', 'avenger']
result = 'List included: ' + spam[0]

for item in range(0, len(spam) - 1):
    result += ', ' + spam[item]

result += ' and ' + spam[len(spam) - 1]
print(result)
