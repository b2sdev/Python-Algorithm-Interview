def solve(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    intersection = set1.intersection(set2)

    return list(intersection)

print(solve([1, 2, 2, 1], [2, 2]))
print(solve([4, 9, 5], [9, 4, 9, 8, 4]))
