def erat(n):
	mas = list(range(n+1))
	mas[1]=0
	for i in mas:
		if i > 1:
			for l in range(i+i,len(mas),i):
				mas[l] = 0
	return mas
a = int(input())
print(erat(a))