from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        i = j = 0
        ans = 0
        while j < len(nums):
            if nums[j] == 0:
                i = j
            while i < j and nums[i] == 0:
                i += 1
            if nums[i] != 0 and nums[j] != 0:
                ans = max(ans, j - i + 1)
            j += 1
        return ans

    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:

        ans = cnt = 0
        for x in nums:
            if x:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans