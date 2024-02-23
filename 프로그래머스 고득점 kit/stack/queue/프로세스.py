from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([(i, priority) for i, priority in enumerate(priorities)])
    cnt = 0
    while q:
        now, priority = q.popleft()
        max = 0
        for i in range(len(q)):
            if max < q[i][1]: max = q[i][1]
        if priority < max:
            q.append((now, priority))
        else:
            cnt += 1
            if location == now:
                answer = cnt

    return answer
