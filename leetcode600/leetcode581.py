from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        nums2 = sorted(nums)
        left, right = 0, n - 1
        flag1, flag2 = False, False
        while left < right:
            if nums2[left] == nums[left]:
                left += 1
            else:
                flag1 = True
            if nums2[right] == nums[right]:
                right -= 1
            else:
                flag2 = True
            if flag1 and flag2:
                break
        if left >= right:
            return 0
        else:
            return right - left + 1




if __name__ == '__main__':
    sol = Solution()
    x = sol.findUnsortedSubarray([2,10,10,4,8,10,9,9,15])
    print(x)
