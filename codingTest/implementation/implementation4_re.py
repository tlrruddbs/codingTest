n, m = map(int, input().split())
x, y, direction = map(int, input().split())
d = [[0] * n for _ in range(m)]
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction += 1
    if direction == 4:
        direction = 0
cnt = 0
turn_time = 0
while True:
    turn_left()
    nx = dx[direction] + x
    ny = dy[direction] + y

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        x, y = nx, ny
        cnt += 1
        d[nx][ny] = 1
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(cnt)




