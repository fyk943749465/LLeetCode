from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        nums.sort()
        left, right = 0, len(nums) - 1
        ans = 0
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                ans += (right - left)
                left += 1
            else:
                right -= 1
        return ans
