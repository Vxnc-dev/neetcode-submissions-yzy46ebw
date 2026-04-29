class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l, curr_wind, res = 0, 0, 0
        total = 0

        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                total += customers[i]
        
        for r in range(len(customers)):
            if grumpy[r] == 1:
                curr_wind += customers[r]

            if r-l+1 > minutes:
                if grumpy[l] == 1:
                    curr_wind -= customers[l]
                l += 1
            res = max(res, total+curr_wind)
        
        return res