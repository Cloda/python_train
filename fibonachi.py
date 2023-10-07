from datetime import datetime


def fib(a):
    if a == 1 or a == 2:
        return 1
    return fib(a - 1) + fib(a - 2)


start = datetime.now()
fib(40)
finish = datetime.now()
pre, cur = 0, 1
start1 = datetime.now()
for i in range(1, 41):
    pre, cur = cur, pre + cur
finish1 = datetime.now()
print(finish - start)
print(finish1 - start1)
