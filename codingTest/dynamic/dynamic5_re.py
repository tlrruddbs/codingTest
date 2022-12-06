n, m = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

d = [10001] * 10001
d[0] = 0

#2, 3, 5
for i in arr:
    for j in range(arr[i], m+1):
        if d[j - i] != 10001:
            d[j] = min(d[i], d[j - 1] + 1)




