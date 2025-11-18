class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        ans = 0
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                a ,b = s[i], s[i+1]
                left = right = 0
                j = i
                while j >=0 and s[j] == a:
                    left += 1
                    j -= 1
                j = i + 1
                while j < len(s) and s[j] == b:
                    right += 1
                    j += 1
                ans += min(left, right)
        return ans




if __name__ == '__main__':
    sol = Solution()
    x = sol.countBinarySubstrings("00110")
    print(x)