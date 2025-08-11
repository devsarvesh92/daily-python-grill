def search_rotated_array(*, nums: list[int], target: int) -> int:

    left, right = 0, len(nums) - 1

    while left < right:
        middle = (left + right) // 2

        if nums[middle] == target:
            return middle

        if nums[left] < nums[middle]:
            # left half is sorted
            if nums[left] <= target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        elif nums[right] > nums[middle]:
            # right half is sorted
            if nums[middle] <= target < nums[right]:
                left = middle + 1
            else:
                right = middle - 1

    return -1
