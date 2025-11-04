import bisect
from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:

        n = len(nums)
        nums.sort()
        ans = n
        for i, c in enumerate(nums):
            lst = bisect.bisect_right(nums, c*k) - 1
            ans = min(ans, i + n - lst - 1)
        return ans

    # 滑动窗口
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_save = left = 0
        for i, mx in enumerate(nums):
            while nums[left] * k < mx:
                left += 1
            max_save = max(max_save, i - left + 1)
        return len(nums) - max_save

if __name__ == '__main__':
    sol = Solution()
    x = sol.minRemoval([4,6], 2)
    print(x)


