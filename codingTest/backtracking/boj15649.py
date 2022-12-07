n, m = map(int, input().split())
arr = [0] * 10
isused = [0] * 10

def func(k):
    global n
    if k == m:
        for i in m:
            print(str(arr[i]), end=' ')
    for i in n:
        if isused[i] is False:
            arr[k] = i
            isused[i] = 1
            func(k+1)
            isused[i] = 0

func(0)