import re
from typing import List


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        # 同向双指针
        def expand(s: str, t: str) -> bool:
            i = j = 0
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    return False
                ch = s[i]
                cnti = 0
                while i < len(s) and s[i] == ch:
                    cnti += 1
                    i += 1
                cntj = 0
                while j < len(t) and t[j] == ch:
                    cntj += 1
                    j += 1

                if cnti < cntj:
                    return False
                if cnti != cntj and cnti < 3:
                    return False
            return i == len(s) and j == len(t)

        return sum(int(expand(S, word)) for word in words)


if __name__ == '__main__':
    s = Solution()
    x = s.expressiveWords("lee", ["le"])
    print(x)
