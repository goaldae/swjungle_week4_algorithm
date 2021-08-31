import sys

N, K = map(int, sys.stdin.readline().split())

data = []

for i in range(N):
    # a(weight), b(value)
    a, b = map(int, sys.stdin.readline().split())
    data.append((a, b))

graph = [[0 for _ in range(K + 1)] for _ in range(N+1)]

for i in range(1, N+1):
    temp_w, temp_v = data[i-1]
    for j in range(1, K+1):
        # j(weight) 채울 수 있는 최대치 
        if temp_w > j:
            graph[i][j] = graph[i-1][j]
        else:
            graph[i][j] = max(graph[i-1][j], graph[i-1][j-temp_w] + temp_v)

print(graph[-1][-1])
