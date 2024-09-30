def dfs(grid, x, y, ans):
  if x == n - 1 and y == m - 1:
    return ans
  grid[x][y] = 0
  if 0 <= y + 1 <= m - 1 and grid[x][y + 1] == 1:
    return dfs(grid, x, y + 1, ans + 1)

  if 0 <= x + 1 <= n - 1 and grid[x + 1][y] == 1:
    return dfs(grid, x + 1, y, ans + 1)

  return ans


n, m = map(int, input().split())
grid = [list(map(int, input())) for _ in range(n)]
ans = 1
x, y = 0, 0

# dfs로 들어갈때 오른쪽, 아래쪽으로

print(dfs(grid, x, y, ans))
