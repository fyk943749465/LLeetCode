from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left, right = 0, len(nums) - 1
        ls = [0] * len(nums)
        j = len(nums) - 1
        while left < right:
            if nums[left]*nums[left] == nums[right]*nums[right]:
                ls[j] = nums[left]*nums[left]
                j -= 1
                ls[j] = nums[right]*nums[right]
                j -= 1
                left += 1
                right -= 1
            elif nums[left]*nums[left] < nums[right]*nums[right]:
                ls[j] = nums[right] * nums[right]
                j -= 1
                right -= 1
            else:
                ls[j] = nums[left] * nums[left]
                j -= 1
                left += 1
        if left == right:
            ls[0] = nums[left] * nums[left]
        return ls

