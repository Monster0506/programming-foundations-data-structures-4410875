set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}

union_set = set_A.union(set_B)
intersection_set = set_A.intersection(set_B)
difference_set = set_A.difference(set_B)
difference_set2 = set_B.difference(set_A)
symmetric_difference = set_A.symmetric_difference(set_B)
symmetric_difference2 = set_A.union(set_B).difference(set_A.intersection(set_B))


print(union_set)
print(intersection_set)
print(difference_set)
print(difference_set2)
print(symmetric_difference)
print(symmetric_difference2)
