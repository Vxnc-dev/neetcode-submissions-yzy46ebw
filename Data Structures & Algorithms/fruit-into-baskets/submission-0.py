class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, res = 0, 0
        count = {}
        total = 0
        for r in range(len(fruits)):
            count[fruits[r]] = count.get(fruits[r], 0) + 1
            total += 1

            while len(count) > 2:
                count[fruits[l]] -= 1
                if not count[fruits[l]]:
                    del count[fruits[l]]
                total -= 1
                l += 1
            res = max(res, total)
        return res