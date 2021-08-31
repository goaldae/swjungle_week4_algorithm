import sys

N, V = map(int, sys.stdin.readline().split())

data = [int(sys.stdin.readline()) for _ in range(N)]

count = 0

def make_combi(v, data):
    global count

    try:
        if v < data[0]:
            return

        coin = data[-1]
        count_up = v // coin
    except:
        return

    if count_up > 0:
        remain = v % coin

        count += count_up
        data.pop()
        make_combi(remain, data)
    else:
        data.pop()
        make_combi(v, data)

make_combi(V, data)

print(count)
sys.exit(0)


