# Time complexity: O(|s|+|t|)
# Space complexity: O(|t|)
def solve(s, t):
    t_freq = {}
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1

    left, right = 0, 0 # 윈도우의 투 포인터
    # 최소 윈도우를 `s[min_start:min_start + min_length]`의 형태로 리턴
    # 따라서, 모든 문자를 찾을 때마다 아래의 상태를 업데이트
    min_start = 0 # 최소 윈도우의 시작 인덱스
    min_length = float('inf') # 최소 윈도우의 크기
    # 문자열 t의 길이로 필요한 문자의 전체 개수
    # 윈도우 내에 포함된 문자의 개수를 추적하기 위해 사용
    count = len(t)

    while right < len(s):
        # left 인덱스를 고정한 상태에서 윈도우 안에
        # 모든 문자가 포함될 때까지 right 인덱스를 증가
        if s[right] in t_freq:
            t_freq[s[right]] -= 1
            if t_freq[s[right]] >= 0:
                count -= 1

        # 모든 문자를 찾았으므로, 상태(min_strt, min_length)를 
        # 업데이트하고 윈도우를 초기화
        while count == 0:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_start = left

            # left 인덱스를 다음 문자의 위치로 옮김
            if s[left] in t_freq:
                t_freq[s[left]] += 1
                if t_freq[s[left]] > 0:
                    count += 1
            left += 1

        right += 1

    return s[min_start:min_start + min_length] if min_length != float('inf') else ""

print(solve("ADOBECODEBANC", "ABC"))
