from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()
        left = curr = 0
        ans = 1
        for i in range(1, len(nums)):

            curr += (i- left) * (nums[i] - nums[i-1])
            while curr > k:
                curr -= nums[i] - nums[left]
                left += 1
            ans = max(ans, i - left + 1)
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.maxFrequency([3, 9, 6], 2)
    print(x)
