from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = list()
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first+ 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                fourth = n - 1
                for third in range(second + 1, n):
                    if third > second + 1 and nums[third] == nums[third - 1]:
                        continue
                    while third < fourth and nums[first] + nums[second] + nums[third] + nums[fourth] > target:
                        fourth -= 1
                    if third == fourth:
                        break
                    if nums[first] + nums[second] + nums[third] + nums[fourth] == target:
                        ans.append([nums[first], nums[second], nums[third], nums[fourth]])
        return ans
