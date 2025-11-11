from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        def isAnagram(s1: str, s2: str):
            if len(s1) != len(s2):
                return False
            count = [0] * 26
            for c1, c2 in zip(s1, s2):
                count[ord(c1)-ord('a')] += 1
                count[ord(c2)-ord('a')] -= 1
            return all(c == 0 for c in count)

        j = 0
        ans = []
        for i, w in enumerate(words):
            if i == 0:
                ans.append(w)
            elif not isAnagram(ans[j], w):
                ans.append(w)
                j += 1

        return ans

if __name__ == '__main__':
    sol = Solution()
    sol.removeAnagrams(["abba","baba","bbaa","cd","cd"])