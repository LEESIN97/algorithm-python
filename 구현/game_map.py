n, m = map(int, input().split())
a, b, dir = map(int, input().split())
step = [(-1, 0), (0, -1), (1, 0), (0, 1)]
map = [list(map(int, input().split())) for _ in range(n)]
cnt = 1
cant_go = 0
while True:
  if cant_go >=8:
    break
  if cant_go == 4:
    map[a][b] = 2
    a -= step[dir][0]
    b -= step[dir][1]
  if dir == 3:
    dir = 0
  elif dir != 3:
    dir += 1
  if map[a + step[dir][0]][b + step[dir][1]] == 1 or map[a + step[dir][0]][b + step[dir][1]] == 2:
    cant_go +=1
    continue
  elif map[a + step[dir][0]][b + step[dir][1]] == 0:
    map[a][b] = 2 # 방문 check
    a += step[dir][0]
    b += step[dir][1]
    cnt += 1
    cant_go = 0


print(cnt)
