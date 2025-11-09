from collections import Counter
from typing import List

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def getTriplets(map1: Counter, map2: Counter) -> int:
            triplets = 0
            for num1, count1 in map1.items():
                square = num1 ** 2
                for num2, count2 in map2.items():
                    if square % num2 == 0:
                        num3 = square // num2
                        if num3 == num2:
                            triplets += count1 * count2 * (count2-1)//2
                        elif num2 < num3 and num3 in map2:
                            triplets += count1 * count2 * map2[num3]
            return triplets

        map1, map2 = Counter(nums1), Counter(nums2)
        return getTriplets(map1, map2) + getTriplets(map2, map1)
if __name__ == '__main__':
    sol = Solution()
    x = sol.numTriplets([1,1], [1,1,1])
    print(x)