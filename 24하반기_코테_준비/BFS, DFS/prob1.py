from collections import deque


def bfs(grid, start, visited):
  dy = [1, -1, 0, 0]
  dx = [0, 0, 1, -1]
  global n, m
  global cnt
  queue = deque([start])
  visited[start[0]][start[1]] = True  # 큐에 넣기 전에 방문 처리

  while queue:
    i, j = queue.popleft()
    for k in range(4):
      ny = i + dy[k]
      nx = j + dx[k]
      if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and grid[ny][
          nx] == 0:
        visited[ny][nx] = True  # 큐에 넣기 전에 방문 처리
        queue.append((ny, nx))
  cnt += 1


n, m = map(int, input().split())
grid = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

cnt = 0

for i in range(n):
  for j in range(m):
    if grid[i][j] == 1 or visited[i][j]:
      continue
    else:
      bfs(grid, (i, j), visited)

print(cnt)
