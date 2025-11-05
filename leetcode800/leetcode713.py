from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        m = 1
        ans = left = 0
        for i, v in enumerate(nums):
            m *= v
            while m >= k and left <= i:
                m /= nums[left]
                left += 1
            ans += i - left + 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
    print(x)