from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        ans= []
        for i, v in enumerate(groups):
            if i == 0:
                t = v
                ans.append(i)
                continue
            if v != t:
                ans.append(i)
                t = v
        result = []
        for i in ans:
            result.append(words[i])
        return result