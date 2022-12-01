n = int(input())
control = input().split()

x = 1
y = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

tmpX = 0
tmpY = 0
move_type = ['L', 'R', 'U', 'D']


for cont in control:
    for i in range(len(move_type)):
        if cont == move_type[i]:
            tmpX = x + dx[i]
            tmpY = y + dy[i]
    if tmpX < 1 or tmpX > n or tmpY < 1 or tmpX > n:
        continue
    else:
        x = tmpX
        y = tmpY


print(str(x)+" "+str(y))


