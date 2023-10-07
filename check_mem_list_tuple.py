mas = ([i for i in range(1, 1000000)], [])  # tuple
mas1 = [[i for i in range(1, 1000000)], []]  # list
print(mas.__sizeof__())
print(mas1.__sizeof__())
