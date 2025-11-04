from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        s = sum(nums)
        ans = -1
        currT = left = 0
        for i, n in enumerate(nums):
            currT += n
            while currT > s - x and left <= i:
                currT -= nums[left]
                left += 1
            if currT == s - x:
                ans = max(ans, i - left + 1)

        return len(nums) - ans if ans != -1 else ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.minOperations(nums=[8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], x=134365)
    print(x)