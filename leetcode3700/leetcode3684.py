from typing import List


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:

        j = 0
        ans = []
        nums.sort(reverse=True)
        for i , num in enumerate(nums):
            if i == 0:
                ans.append(nums[i])
            elif ans[j] != num and j + 1 < k:
                ans.append(nums[i])
                j += 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    sol.maxKDistinct([1,1,1,2,2,2], 6)