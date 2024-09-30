lst1 = list(map(int, input()))
lst1.sort()
ans_lst = [num for num in lst1 if num != 0]
ans = 1
for i in range(len(ans_lst)):
  ans *= ans_lst[i]
print(ans)