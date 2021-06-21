import sys

input = sys.stdin.readline

INF = int(1e9)

N, V = map(int, input().split())
start = int(input())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
distance = [INF for _ in range(N+1)]
distance[start] = 0  # 시작 노드의 거리는 0

for _ in range(V):
   a, b, c = map(int, input().split())
   graph[a].append((b, c))


def get_smallest_node():
   min_distance = INF
   node = 0

   for i in range(N+1):
      if distance[i] < min_distance and not visited[i]:
         node = i
         min_distance = distance[i]

   return node


def dijkstra():
    # 초기 설정
    visited[start] = True

    for i, c in graph[start]:
        distance[i] = c

    # 시작 노드를 제외하고 나머지 노드에 대해서 실행
    for _ in range(N-1):
        node = get_smallest_node()      # 가장 비용이 작은 노드를 선택
        visited[node] = True            # 방문 처리를 수행함

        # 방문 중인 노드로부터 갈 수 있는 노드에 대하여
        for i, c in graph[node]:
            # 기존 최단 경로보다 방문 중인 노드를 통해 이동하는 경우가 더 거리가 저렴하다면 최단 거리 테이블을 업데이트 함
            if distance[i] > distance[node] + c:
                distance[i] = distance[node] + c

dijkstra()

print(distance[1:])
