from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:

        numMap = {}
        s = 0
        ans = 0
        for i, num in enumerate(nums):
            s += num
            if num in numMap:
                numMap[num] += 1
            else:
                numMap[num] = 1
            # 更新答案
            if i- k + 1 >= 0:
                if len(numMap) >= m:
                    ans = max(ans, s)
                # 离开窗口
                s -= nums[i-k+1]
                if numMap[nums[i-k+1]] == 1:
                    numMap.pop(nums[i-k+1])
                else:
                    numMap[nums[i-k+1]]-=1
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.maxSum([1,1,1,3], 2, 2)
    print(x)