from datetime import datetime


def timeit(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result

    return wrapper


@timeit
def one():
    mas = [x for x in range(10 ** 7) if x % 2 == 0]
    return mas


@timeit
def two():
    mas = []
    for x in range(10 ** 7):
        if x % 2 == 0:
            mas.append(x)
    return mas


one()
two()