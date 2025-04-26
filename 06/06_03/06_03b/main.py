from collections import deque

history_stack = deque()

history_stack.append("https://google.com")
history_stack.append("https://example.com")
history_stack.append("https://github.com")


print(history_stack[-1])
print(history_stack.pop())

