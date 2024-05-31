def solve(s, k):
    if not s:
        return 0

    left, right = 0, 0
    max_count = 0
    max_length = 0
    char_count = {} # 현재 윈도우의 카운트

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        max_count = max(max_count, char_count[s[right]])
        # (현재 윈도우 크기 - 최대 문자 개수)가 k보다 크다는 것은
        # k개 이상의 문자를 변경해야 함
        # 따라서, 윈도우를 이동시키고 현재 윈도우의 카운트를 초기화
        while right - left + 1 - max_count > k:
            char_count[s[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)

    return max_length

print(solve("AAABBC", 2))
