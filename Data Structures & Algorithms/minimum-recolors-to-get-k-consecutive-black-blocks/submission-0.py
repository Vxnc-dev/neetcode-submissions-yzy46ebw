class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = k+1
        count = 0
        l, r = 0, k-1
        while r < len(blocks):
            for i in range(l, r+1):
                if blocks[i] == "W":
                    count += 1
            if count < res:
                res = count
            count = 0
            r += 1
            l += 1
        return res