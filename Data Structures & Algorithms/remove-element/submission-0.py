class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, count = 0, 0
        end = len(nums)
        r = len(nums)-1
        while l < end:
            if nums[l] == val:
                count += 1
                nums.pop(l)
                nums.insert(r,val)
                end -= 1
            else:
                l += 1
        return len(nums) - count