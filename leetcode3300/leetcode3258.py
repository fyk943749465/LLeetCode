class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        zeroCnt = oneCnt = 0
        ans = left = 0
        for i, c in enumerate(s):
            if c == '0':
                zeroCnt += 1
            else:
                oneCnt += 1
            while oneCnt > k and zeroCnt > k:
                if s[left] == '0':
                    zeroCnt -= 1
                else:
                    oneCnt -= 1
                left += 1
            ans += i - left + 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.countKConstraintSubstrings("10101", 1)
    print(x)
