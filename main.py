# Find the second smallest number in a List in Python

def second_smallest(l):
    return sorted(set(l))[1]


print(second_smallest([1, 1, 3, 5, 7]))  # 👉️ 3

print(second_smallest([1, 3, 5, 7]))  # 👉️ 3