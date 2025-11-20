class Solution:
    def countHomogenous(self, s: str) -> int:

        i = ans = 0
        for j, v in enumerate(s):
            if s[i] != s[j]:
                i = j
            ans += (j-i+1)
            ans %= 1e9+7
        return int(ans)