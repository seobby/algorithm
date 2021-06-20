
def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]


def union_parent(parents, a, b):
    parent_a = find_parent(parents, a)
    parent_b = find_parent(parents, b)

    if parent_a > parent_b:
        parents[parent_a] = parent_b
    else:
        parents[parent_b] = parent_a


N, E = map(int, input().split())
edges = []
for i in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 비용 기준으로 정렬함
edges.sort()

parents = [0] + [i for i in range(1, N+1)]

cost_sum = 0
for e in edges:
    cost, a, b = e

    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        cost_sum += cost

