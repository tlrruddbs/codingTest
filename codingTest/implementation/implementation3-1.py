input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a'))+1

print(int(ord('a'))+1)
print(int(ord(input_data[0])))
print(column)

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
cnt = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 9:
        cnt += 1

print(cnt)