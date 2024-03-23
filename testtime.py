import time


def test_time(func):
    def wrapp(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        etime = time.time() - start
        print(f'Время работы {etime}')
        return result

    return wrapp

@test_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

@test_time
def fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b

    return a

# print(get_nod(3, 1000000000))
print(fast_nod(3, 1000000000000000000000000000000000000000000))
