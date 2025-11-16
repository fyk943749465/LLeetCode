from typing import List


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:

        staple.sort()
        drinks.sort(reverse=True)
        i, j = 0, 0
        result = 0
        while i < len(staple) and j < len(drinks):
            if staple[i] > x:
                break
            elif staple[i] + drinks[j] <= x:
                result += len(drinks) - j
                result %= (1e9 + 7)
                i += 1
            else:
                j += 1
        return result