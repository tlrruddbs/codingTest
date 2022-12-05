x = int(input())
d = [0]*30001
d[1] = 0
cnt = 0

for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    print("d["+str(i)+"]: "+str(d[i]))

    if i % 2 == 0:
        print("d[" + str(i) + "] = min(" + str(d[i]) + ", d[" + str(d[i // 2]) + "] +1)")
        d[i] = min(d[i], d[i // 2] + 1)

        print("2로 나누기 "+str(d[i]))
    if i % 3 == 0:
        print("d[" + str(i) + "] = min(" + str(d[i]) + ", d[" + str(d[i // 3]) + "] +1)")
        d[i] = min(d[i], d[i // 3] + 1)

        print("3로 나누기 " +str(d[i]))
    if i % 5 == 0:
        print("d[" + str(i) + "] = min(" + str(d[i]) + ", d[" + str(d[i // 5]) + "] +1)")
        d[i] = min(d[i], d[i // 5] + 1)

        print("5로 나누기 " +str(d[i]))

print(d[x])





