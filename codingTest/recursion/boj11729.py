n = int(input())

start = 1
end = 3

def func(a, b, n):
    if n == 1:
        print(str(a)+", "+str(b))
        return
    func(a, 6-a-b, n-1)
    print(str(a)+", "+str(b))
    func(6-a-b, b, n-1)

func(1, 3, n)