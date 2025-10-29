from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        s = 0
        ans = 0
        numMap = {}
        for i, num in enumerate(nums):
            s += num
            if num in numMap:
                numMap[num] += 1
            else:
                numMap[num] = 1
            if i - k + 1 >= 0:
                if len(numMap) == k:
                    ans = max(ans, s)
                s -= nums[i-k+1]
                if numMap[nums[i-k+1]] == 1:
                    numMap.pop(nums[i-k+1])
                else:
                    numMap[nums[i-k+1]] -= 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    x = sol.maximumSubarraySum([1,5,4,2,9,9,9], 3)
    print(x)