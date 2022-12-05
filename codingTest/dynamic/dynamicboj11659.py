n, m = map(int, input().split())
arr = map(int, input().split())
ran = []
for i in range(0, m):
    ran.append(map(int, input().split()))

d = [0] * 100001
d = ran
while n == 0:
    for i in range(i, j):
        d[i] = d[j]-d[i-1]
    n -= 1

