from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:

        numsMap = {}
        ans = []
        for i in range(k):
            if i < len(nums) and nums[i] == key:
                numsMap[i] = key

        for i, c in enumerate(nums):
            if i + k < len(nums) and nums[i + k] == key:
                numsMap[i+k] = key
            if i - k - 1 >= 0 and nums[i-k-1] == key:
                numsMap.pop(i-k-1)
            if len(numsMap) > 0:
                ans.append(i)
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.findKDistantIndices([2,2,2,2,2], 2, 2)
    print(x)