from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque(progresses)
    q_speed = deque(speeds)
    while q:
        while q[0] < 100:
            for i in range(len(q)):
                q[i] += q_speed[i]
        cnt = 0
        while q and q[0] >= 100:
            q.popleft()
            q_speed.popleft()
            cnt += 1
        answer.append(cnt)
    return answer
