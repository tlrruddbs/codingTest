n = int(input())

d = [0] * 30001
d[0] = 0
d[1] = 0
d[2] = 1
d[3] = 1


d = [0] * 30001
for i in range(4,  n+1):
    d[i] = d[i-1] + 1
    if n % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    if n % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if n % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[n])

#
#


