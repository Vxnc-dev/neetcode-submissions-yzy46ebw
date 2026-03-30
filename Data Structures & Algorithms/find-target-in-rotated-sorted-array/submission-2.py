class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, m in enumerate(nums):
            if target == m:
                return i
        return -1