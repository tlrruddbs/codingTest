n, m = list(map(int, input().split()))
x, y, direction = list(map(int, input().split()))
d = [[0] * m for _ in range(n)] #방문한 위치를 저장하기 위한 맵을 생성

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

def turn_left():
    global direction
    direction = direction -1
    if direction == -1:
        direction = 3

cnt = 0
turn_time = 0
while True:
    turn_left()
    nx = dx[direction] + x
    ny = dy[direction] + y

    if array[nx][ny] == 0 and d[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time+=1

    if turn_time == 4:
        nx = x-dx[direction]
        ny = y-dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(cnt)




