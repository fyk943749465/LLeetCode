class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        cnt = 0
        for i in s:
            cnt += (ord(i) - ord('0'))
        j = 0
        ans = cnt
        while j < len(s):
            start = j
            if s[j] == '0':
                flag1 = flag2 = flag3 = False
                # 连续0
                while j < len(s) and s[j] == '0':
                    flag1 = True
                    j += 1
                x = 0
                # 连续1
                while j < len(s) and s[j] == '1':
                    flag2 = True
                    x += 1
                    j += 1
                k = j
                # 连续0
                while k < len(s) and s[k] == '0':
                    flag3 = True
                    k += 1
                if flag1 and flag2 and flag3:
                    ans = max(ans, cnt + k - start - x)
            else:
                j += 1
        return ans

