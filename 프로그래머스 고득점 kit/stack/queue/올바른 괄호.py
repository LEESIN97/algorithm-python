def solution(s):
    answer = True
    arr = list(s)
    stack = []
    for data in arr:
        if data == '(':
            stack.append(data)
        if data == ')':
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    return True
