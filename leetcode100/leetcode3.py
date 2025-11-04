class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpMap = {}
        ans = 0
        start = 0
        for i, c in enumerate(s):
            if c not in alpMap:
                alpMap[c] = 1
            else:
                alpMap[c] += 1
            while len(alpMap) < i - start + 1 and len(alpMap) > 0:
                if alpMap[s[start]] == 1:
                    alpMap.pop(s[start])
                else:
                    alpMap[s[start]] -= 1
                start += 1
            if ans < len(alpMap):
                ans = len(alpMap)
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.lengthOfLongestSubstring("pwwkew")
    print(x)