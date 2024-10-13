def dfs(x, y):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    visited[x][y] = True
    count = 1


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]


        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 1:
            count += dfs(nx, ny)

    return count


N = int(input())
grid = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]


complexes = []


for i in range(N):
    for j in range(N):

        if grid[i][j] == 1 and not visited[i][j]:

            complexes.append(dfs(i, j))


print(len(complexes))


for complex_size in sorted(complexes):
    print(complex_size)