def find_duplicate(nums):
    if not nums or len(nums) < 2:
        return False

    end = len(nums) - 1
    nums.sort()
    for index in range(0, end):
        position = index
        nextPosition = position + 1
        if type(nums[index]) is str or nums[index] < 0:
            return False
        search = nums[position] == nums[nextPosition]
        if search:
            return nums[position]

    return False
