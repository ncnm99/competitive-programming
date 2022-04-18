for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = []
    for v in s[::-1]:
        ans.append(v)
        if len(ans) >= 3 and ans[-3:] == ["B", "B", "A"]:
            ans.pop(); ans.pop()
    print("".join(ans[::-1]))