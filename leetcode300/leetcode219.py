from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        h = {}
        j = 0
        for i, v in enumerate(nums):
            if v in h:
                h[v] += 1
            else:
                h[v] = 1
            if i - j > k:
                if h[nums[j]] > 1:
                    h[nums[j]] -= 1
                else:
                    h.pop(nums[j])
                j += 1
            if h[v] > 1:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    x = sol.containsNearbyDuplicate([1,0,1,1], 1)
    print(x)
