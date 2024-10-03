n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)

ans = 0
ans_idx = 0
start_idx = 0
end_idx = n - 1
mid_idx = (start_idx + end_idx) // 2
while ans != m:
  ans = 0
  for i in range(mid_idx):
    ans += lst[i] - lst[mid_idx]
  if ans < m:
    start_idx = mid_idx
    mid_idx = (start_idx + end_idx) // 2
    ans_idx = mid_idx
  if ans > m:
    end_idx = mid_idx
    mid_idx = (start_idx + end_idx) // 2
    ans_idx = mid_idx

print(lst[ans_idx])
