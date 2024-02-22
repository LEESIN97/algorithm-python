def solution(participant, completion):
    check = dict()
    for person in participant:
        if person in check:
            check[person] += 1
        else:
            check[person] = 1
    for person in completion:
        check[person] -= 1
    for c in check.keys():
        if check[c] != 0:
            answer = c

    return answer
