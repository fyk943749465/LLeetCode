from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        max_element = max(nums)
        ans = left = curr = 0
        for i, v in enumerate(nums):
            if v == max_element:
                curr += 1
            while curr >= k:
                ans += len(nums)- i  # 越长越合法
                if nums[left] == max_element:
                    curr -= 1
                left += 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.countSubarrays([1,4,2,1], 3)
    print(x)