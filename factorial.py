def fact(a):
	if a == 0:
		return 1
	return fact(a-1)*a
a = int(input())
print(fact(a))