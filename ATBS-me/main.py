

def _print_list(spam):
    str = ""
    for item in spam :

    spam[len(spam) - 1] = "and " + spam[len(spam) - 1 ]
    print(spam)


spam = ['apples', 'bananas', 'tofu', 'cats']


_print_list(spam)