from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:
            return 0
        ans = len(nums)
        curr = left = 0
        for i, v in enumerate(nums):
            curr += v
            while curr >= target:
                curr -= nums[left]
                left += 1
                ans = min(ans, i - left + 2)
        return ans


if __name__ == '__main__':
    sol = Solution()
    sol.minSubArrayLen(11, [1, 2, 3, 4, 5])