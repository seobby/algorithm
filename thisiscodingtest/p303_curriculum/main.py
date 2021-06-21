from collections import deque
import copy

N = int(input())

graph = [[] for _ in range(N+1)]
indegrees = [0 for _ in range(N+1)]
time = [0 for _ in range(N+1)]
result = [0 for _ in range(N+1)]

queue = deque([])

for i in range(1, N+1):
    lst = list(map(int, input().split()))
    time[i] = lst[0]
    for n in lst[1:-1]:
        graph[n].append(i)
        indegrees[i] += 1

result = copy.deepcopy(time)

for n in range(1, N+1):
    if indegrees[n] == 0:
        queue.append(n)

while queue:
    n = queue.popleft()
    # visit n

    for x in graph[n]:
        indegrees[x] -= 1
        if indegrees[x] == 0:
            queue.append(x)
        result[x] = max(result[x], result[n] + time[x])

print(' '.join(map(str, result[1:])))
