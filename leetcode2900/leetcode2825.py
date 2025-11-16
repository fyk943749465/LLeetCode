class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        i = j = 0
        while i < len(str1) and j < len(str2):
            idx1 = ord(str1[i]) - ord('a')
            idx2 = ord(str2[j]) - ord('a')
            if str1[i] == str2[j]:
                i+= 1
                j+= 1
            elif (idx1 + 1)%26 == idx2:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(str2)


if __name__ == '__main__':
    sol = Solution()
    x = sol.canMakeSubsequence("zc", "ad")
    print(x)