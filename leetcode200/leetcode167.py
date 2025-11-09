import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i, v in enumerate(numbers):
            x = target - v
            j = bisect.bisect_right(numbers, x)-1
            if j != i and j < len(numbers) and v + numbers[j] == target:
                return [i +1, j + 1]
        return []

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while True:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1

if __name__ == '__main__':
    sol = Solution()
    x = sol.twoSum([2,7,11,15], 9)
    print(x)