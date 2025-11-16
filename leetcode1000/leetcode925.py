class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        if len(name) > len(typed):
            return False
        i = j = 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j - 1] == typed[j]:
                j += 1
            else:
                return False
        if i < len(name):
            return False
        a = typed[j - 1]
        while j < len(typed):
            if typed[j] != a:
                return False
            j += 1
        return True

if __name__ == '__main__':
    solution = Solution()
    x = solution.isLongPressedName("pyplrz", "ppyypllr")
    print(x)