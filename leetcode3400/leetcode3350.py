from typing import List
from urllib.request import proxy_bypass


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:

        i, j = 0,1
        ans = []
        while j < len(nums):
            if nums[j] <= nums[j-1]:
                ans.append(j-1 - i + 1)
                i = j
            j += 1
        ans.append(j-i)
        if len(ans) == 1:
            return ans[0]//2
        result = 0
        for i in range(1, len(ans)):
            result = max(result, min(ans[i],ans[i-1]))
            result = max(result, max(ans[i], ans[i-1])//2)
        return result


if __name__ == '__main__':
    sol = Solution()
    x = sol.maxIncreasingSubarrays([-15,19])
    print(x)
