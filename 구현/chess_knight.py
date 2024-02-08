current_pos = list(input())
x = int(ord(current_pos[0]) - ord('a') + 1)
y = int(current_pos[1])
move_dx = [-2, -2, 2, 2, -1, -1, 1, 1]
move_dy = [-1, 1, -1, 1, 2, -2, 2, -2]

cnt = 0

for i in range(8):
  if 1 <= (x + move_dx[i]) <= 8 and 1 <= (y + move_dy[i]) <= 8:
    cnt += 1
print(cnt)
