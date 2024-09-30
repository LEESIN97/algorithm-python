cur_pos = list(map(str, input()))

nx = ord(cur_pos[0]) - ord('a')
ny = int(cur_pos[1]) - 1
dy = [1, -1, 2, -2, 2, -2, 1, -1]
dx = [-2, -2, -1, -1, 1, 1, 2, 2]

cnt = 0
for y, x in zip(dx, dy):
  temp_x, temp_y = nx + x, ny + y
  if 0 <= temp_x <= 7 and 0 <= temp_y <= 7:
    cnt += 1

print(cnt)
