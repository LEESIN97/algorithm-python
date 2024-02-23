def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for i, citation in enumerate(citations):
        if i + 1 <= citation:
            answer = i + 1
        else:
            break
    return answer
