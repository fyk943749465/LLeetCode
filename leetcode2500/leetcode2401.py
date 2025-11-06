from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        left = 0
        ans = 1
        curr = nums[0]
        for i in range(1, len(nums)):
            # 如果满足添加
            if nums[i] & curr == 0:
                curr |= nums[i]   # 并入集合中
                ans = max(ans, i - left + 1) # 更新答案
            else:
                # 不满足条件
                while left <= i and nums[i] & curr != 0:
                    curr ^= nums[left] # 从集合中减去
                    left += 1  # 左边指针增加
                # 再次判断当前元素与集合中的元素进行 and 操作是否为0
                if nums[i] & curr == 0:
                    curr |= nums[i]   # 将当前元素加入集合中
                    ans = max(ans, i - left + 1)  # 更新答案
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.longestNiceSubarray([3,1,5,11,13])
    print(x)