from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        binMap = {}
        ans = start = 0
        for i, c in enumerate(nums):
            if c not in binMap:
                binMap[c] = 1
            else:
                binMap[c] += 1
            while len(binMap) > 0 and 0 in binMap and binMap[0] > 1:
                if binMap[nums[start]] == 1:
                    binMap.pop(nums[start])
                else:
                    binMap[nums[start]] -= 1
                start += 1

            ans = max(ans, i - start)
        return ans
