class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        start = r+1
        while l < start:
            if nums[l] == 0:
                nums.insert(r+1,0)
                nums.pop(l)
                start -= 1
            else:
                l += 1
            