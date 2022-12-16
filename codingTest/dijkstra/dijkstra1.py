INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            if graph[a][b] == INF:
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)
#수행된 결과를 출력
# for a in range(n+1):
#     for b in range(n+1):
#         if graph[a][b] == INF:
#             print("inf")
#         else:
#             print(graph[a][b], end= '')
#     print()