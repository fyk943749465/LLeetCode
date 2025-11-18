from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        preOne = -1
        for j, v in enumerate(nums):
            if preOne != -1 and v == 1:
                t = j - preOne -1
                if t < k:
                    return False
            if v == 1:
                preOne = j
        return True