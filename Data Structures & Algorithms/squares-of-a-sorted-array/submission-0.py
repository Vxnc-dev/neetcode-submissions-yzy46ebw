class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, pot = 0, 0
        while l < len(nums):
            pot = nums[l] ** 2
            nums[l] = pot
            l += 1
            pot = 0
        nums.sort()
        return nums