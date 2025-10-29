class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = cnt = 0
        for i, c in enumerate(s):
            if c in "aeiou":
                cnt += 1
            left = i - k  + 1
            ans = max(ans, cnt)
            if left < 0:
                continue
            if s[left] in "aeiou":
                cnt -= 1
        return ans

if __name__ == '__main__':
    s = "abciiidef"
    k = 3
    solution = Solution()
    print(solution.maxVowels(s, k))
