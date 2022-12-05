n = int(input())

d = [0] * 1000001
d[0] = 0
d[1] = 0
d[2] = 1

pre = [0] * 1000001
array = []
for i in range(3, n+1):
    d[i] = d[i - 1] + 1
    pre[i] = i-1

    if i % 2 == 0 and d[i] > d[i//2]+1:
        d[i] = d[i//2] + 1
        pre[i] = i//2

    if i % 3 == 0 and d[i] > d[i//3]+1:
        d[i] = d[i//3] + 1
        pre[i] = i//3

cur = n
while pre[cur] != 0:
    print(pre[cur], end=' ')

    cur = pre[cur]
