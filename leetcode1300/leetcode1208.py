class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        maxLen = 0
        left = currCost = 0
        for i, c in enumerate(s):
            currCost += abs(ord(c) - ord(t[i]))
            while currCost > maxCost:
                currCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            maxLen = max(maxLen, i - left + 1)
        return maxLen

if __name__ == '__main__':
    sol = Solution()
    x = sol.equalSubstring("abcd", "bcdf", 3)
    print(x)
