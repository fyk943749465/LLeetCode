from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        num_hash = {}
        for i, v in enumerate(nums):
            if v not in num_hash:
                num_hash[v] = 1

        while original in num_hash:
            original *= 2
        return original

    def findFinalValue2(self, nums: List[int], original: int) -> int:

        num = set(nums)
        while original in num:
            original *= 2
        return original
