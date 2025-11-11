import collections
from typing import List


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:

        MOD = 10**9 + 7
        ans = 0
        A.sort()
        for i, x in enumerate(A):
            T = target - x
            j, k = i + 1, len(A) - 1
            while j < k:
                if A[j] + A[k] < T:
                    j += 1
                elif A[j] + A[k] > T:
                    k -= 1
                elif A[j] != A[k]:
                    left = right = 1
                    while j + 1 < k and A[j] == A[j + 1]:
                        left += 1
                        j += 1
                    while k-1 > j and A[k] == A[k - 1]:
                        right += 1
                        k -= 1
                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1
                else:
                    ans += (k-j+1)*(k-j)/2
                    ans %= MOD
                    break
        return ans

    # 三数之和的多重计数版本
    # 组合计数 + 哈希 + 模运算
    def threeSumMulti2(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = collections.Counter(arr)
        nums = sorted(count)
        res = 0
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i:], i):
                c = target - a - b
                if c not in count:
                    continue
                if a == b == c:
                    res += count[a] * (count[a]-1) * (count[a]-2) // 6
                elif a == b != c:
                    res += count[a] * (count[a]-1) // 2 * count[c]
                elif a < b and b < c:
                    res += count[a] * count[b] * count[c]
        return res % MOD

if __name__ == '__main__':
    sol = Solution()
    sol.threeSumMulti2([1,1,2,2,3,3,4,4,5,5], 8)
