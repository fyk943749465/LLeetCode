from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        ans = left = 0
        zeroCnt = 0
        for i, c in enumerate(nums):
            if c == 0:
                zeroCnt += 1
            while zeroCnt > k:
                if nums[left] == 0:
                    zeroCnt -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
    print(x)
