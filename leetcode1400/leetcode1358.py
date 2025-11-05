class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        a = b = c = 0
        ans = left = 0
        for i, v in enumerate(s):
            if v == 'a':
                a += 1
            elif v == 'b':
                b += 1
            else:
                c += 1
            while a >=1 and b >=1 and c >=1:
                if s[left] == 'a':
                    a -= 1
                elif s[left] == 'b':
                    b -= 1
                else:
                    c -= 1
                left += 1
            ans += left
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.numberOfSubstrings('abcabc')
    print(x)
