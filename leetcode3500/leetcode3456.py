class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:

        i = 0
        for j, v in enumerate(s):
            if s[i] != s[j]:
                i = j
            if j == len(s)-1 and j -i + 1 == k or j < len(s)-1 and j - i + 1 == k and s[j+1] != s[j]:
                return True
        return False
