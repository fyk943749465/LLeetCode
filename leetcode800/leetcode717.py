from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        i = 0
        while i < len(bits):
            if bits[i] != 0:
                if i == len(bits) - 2:
                    return False
                i += 1
            i += 1
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isOneBitCharacter([1,1,0]))
