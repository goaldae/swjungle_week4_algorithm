import sys

N = int(sys.stdin.readline())

data = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    data.append((a, b))

meetings = sorted(data, key=lambda x:(x[1], x[0]))

count = 1
while len(meetings) > 1:
    if meetings[0][0] == meetings[0][1]:
        meetings = meetings[1:]
    else:
        end_point = meetings[0][1]
        meetings = [x for x in meetings if x[0] >= end_point]
    count += 1


if count > 0:
    print(count)
else:
    print(0)