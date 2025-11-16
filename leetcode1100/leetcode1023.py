from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        def isMatch(s1: str, s2: str) -> bool:
            i, j = 0, 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    if s2[j].isupper():
                        return False
                    j += 1
            if i < len(s1):
                return False
            while j < len(s2):
                if s2[j].isupper():
                    return False
                j += 1
            return True

        answer = []
        for s2 in queries:
            answer.append(isMatch(pattern, s2))
        return answer

if __name__ == '__main__':
    sol = Solution()
    x = sol.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB")
    print(x)