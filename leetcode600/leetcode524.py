from typing import List


class Solution:
    def findLongestWord(self, T: str, dictionary: List[str]) -> str:

        def isSubsequence(s: str, t: str) -> bool:
            i = j = 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == len(s)

        ans = ""
        for d in dictionary:
            if isSubsequence(d, T):
                if len(d) > len(ans):
                    ans = d
                elif len(d) == len(ans) and d < ans:
                    ans = d
        return ans

if __name__ == '__main__':
    s = Solution()
    x = s.findLongestWord("abpcplea", ["ale","apple","monkey","plea"])
    print(x)