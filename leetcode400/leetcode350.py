import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()
        i = j = 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans

    def intersec2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = collections.Counter()
        for num in nums1:
            m[num] += 1

        intersect = list()
        for num in nums2:
            if (count := m.get(num, 0)) > 0:
                intersect.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)
        return intersect


if __name__ == '__main__':
    sol = Solution()
    x = sol.intersect([1,2,2,1], [2,2])
    print(x)
