def solve(s):
    if not s:
        return ""

    last_index = {char: i for i, char in enumerate(s)}

    print(last_index)

    result = []
    stack = []

    for i, char in enumerate(s):
        # 스택에 쌓여 있는 문자(stack[-1])가 현재 문자(char)보다 크고, 뒤에 다시 붙일 문자가 있으면,
        # 쌓아둔 문자를 없앤다.
        while stack and char < stack[-1] and last_index[stack[-1]] > i: # and stack[-1] in s[i:]:
            stack.pop()

        if char not in stack:
            stack.append(char)
            result.append(char)

    return "".join(result)

print(solve("bcabc"))
print(solve("cbacdcbc"))
