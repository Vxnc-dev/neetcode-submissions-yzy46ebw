class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        reach = 0
        l, r = 0, k-1
        while r < len(arr):
            for i in range(l, r+1):
                reach += arr[i]
            reach = reach / k
            if reach >= threshold:
                res += 1
            reach = 0
            l += 1
            r += 1
        return res