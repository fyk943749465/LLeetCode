from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        if k == 1:
            return nums
        n = len(nums)
        ans = [-1]*(n-k+1)
        i,j = 0, 1
        while j < n:
            # 边界条件判断，要注意
            while j<n and nums[j] - nums[j-1] == 1:
                if j - i + 1 == k:
                    ans[i] = nums[j]
                    i += 1
                j += 1
            i = j
            j = j + 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.resultsArray([2, 3], 2))

