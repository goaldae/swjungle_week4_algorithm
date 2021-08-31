import sys

N = int(sys.stdin.readline())

metrix = []

for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    metrix.append(temp)

print(metrix)

graph = [[0]*(N) for _ in range(N)]
print(graph)

for i in range(1, N+1):
    for j in range(i-1, -1, -1):
        graph[i][j] = 1000000*16
        for k in range(0, j+1):
            if k == 0 or k == j:
                graph[i][j] = graph[1][j] + metrix[j]
            else:
                graph[i][j] = max(graph[i][j], graph[1][k-1] + graph[k+1][j] + metrix[k-1][k] + metrix[k][k+1])
