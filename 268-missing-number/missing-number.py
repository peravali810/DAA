class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=0
        for i in range(len(nums)):
            x^=i+1^nums[i]
        return x