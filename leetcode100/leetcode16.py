from cmath import inf
from dis import code_info
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)
        min_diff = inf
        for i in range(n-2):
            # if i > 0 and nums[i] == nums[i - 1]:
            #     continue
            # s = nums[i] + nums[i+1] + nums[i+2]
            # if s > target:
            #     if s - target < min_diff:
            #         ans = s
            #     break
            #
            # s = nums[i] + nums[-2] + nums[-1]
            # if s < target:
            #     if target - s < min_diff:
            #         min_diff = target-s
            #         ans = s
            #     continue
            j, k = i + 1, n -1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                if s > target:
                    if s - target < min_diff:
                        min_diff = s - target
                        ans = s
                    k -= 1
                else:
                    if target - s < min_diff:
                        min_diff = target - s
                        ans = s
                    j += 1
        return ans
    def threeSumClosest2(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = inf
        for i in range(n-2):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                if s > target:
                    if s - target < min_diff:
                        min_diff = s - target
                        ans = s
                    k -= 1
                else:
                    if target - s < min_diff:
                        min_diff = target - s
                        ans = s
                    j += 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.threeSumClosest2([2, 5, 6, 7], 16)
    print(x)