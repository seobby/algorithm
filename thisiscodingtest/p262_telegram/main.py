import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

N, M, C = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]

for _ in range(M):
   a, b, c = map(int, input().split())
   graph[a].append((b, c))


def dijkstra():
    # list for heapq
    q = []
    # 초기 설정
    heapq.heappush(q, (0, C))
    distance[C] = 0  # 시작 노드의 거리는 0

    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue

        for i, c in graph[node]:
            if distance[i] > distance[node] + c:
                distance[i] = distance[node] + c
                heapq.heappush(q, (c, i))


dijkstra()

num_city = len([0 for i in distance[2:] if i != INF])
time = max(distance[2:])

print(num_city, time)
