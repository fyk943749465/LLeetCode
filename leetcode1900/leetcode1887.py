from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        nums.sort(reverse=True)
        j = ans = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[j]:
                ans +=  (j+1)
            j = i
        return ans


