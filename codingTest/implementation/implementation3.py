n = list(map(str, input()))

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
number = [1, 2, 3, 4, 5, 6, 7, 8]
x = int(n[1])
y = 0
for i in range(len(alpha)):
    if n[0] == alpha[i]:
        y = number[i]

dx = [1, -1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, 1, -1]

cnt = 0
for i in range(8):
    tmpX = x + dx[i]
    tmpY = y + dy[i]
    if tmpX < 1 or tmpY < 1 or tmpX > 8 or tmpY > 8:
        continue
    else:
        cnt = cnt + 1
print(cnt)