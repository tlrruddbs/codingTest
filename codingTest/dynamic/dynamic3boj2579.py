# n = input()
#  = list(map(int, input().split()))
s = [0, 10, 20, 15, 25, 10, 20]

rows = 10
cols = 10
d = [[0 for j in range(cols)] for i in range(rows)]

print(d)

d[1][1] = s[1]
d[1][2] = 0
d[2][1] = s[2]
d[2][2] = s[1]+s[2]

for i in range(3, 6+1):
    d[i][1] = max(d[i-2][1], d[i-2][2]) + s[i]
    d[i][2] = d[i-1][1] + s[i]

print(max(d[6][1], d[6][2]))
