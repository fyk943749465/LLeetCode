class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        ans = ""
        oneCnt = left = 0
        for i, c in enumerate(s):
            if c == '1':
                oneCnt += 1
            while oneCnt >= k:
                if oneCnt == k:
                    if ans == "":
                        ans = s[left:i+1]
                    else:
                        if len(ans) > len(s[left:i+1]):
                            ans = s[left:i+1]
                        elif len(ans) == len(s[left:i+1]) and ans > s[left:i+1]:
                            ans = s[left:i+1]
                if s[left] == '1':
                    oneCnt -= 1
                left += 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.shortestBeautifulSubstring("000", 1)
    print(x)