n, m, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)
res = 0
count = 0

for i in range(m):
    if count == k:
        res = res + a[1]
        count = 0
    else:
        res = res + a[0]
        count = count + 1

print(res)

