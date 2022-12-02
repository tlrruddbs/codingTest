n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda x: x[1], reverse=False)

for arr in array:
    print(arr[0], end=' ')
