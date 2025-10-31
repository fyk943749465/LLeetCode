class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:

        alphMap = {}
        for i, c in enumerate(s):
            if c not in alphMap:
                alphMap[c] = 1
            else :
                alphMap[c] += 1

        freqMap = {}
        for k, v in alphMap.items():
            if v in freqMap:
                freqMap[v] += k
            else:
                freqMap[v] = k

        ansv = 0
        ans = ""

        for k, v in freqMap.items():
            if len(v) > len(ans):
                ansv= k
                ans =v
            elif len(v) == len(ans):
                if k > ansv:
                    ansv = k
                    ans = v
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.majorityFrequencyGroup("abcd")
    print(x)