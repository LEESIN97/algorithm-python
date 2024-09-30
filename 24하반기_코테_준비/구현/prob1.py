n = int(input())
dir_lst = list(map(str, input().split()))
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
dir_info = {'L': 0, 'R': 1, 'U': 2, 'D': 3}
start_x = 1
start_y = 1
for dir in dir_lst:
  inx = dir_info[dir]
  if 1 <= start_x + dx[inx] <= n and 1 <= start_y + dy[inx] <= n:
    start_x += dx[inx]
    start_y += dy[inx]
  else:
    continue

print(start_x, start_y)
