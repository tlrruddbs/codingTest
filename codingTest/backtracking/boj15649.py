

def func(k):
    if k == m:
        for i in range(m):
            print(str(arr[i]), end=' ')
        print()
    for i in range(1, n+1):

        if isused[i] == 0:
            arr[k] = i
            isused[i] = 1
            func(k+1)
            isused[i] = 0

n, m = map(int, input().split())
arr = [0] * 10
isused = [0] * 10
func(0)