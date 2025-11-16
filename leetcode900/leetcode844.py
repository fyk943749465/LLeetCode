class Solution:
    # 栈的思路
    def backspaceCompare(self, s: str, t: str) -> bool:

        l1 = list()
        l2 = list()
        for i, v in enumerate(s):
            if v == '#':
                if len(l1) > 0:
                    l1.pop()
            else:
                l1.append(v)
        for i, v in enumerate(t):
            if v == '#':
                if len(l2) > 0:
                    l2.pop()
            else:
                l2.append(v)

        return l1 == l2

    # 双指针的思路
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1
        skipS = skipT = 0
        while i >= 0 or j >= 0:
            while i >=0:
                if s[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >=0:
                return False
            i-=1
            j-=1
        return True