from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        i = j = 0
        ans = 0
        while i < len(nums1) and j < len(nums2):

            if i <= j and nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            elif i <=j :
                i += 1
                j += 1
            else:
                j += 1
        return ans