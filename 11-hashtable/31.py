from collections import Counter

def solve(nums, k):
    freq = Counter(nums)   
    sorted_freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
    return [x[0] for x in sorted_freq[:k]]

print(solve([1, 1, 1, 2, 2, 3], 2))
