from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        n = len(arr)
        top = 0
        i = -1
        # 这里 top 最多到 n + 1， 如果top 在n+1的位置，那么最后一个元素一定是0
        while top < n:
            i += 1      # i 记录了实际放置的元素
            top += 1 if arr[i] else 2
        j = n - 1
        if top == n + 1:
            arr[j] = 0
            j -= 1
            i -= 1
        while j >= 0:
            arr[j] = arr[i]
            j -= 1
            if arr[i] == 0:
                arr[j] = arr[i]
                j -= 1
            i -= 1



if __name__ == '__main__':
    sol = Solution()
    sol.duplicateZeros([8,4,5,0,0,0,0,7])