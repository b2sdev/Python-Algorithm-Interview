# Time complexity: O(m + n)
# Space complexity: O(m)
def solve(jewels, stones):
	jewel_set = set(jewels)

	count = 0
	for stone in stones:
		if stone in jewel_sets:
			count += 1
	
	return count

print(solve("aA", "aAAbbbb"))
