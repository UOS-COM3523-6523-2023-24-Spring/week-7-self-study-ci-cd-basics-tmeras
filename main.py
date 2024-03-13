import random


def simple_count(s):
    return len(s)


def random_function():
    import random
    # random.seed(5)

    if random.random() < 0.001:
        return True
    else:
        return False


def complex_function():
    if random_function():
        return 'behaviour 1'
    else:
        return 'behaviour 2'
