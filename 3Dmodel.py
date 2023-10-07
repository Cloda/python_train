n = 1000
temp = 0
for i in range(1, n+1):
    m = 7*i - 4
    for l in range(2, m):
        if m % l != 0:
            temp += 1
    if temp == m - 2:
        if i % 5 == 0 and i % 3 == 0:
            print(m, i, "- 15")
        if i % 3 == 0 and i % 5 != 0:
            print(m, i, "- 3")
        if i % 3 != 0 and i % 5 == 0:
            print(m, i, "- 5")
        if i % 3 != 0 and i % 5 != 0 and i % 11 != 0 and i % 7 != 0 and i % 13 != 0:
            print(m, i, "- типа простое")
        if i % 7 == 0:
            print(m, i, "- 7")
        if i % 13 == 0:
            print(m, i, "- 13")
        if i % 11 == 0:
            print(m, i, "- 11")
    temp = 0
