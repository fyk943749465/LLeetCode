class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:

        cnt = [0]*26
        ans = left = 0
        for i, c in enumerate(s):
            cnt[ord(c) - ord('a')] += 1
            while cnt[ord(c) - ord('a')] >= k:
                ans += len(s)- i
                cnt[ord(s[left]) - ord('a')] -= 1
                left += 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.numberOfSubstrings("abcde", 1)
    print(x)