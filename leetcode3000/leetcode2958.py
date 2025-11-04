from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        numMap = {}
        ans = left = 0
        for i, c in enumerate(nums):
            if c not in numMap:
                numMap[c] = 1
            else:
                numMap[c] += 1
            while numMap[c] > k:
                if numMap[nums[left]] == 1:
                    numMap.pop(nums[left])
                else:
                    numMap[nums[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.maxSubarrayLength([1,2,1,2,1,2,1,2], 1)
    print(x)
