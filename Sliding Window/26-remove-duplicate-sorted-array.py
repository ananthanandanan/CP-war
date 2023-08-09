class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1

        while l<=r and r<(len(nums)):
            if nums[l] == nums[r]:
                r+=1
            else:
                nums[l + 1] = nums[r]
                l+=1
        return l + 1
         

        