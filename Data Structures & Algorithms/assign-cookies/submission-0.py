class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        pg, ps = 0, 0
        happy = 0
        while ps < len(s) and pg < len(g):
            if s[ps] >= g[pg]:
                happy += 1
                ps += 1
                pg += 1
            else:
                ps += 1
        return happy