from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        i, j = 0, 0
        ans = []
        while i < len(s):
            if j < len(spaces) and i < spaces[j]:
                ans.append(s[i])
            elif j < len(spaces) and i == spaces[j]:
                ans.append(" ")
                ans.append(s[i])
                j += 1
            else:
                ans.append(s[i])
            i += 1
        return "".join(ans)

if __name__ == '__main__':
    s = Solution()
    x = s.addSpaces('LeetcodeHelpsMeLearn', [8, 13, 15])
    print(x)
