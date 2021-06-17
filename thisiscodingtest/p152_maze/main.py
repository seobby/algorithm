from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for i in range(N)]
distance = [[1 for _ in range(M)] for _ in range(N)]
distance[0][0] = 1

q = deque([])
q.append((0, 0))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
while q:
    x, y = q.popleft()

    for idx in range(4):
        nx, ny = x + dx[idx], y + dy[idx]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if maze[nx][ny] == 0:
            continue

        if distance[nx][ny] == 1:
            distance[nx][ny] = distance[x][y] + 1
            q.append((nx, ny))
            print(nx, ny)


print(distance[N-1][M-1])
