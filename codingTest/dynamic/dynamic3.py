n = int(input())
s = list(map(int, input().split()))
s.insert(0, 0)
d = [0] * 101
print(d)

d[1] = s[1]
d[2] = max(s[1], s[2])

for i in range(3, n + 1):
    d[i] = max(d[i-1], d[i-2]+s[i])

print(d[n])
