def is_anagram(first_string, second_string):
    pali1 = list(first_string.lower())
    merge_sort(pali1)
    pali2 = list(second_string.lower())
    merge_sort(pali2)
    isEqual = pali1 == pali2
    if not first_string or not second_string:
        isEqual = False
    return ("".join(pali1), "".join(pali2), isEqual)


def merge_sort(string, low_index=0, high_index=None):
    if high_index is None:
        high_index = len(string)

    if (high_index - low_index) > 1:
        mid = (high_index + low_index) // 2
        merge_sort(string, low_index, mid)
        merge_sort(string, mid, high_index)
        merge(string, low_index, mid, high_index)


def merge(payload, low_index, mid, high_index):
    left = payload[low_index:mid]
    right = payload[mid:high_index]

    left_index, right_index = 0, 0

    for index in range(low_index, high_index):
        if left_index >= len(left):
            payload[index] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            payload[index] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            payload[index] = left[left_index]
            left_index += 1
        else:
            payload[index] = right[right_index]
            right_index += 1


print(is_anagram("", ""))
