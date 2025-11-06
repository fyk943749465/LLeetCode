from typing import List

from sortedcontainers import SortedList
from unionfind.UnionFind import UnionFind

# SortedList 为 python 中的有序列表，但是不属于标准库中的
# 需要 pip install sortedcontainers
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c+1)
        for u,v in connections:
            uf.union(u, v)
        st = [SortedList() for _ in range(c+1)]
        for i in range(1, c + 1):
            st[uf.find(i)].add(i)
        ans = []
        for a, x in queries:
            root = uf.find(x)
            if a == 1:
                if x in st[root]:
                    ans.append(x)
                elif len(st[root]):
                    ans.append(st[root][0]) # 最小的元素
                else:
                    ans.append(-1)
            else:
                st[root].discard(x) # 将 x 从有序集合中删除
        return ans

