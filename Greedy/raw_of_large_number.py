n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort(reverse=True)

# m번을 더하여 가장 큰 수를 출력 하는 문제
# 똑같은 인덱스는 k번 연달아 더하는 것만 가능
ans = 0
ans = (num_list[0] * k + num_list[1]) * (m // (k+1)) + (m % (k+1)) * num_list[0]


print(ans)

