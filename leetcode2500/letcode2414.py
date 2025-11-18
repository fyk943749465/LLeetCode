class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 0
        i = 0
        for j, v in enumerate(s):
            if ord(s[i]) + (j-i) == ord(s[j]):
                ans = max(ans, j - i + 1)
            else:
                i = j
        return ans