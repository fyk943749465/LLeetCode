from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        numMap = {}
        subMap = {}
        ans = left = 0
        for i, num in enumerate(nums):
            numMap[num] = 0
        for i, num in enumerate(nums):
            if num in subMap:
                subMap[num] += 1
            else:
                subMap[num] = 1
            while len(numMap) == len(subMap):
                ans += len(nums) - i
                if subMap[nums[left]] == 1:
                    subMap.pop(nums[left])
                else:
                    subMap[nums[left]] -= 1
                left += 1
        return ans

if __name__ == '__main__':
    so = Solution()
    x = so.countCompleteSubarrays([5,5,5,5])
    print(x)