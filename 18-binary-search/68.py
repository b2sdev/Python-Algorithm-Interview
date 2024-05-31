# Time complexity: O(n)
# Space complexity: O(1)
def solve(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

print(solve([2, 7, 11, 15], 9))
