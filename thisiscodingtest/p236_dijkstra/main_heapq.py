import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

N, V = map(int, input().split())
start = int(input())

graph = [[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]

for _ in range(V):
   a, b, c = map(int, input().split())
   graph[a].append((b, c))


def dijkstra():
    # list for heapq
    q = []
    # 초기 설정
    heapq.heappush(q, (0, start))
    distance[start] = 0  # 시작 노드의 거리는 0

    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue

        for i, c in graph[node]:
            if distance[i] > distance[node] + c:
                distance[i] = distance[node] + c
                heapq.heappush(q, (c, i))


dijkstra()

print(distance[1:])
