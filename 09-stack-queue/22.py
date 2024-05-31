def solve(T):
    # 입력 T는 일별 온도이다.
    # 따라서, T의 index는 날짜를 의미하며,
    # 결과의 값은 인덱스의 차로 정의된다.

    if not T:
        return []

    
    result = [0] * len(T)
    stack = []
 
    for i in range(len(T)):
        # 이전 날짜의 온도가 현재 온도보다 낮은지를 트래킹하며,
        # 현재 날짜와의 이전 날짜의 인덱스의 차이를 계산
        while stack and T[i] > T[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day
        stack.append(i)

    return result

print(solve([73, 74, 75, 71, 69, 72, 76, 73]))
