class Solution:
    def maxPower(self, s: str) -> int:

        i = 0
        ans = 0
        for j, v in enumerate(s):
            if s[j] != s[i]:
                i = j
            ans = max(ans, j - i + 1)
            j += 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.maxPower("abbcccddddeeeeedcba")
    print(x)