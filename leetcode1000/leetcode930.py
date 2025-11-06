from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        left1 = left2 = 0
        sum1 = sum2 = 0
        ans = 0
        for r, num in enumerate(nums):
            sum1 += num
            sum2 += num
            # 计算 sum >= k
            while left1 <= r and sum1 >= goal:
                sum1 -= nums[left1]
                left1 += 1
            # 计算 sum >= k + 1
            while left2 <= r and sum2 >= goal+1:
                sum2 -= nums[left2]
                left2 += 1
            ans += (left1 - left2)
        return ans