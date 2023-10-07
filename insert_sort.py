
a = [1, 8, 4, 6, 3, 84, 2, 94, 78, 32]
for j in range(1, len(a)):
    key = a[j] 
    i = j-1
    while (i > -1) and key < a[i]:
        a[i+1] = a[i]
        i -= 1
    a[i+1] = key
print(a)
