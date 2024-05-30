from collections import deque

# Time complexity: O(n)
# Space complexity: O(k)
def solve(nums, k):
    result = []
    window = deque()

    for i in range(len(nums)):
        # 윈도우가 이동했으므로 가장 오랜된 값을 제거
        while window and nums[i - k] == window[0]:
            window.popleft()

        # 현재 값보다 작은 값을 제거
        # -> 덱의 맨 앞에는 현재 윈도우의 최대값의 인덱스가 보장됨
        while window and nums[i] > window[-1]:
            window.pop() 

        # 현재 값을 덱에 추가
        window.append(nums[i])

        # 현재 윈도우의 최대값을 기록
        if i >= k - 1:
            result.append(window[0])

    return result

print(solve([1, 3, -1, -3, 5, 3, 6, 7], 3))
