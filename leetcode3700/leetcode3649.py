from typing import List


class Solution:

    # 这个题目，要掌握数学推导过程
    def perfectPairs(self, nums: List[int]) -> int:

        nums.sort(key=lambda x: abs(x))
        ans = left = 0
        for j, b in enumerate(nums):
            while abs(nums[left]) * 2 < abs(b):
                left += 1
            ans += j - left
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.perfectPairs([0, 1, 2 ,3])
    print(x)