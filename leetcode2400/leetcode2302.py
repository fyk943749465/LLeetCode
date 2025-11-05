from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        ans = curr = left = 0
        for i, v in enumerate(nums):
            curr += v
            while curr * (i - left + 1) >= k:
                curr -= nums[left]
                left += 1
            ans += i - left + 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.countSubarrays([2, 1, 4, 3, 5], 10)
    print(x)
