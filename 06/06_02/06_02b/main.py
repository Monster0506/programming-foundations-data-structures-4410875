card_stack = []
card_stack.append("JH")
card_stack.append("2D")
card_stack.append("10S")


top_card = card_stack.pop()
print("Top card:", top_card)
top_card = card_stack[-1]
print("Top card:", top_card)

if not card_stack:
    print("The stack is empty")
else:
    print(len(card_stack), "cards in the stack")
