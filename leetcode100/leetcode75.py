from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt0 = cnt1 = cnt2 = 0
        for num in nums:
            if num == 0:
                cnt0 += 1
            elif num == 1:
                cnt1 += 1
            else:
                cnt2 += 1

        j = 0
        for i in range(cnt0):
            nums[j] = 0
            j += 1
        for i in range(cnt1):
            nums[j] = 1
            j += 1
        for i in range(cnt2):
            nums[j] = 2
            j += 1

    def sortColors1(self, nums: List[int]) -> None:
        n = len(nums)
        p = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        for i in range(p, n):
            if nums[i] == 1:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

    # p0 指向0末尾+1位置，p1 指向1末尾+1位置
    def sortColors2(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
    def sortColors3(self, nums: List[int]) -> None:
        p0 = p1 = 0
        for i, val in enumerate(nums):
            nums[i] = 2
            if val <= 1:
                nums[p1] = 1
                p1 += 1
            if val == 0:
                nums[p0] = 0
                p0 += 1


if __name__ == '__main__':
    solution = Solution()
    solution.sortColors2([0,1,2,1,2,1,0])
