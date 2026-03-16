def chunked(s: list[str]) -> list[list[str]]:
    res = [[]]
    for i in range(1, len(s)):
        for j in range(len(s) - (i - 1)):
            res.append(s[j: j + i])
    res.append(s)
    return res

s = input().split()
print(chunked(s))