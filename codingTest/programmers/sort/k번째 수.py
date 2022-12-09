def solution(array, commands):
    res = []
    for command in commands:
        arr = array
        # command = commands[i]
        arr = arr[command[0] - 1:command[1]]
        arr.sort()

        res.append(arr[command[2] - 1])
    return res