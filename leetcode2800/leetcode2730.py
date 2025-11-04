class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        cnt = 0
        ans = left = 0
        for i, c in enumerate(s):
            if i > 0 and s[i-1] == s[i]:
                cnt += 1
            while cnt > 1:
                if s[left] == s[left+1]:
                    cnt -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.longestSemiRepetitiveSubstring("4411794")
    print(x)

