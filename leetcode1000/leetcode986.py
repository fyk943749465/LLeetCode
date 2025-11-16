from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        n = len(firstList)
        m = len(secondList)
        i = j = 0
        ans = []
        while i < n and j < m:
            if firstList[i][0] > secondList[j][1]:
                j += 1
            elif firstList[i][1] < secondList[j][0]:
                i += 1
            elif firstList[i][1] <= secondList[j][1] and firstList[i][1] >= secondList[j][0]:
                ans.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
                i += 1
            else:
                ans.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
                j += 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))