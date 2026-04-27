class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l, r = 0, len(arr)-1
        loc_max = arr[r]
        arr[r] = -1
        r -= 1
        while l <= r:
            if arr[r] <= loc_max:
                arr[r] = loc_max
                r -= 1
            else:
                new_max = arr[r]
                arr[r] = loc_max
                loc_max = new_max
                r -= 1
        return arr