n = int(input())
d = [0] * 100001
d[1] = 0
d[2] = 2
d[3] = 3

for i in range(4, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
