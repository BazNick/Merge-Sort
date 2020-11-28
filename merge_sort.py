import random

my_array = [0] * 100

for number in range(len(my_array)):
    my_array[number] = random.randint(1, 1000)


def merge_sort(array):
    if len(array) > 1:
        mid = (len(array)) // 2
        left_array = array[:mid]
        right_array = array[mid:]
        merge_sort(left_array)
        merge_sort(right_array)
        merge(array, left_array, right_array)


def merge(temp_array, left, right):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp_array[k] = left[i]
            i += 1
            k += 1
        else:
            temp_array[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        temp_array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        temp_array[k] = right[j]
        j += 1
        k += 1


merge_sort(my_array)

print(my_array)
