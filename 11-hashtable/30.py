# sliding window
# Time complexity - O(n)
# Space complexity - O(min(m+n))
def solve(s):
	left, right, max_length = 0, 0, 0
	seen = set()

	while right < len(s):
		if s[right] not in seen:
			seen.add(s[right])
			right += 1
			max_length = max(max_length, len(seen))
		else:
			seen.remove(s[left])
			left += 1

	return max_length


print(solve("abcabcbb"))
print(solve("bbbbb"))
print(solve("pwwkew"))
