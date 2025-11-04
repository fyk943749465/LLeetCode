from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        ans = left = curr = 0
        itemMap = {}
        for i, c in enumerate(nums):
            if c not in itemMap:
                itemMap[c] = 1
            else:
                itemMap[c] += 1
            curr += c
            while len(itemMap) < i - left + 1:
                curr -= nums[left]
                if itemMap[nums[left]] == 1:
                    itemMap.pop(nums[left])
                else:
                    itemMap[nums[left]] -= 1
                left += 1
            ans = max(ans, curr)
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.maximumUniqueSubarray([4,2,4,5,6])
    print(x)