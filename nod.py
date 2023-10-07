def func(x):
	if x > 0:
		return 1
	else:
		return 0
a = [1, -4, 6, 8, -10]
a = filter(func, a)
a = list(a)
print(a)
