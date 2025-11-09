import bisect
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        ans = 0
        nums.sort()
        for j, x in enumerate(nums):
            r = bisect.bisect_right(nums, upper-x, 0, j)
            l = bisect.bisect_left(nums, lower-x, 0, j)
            ans += r - l
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.countFairPairs([0,1,7,4,4,5], 3, 6)
    print(x)