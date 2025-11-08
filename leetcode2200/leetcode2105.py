from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:

        left, right = 0, len(plants)-1
        x, y = capacityA, capacityB
        ans = 0
        while left < right:
            if x >= plants[left]:
                x -= plants[left]
            else:
                x = capacityA
                x -= plants[left]
                ans += 1
            left += 1
            if y >= plants[right]:
                y -= plants[right]
            else:
                y = capacityB
                y -= plants[right]
                ans += 1
            right -= 1
        if left == right:
            if x < plants[left] and y < plants[left]:
                ans += 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.minimumRefill([2,2,3,3], 5, 5)
    print(x)
