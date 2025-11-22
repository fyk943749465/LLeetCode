from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        d = defaultdict(int)
        i = 0
        while i < len(s):
            start = i
            i += 1
            # python 中的取模运算，取决于除数的符号
            while i < len(s) and (ord(s[i]) - ord(s[i-1]))%26 == 1:
                i += 1
            for j in range(start, i):
                c = s[j]
                d[c] = max(d[c], i - j)
        return sum(d.values())

if __name__ == '__main__':
    print(-1%3)
    sol = Solution()
    sol.findSubstringInWraproundString("abcdzabcde")