from collections import deque
def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    q = deque(arr)
    tmp = 10
    while q:
        tmp2 = q.popleft()
        if tmp != tmp2:
            answer.append(tmp2)
        tmp = tmp2


    print('Hello Python')
    return answer
