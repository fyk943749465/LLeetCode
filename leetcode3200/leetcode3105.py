from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        flag = True
        ans = 1
        result = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if flag:
                    result = 2
                    flag = False
                else:
                    result += 1
            else:
                flag = True
            ans = max(ans, result)

        flag = False
        result = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if flag:
                    result = 2
                    flag = False
                else:
                    result += 1
            else:
                flag = True
            ans = max(ans, result)
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.longestMonotonicSubarray([1,4,3,3,2])
    print(x)