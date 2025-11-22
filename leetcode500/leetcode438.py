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

    def findAnagrams2(self, s: str, p: str) -> List[int]:

        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []
        ans = []
        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1
        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)

        for i in range(s_len - p_len):
            if count[ord(s[i]) - 97] == 1:
                differ -= 1
            elif count[ord(s[i]) - 97] == 0:
                differ += 1
            count[ord(s[i]) - 97] -= 1

            if count[ord(s[i+p_len]) - 97] == -1:  # 不同变为相同了
                differ -= 1
            elif count[ord(s[i+p_len]) - 97] == 0:
                differ += 1
            count[ord(s[i+p_len]) - 97] += 1

            if differ == 0:
                ans.append(i+1)
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.findAnagrams("abab", "ab")
    print(x)
