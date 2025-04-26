from collections import deque


def check_matching_parentheses(s):
    stack = deque()
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            else:
                stack.pop()
    return len(stack) == 0
