n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

def binarySearch(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return "yes"
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return "no"


nList.sort()
for i in mList:
    print(binarySearch(nList, i, 0, n - 1), end=' ')


