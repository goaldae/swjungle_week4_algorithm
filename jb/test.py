import sys
import copy

N, K = map(int, sys.stdin.readline().split())

initial_order = list(map(int, sys.stdin.readline().split()))

socket = set()

socket.update(initial_order[:N])

count = 0
order = initial_order[N:]

for i in range(len(order)):
    if order[i] in socket:
        continue
    else:
        temp = copy.deepcopy(socket)
        for j in range(i, len(order)):
            if order[j] in socket:
                temp.remove(order[j])
                if len(temp) == 1:
                    el = temp.pop()
                    socket.remove(el)
                    socket.add(order[i])
                    count += 1
                    break

print(socket)

print(count)
