primary_colors = frozenset(["red", "blue", "yellow"])


if "blue" in primary_colors:
    print("Blue in the set!")

# This will raise an error because frozenset is immutable
# primary_colors.add("green")
