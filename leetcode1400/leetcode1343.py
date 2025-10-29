from typing import List
#from _ast import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum = 0
        cnt = 0
        for i, v in enumerate(arr):
            sum += v
            if i  + 1 - k >= 0:
                if sum/k >= threshold:
                    cnt += 1
                sum -= arr[i+1-k]
        return cnt
if __name__ == '__main__':

    s = Solution()
    x = s.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4)
    print(x)