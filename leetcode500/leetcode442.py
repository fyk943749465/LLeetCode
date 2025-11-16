from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            x = (num-1)%n
            nums[x] += n
        ret = [i + 1 for i, num in enumerate(nums) if num > 2 * n]
        return ret
