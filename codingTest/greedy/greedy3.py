n, m = map(int, input().split())
res = []
for i in range(n):
    data = list(map(int, input().split()))
    res.append(min(data))

print(max(res))

