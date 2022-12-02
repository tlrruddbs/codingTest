from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

cnt = 0


def bfs(graph, start, visited):
    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end='')
        for i in graph[start]:
                queue.append(i)
                visited[i] = True


bfs(x,y)