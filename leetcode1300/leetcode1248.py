from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        left1 = left2 = ans = 0
        odd1 = odd2 = 0
        for r, num in enumerate(nums):
            if num %2 == 1:
                odd1 += 1
                odd2 += 1
            while left1 <= r and odd1 >=k:
                if nums[left1] % 2 == 1:
                    odd1 -= 1
                left1 += 1
            while left2 <= r and odd2 >=k +1:
                if nums[left2] % 2 == 1:
                    odd2 -= 1
                left2 += 1
            ans += (left1 - left2)
        return ans

