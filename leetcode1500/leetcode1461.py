class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        strMap = {}
        list = []
        for i, c in enumerate(s):
            list.append(c)
            if i - k + 1 >= 0:
                strMap["".join(list)] = 1
                list.pop(0)

        return len(strMap) == pow(2, k)