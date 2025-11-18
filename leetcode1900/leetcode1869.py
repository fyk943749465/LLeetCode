class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ans0 = ans1 = 0

        i = 0
        for j, v in enumerate(s):
            if s[j] != s[i]:
                i = j
            if s[j] == '0':
                ans0 = max(ans0, j - i + 1)
            if s[j] == '1':
                ans1 = max(ans1, j - i + 1)
            j += 1
        return ans1 > ans0

if __name__ == '__main__':
    s = Solution()
    x = s.checkZeroOnes('1101')
    print(x)