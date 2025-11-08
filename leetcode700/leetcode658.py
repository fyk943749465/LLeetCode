import bisect
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key = lambda v : abs(v-x)) # 对数组中的每个元素，按照其与 x 的距离排序
        return sorted(arr[:k])              # 取前k个元素，并且排序

    def findClosestElements2(self, arr: List[int], k: int, x: int) -> List[int]:
        right = bisect.bisect_left(arr, x) # <= X 的坐标
        left = right - 1
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr) or x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left+1:right]

if __name__ == '__main__':
    sol = Solution()
    sol.findClosestElements([1,2,3,4,5], 4, 3)