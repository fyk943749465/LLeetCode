from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:

        arr.sort()
        n = len(arr)
        mid = arr[(n-1)//2]

        arr.sort(lambda v : abs(v-mid))
        return arr[:k]
