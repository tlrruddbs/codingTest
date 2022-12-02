n, m = map(int, input().split())
array = list(map(int, input().split()))

def binarySearch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        print(mid)
        cut = 0

        for i in range(len(array)):
            if array[i] - array[mid] > 0:
                cut = cut + array[i] - array[mid]

        print("cut: " + str(cut))
        if cut == target:
            print("cut: "+str(cut))
            return array[mid]
        elif cut > target:
            start = mid + 1
        else:
            end = mid - 1

array.sort()
res = binarySearch(array, m, 0, n-1)

print(res)




