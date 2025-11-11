from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(2, len(nums)):
            if nums[j] != nums[i]:
                nums[j+1] = nums[i]
                j += 1
            elif nums[j] == nums[i] and nums[j-1] != nums[j]:
                nums[j+1] = nums[i]
                j += 1
        return j + 1


if __name__ == '__main__':

    sol = Solution()
    sol.removeDuplicates([1,1,1,2, 2, 3])