# 런타임에러
import sys
# N, K = map(int, sys.stdin.readline().split())
N, K = map(int, input().split())

gene = dict()

for _ in range(N):
    # a, b = map(int, sys.stdin.readline().strip().split())
    a, b = map(int, input().split())
    gene[a] = b

gene_key = sorted(gene.keys())

def optimize(k):
    if k in gene:
        return gene[k]

    bucket = []

    for i in gene_key:
        # if k - i < gene_key[0] or (k - i) not in gene:
        if k - i < gene_key[0]:
            continue
        elif (k-i) in gene:
            value = gene[k-i] + optimize(i)
            bucket.append(value) 
        else:
            value = optimize(k-i) + optimize(i)
            gene[k] = value
            bucket.append(value)

    return max(bucket)

if gene_key[0] > K:
    print(0)
    sys.exit(0)

result = optimize(K)
if result > 0:
    print(result)
else:
    print(0)
