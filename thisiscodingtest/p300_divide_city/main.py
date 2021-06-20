
# 서로소 집합 연산 정의
def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])

    return parents[x]

def union_parents(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)

    if a > b:
        parents[a] = b
    else:
        parents[b] = a


N, M = map(int, input().split())
parents = [i for i in range(N+1)]
edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()


max_cost = 0
total_cost = 0
for e in edges:
    cost, a, b = e
    if find_parent(parents, a) != find_parent(parents, b):
        union_parents(parents, a, b)
        total_cost += cost
        max_cost = max(max_cost, cost)

print(total_cost - max_cost)

