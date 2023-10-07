foo = [1]
bar = foo
bar += [2]
print(foo, bar, sep="\n")


def test(num, targ=[]):
    targ.append(num)
    return targ


print(test(1))
print(test(2))
print(test(3))


def test(num, targ=None):
    if targ is None:
        targ = []
    targ.append(num)
    return targ


print(test(1))
print(test(2))
print(test(3))


def hi(name="Ivan"):
    print("Hi " + name)


greet = hi


del hi
print(greet())
