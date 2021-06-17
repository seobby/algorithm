N, M = map(int, input().split())
icemap = [list(map(int, list(input()))) for i in range(N)]

def dfs(x, y):
    dx, dy = [1, -1, 0, 0,], [0, 0, 1, -1]

    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if icemap[x][y] == 0:
        icemap[x][y] = 1
        for idx in range(4):
            nx, ny = x+dx[idx], y+dy[idx]
            dfs(nx, ny)
        return True
    return False

cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)