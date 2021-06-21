from collections import deque

N, M = map(int, input().split())

graph = {
}

queue = deque([])

# 1-based 배열로 간주함 (노드 번호와 인덱스를 동일하게 맞춤)
indegrees = [0 for _ in range(N+1)]

# 자료 입력
for i in range(N+1):
    graph[i] = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 위상 정렬 알고리즘
# indegree 가 0인 것들만 뽑아낸다.
for k, v in graph.items():
    for n in v:
        indegrees[n] += 1

# 초기 값을 큐에 넣는다.
# indegree가 0인 것들만...
for i in range(1, N+1):
    if indegrees[i] == 0:
        queue.append(i)

answer = []

while queue:
    n = queue.popleft()
    answer.append(n)
    for node in graph[n]:
        indegrees[node] -= 1
        if indegrees[node] == 0:
            queue.append(node)

print(' '.join(map(str, answer)))
