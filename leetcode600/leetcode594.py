from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        h= {}
        for num in nums:
            if num not in h:
                h[num] = 1
            else:
                h[num] += 1
        ans = 0
        for k, v in h.items():

            if k + 1 in h:
                ans = max(ans, h[k+1] + v)
            if k - 1 in h:
                ans = max(ans, h[k-1] + v)
        return ans

    ## 双指针解法
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        res, begin = 0, 0
        for end in range(len(nums)):
            while nums[end] - nums[begin] > 1:
                begin += 1
            if nums[end] == nums[begin] + 1:
                res = max(res, end - begin + 1)
        return res