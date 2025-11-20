from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        i, j = 0, 1
        flip = 1
        ans = 0
        while j < len(nums):
            if nums[j] - nums[j-1] == flip:
                flip = - flip
                ans = max(ans, j - i + 1)
            else:
                i = j -1
                flip = 1
                if nums[j] - nums[j - 1] == flip:
                    flip = - flip
                    ans = max(ans, j - i + 1)
                    i = j - 1
                else:
                    i = j
            j += 1
        return ans if ans > 0 else -1

if __name__ == '__main__':
    s = Solution()
    x = s.alternatingSubarray([1,29,30,5])
    print(x)