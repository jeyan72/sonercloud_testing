
def divide_by_zero_bug(a, b):
    result = a / b
    print("Result of division:", result)


def array_index_bug():
    my_list = [1, 2, 3]
    element = my_list[3]  # Accessing index 3, which is out of range
    print("Element at index 3:", element)

divide_by_zero_bug(5, 0)
array_index_bug()


