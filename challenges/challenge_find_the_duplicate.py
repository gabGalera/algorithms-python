def find_duplicate(nums):
    if not nums or len(nums) < 2:
        return False

    merge_sort(nums)
    for index in range(0, len(nums)):
        position = index + 1
        end = len(nums)
        target = nums[position:end]
        if type(nums[index]) is str or nums[index] < 0:
            return False
        search = single_search(target, nums[index])
        if search != -1 and search is not None:
            return search

    return False


def merge_sort(nums, start=0, end=None):
    if end is None:
        end = len(nums)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(nums, start, mid)
        merge_sort(nums, mid, end)
        merge(nums, start, mid, end)


def merge(nums, start, mid, end):
    left = nums[start:mid]
    right = nums[mid:end]

    left_index, right_index = 0, 0

    for index in range(start, end):
        if left_index >= len(left):
            nums[index] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            nums[index] = left[left_index]
            left_index + 1
        elif left[left_index] < right[right_index]:
            nums[index] = left[left_index]
            left_index += 1
        else:
            nums[index] = right[right_index]
            right_index += 1


def single_search(nums, target):
    if nums and nums[0] == target:
        return nums[0]
    else:
        return -1


test = [1, 2]

print(find_duplicate(test))
