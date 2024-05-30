def solve(nums):
	return sum(sorted(nums)[::2])

print(solve([1, 4, 3, 2]))
