N, M = map(int, input().split())
icemap = [list(map(int, list(input()))) for i in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

stack = []
cnt = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for i in range(N):
    for j in range(M):
        if not visited[i][j] and icemap[i][j] == 0:
            if len(stack) == 0:
                cnt += 1
                stack.append((i, j))

            while stack:
                x, y = stack.pop()
                visited[x][y] = True

                for idx in range(4):
                    nx, ny = x + dx[idx], y + dy[idx]
                    if nx < 0 or nx >= N or ny < 0 or ny >= M or icemap[nx][ny] == 1:
                        continue
                    if not visited[nx][ny]:
                        stack.append((nx, ny))

print(cnt)