def countdown(max):
    newList = []
    for i in range(max, -1, -1):
        newList.append(i)
    return newList


def print_and_return(array):
    print(array[0])
    return array[1]


def first_plus_length(array):
    return array[0] + len(array)


def values_greater_than_second(array):
    if len(array) < 2:
        return False
    new_array = []
    for item in array:
        if item > array[1]:
            new_array.append(item)
    print(len(new_array))
    return new_array


def this_length_that_value(size, value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list

print(print_and_return([5, 7]))
print(first_plus_length([7, 5, 9]))
print(values_greater_than_second([5, 2, 8, 7, 1, 13, -4]))
print(values_greater_than_second([7, 4]))
print(values_greater_than_second([1, 5]))
print(values_greater_than_second([1]))
print(this_length_that_value(4, 7))
