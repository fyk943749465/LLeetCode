from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:

        left = flip = ans = 0
        for i in range(len(nums)):
            if nums[i]%2 == flip:
                if nums[i] <= threshold:
                    flip = (flip + 1) % 2
                else:
                    flip = 0
                    left = i + 1
            else:
                if nums[i] % 2 == 0 and nums[i] <= threshold:
                    left = i
                else:
                    left = i + 1
                    flip = 0
            ans = max(ans, i - left + 1)
        return ans

if __name__ == '__main__':
    s = Solution()
    x = s.longestAlternatingSubarray([4,10,3], 10)
    print(x)
