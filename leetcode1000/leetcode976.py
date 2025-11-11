from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        ans = 0
        nums.sort()
        for i in range(2, len(nums)):
            if nums[i-2] + nums[i-1] > nums[i]:
                ans = max(ans, nums[i-2] + nums[i-1] + nums[i])
        return ans

    def largestPerimeter2(self, nums: List[int]) -> int:

        ans = 0
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return  nums[i-2] + nums[i-1] + nums[i]
        return ans