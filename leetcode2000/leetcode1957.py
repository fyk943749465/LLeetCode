class Solution:
    def makeFancyString(self, s: str) -> str:

        i = 0
        ans = list()
        for j, v in enumerate(s):
            if s[i] != s[j]:
                i = j
            if j - i + 1 <= 2:
                ans.append(v)
        return "".join(ans)