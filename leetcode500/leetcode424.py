class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        cnt = {}
        left = 0
        ans = 1
        for i, c in enumerate(s):
            if c not in cnt:
                cnt[c] = 1
            else:
                cnt[c] += 1
            maxCnt = 0
            for x, v in cnt.items():
                maxCnt = max(maxCnt, v)
            while i - left + 1 - maxCnt > k:
                if cnt[s[left]] == 1:
                    cnt.pop(s[left])
                else:
                    cnt[s[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.characterReplacement("ABAB", 2)
    print(x)