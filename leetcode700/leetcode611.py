from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)
        ans = 0
        for k in range(2, n):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans

    def triangleNumber2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                if nums[k] - nums[j] < nums[i]:
                    ans += k - j
                    j += 1
                else:
                    k -= 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.triangleNumber2([1,2,3,4,5,6])
    print(x)