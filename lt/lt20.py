from collections import deque

p = "(()())("

def isvalid(p):
    stack = deque()
    pairs = 0

    for par_ in p:
        if par_ == "(":
            stack.append(par_)
        elif par_ == ")":
            if stack:
                stack.pop()
            else:
                return False

    return not stack


print(isvalid(p))



