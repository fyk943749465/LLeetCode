from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        k = len(p)
        ans = []
        cntP = {}
        cntS = {}
        for c in p:
            if c in cntP:
                cntP[c] += 1
            else:
                cntP[c] = 1
        for i, c in enumerate(s):
            if c in cntS:
                cntS[c] += 1
            else:
                cntS[c] = 1
            if i - k + 1 >= 0:
                flag = False
                for k1, v1 in cntS.items():
                    if k1 not in cntP or v1 != cntP[k1]:
                        flag = True
                        break
                if not flag:
                    ans.append(i-k+1)
                if cntS[s[i-k+1]] == 1:
                    cntS.pop(s[i-k+1])
                else:
                    cntS[s[i-k+1]] -= 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.findAnagrams("abab", "ab")
    print(x)
