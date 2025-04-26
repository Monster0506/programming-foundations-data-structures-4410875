def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None

    return sorted(my_list)[1]


def find_second_smallest_v2(my_list):
    if len(my_list) < 2:
        return None
    smallest = float("inf")
    smallest_2 = float("inf")
    for num in my_list:
        smallest_2 = smallest
        if num < smallest:
            num = smallest
        elif num < smallest_2:
            smallest_2 = num
    return smallest_2


print(find_second_smallest([5, 8, 3, 2, 6]))
print(find_second_smallest_v2([5, 8, 3, 2, 6]))
