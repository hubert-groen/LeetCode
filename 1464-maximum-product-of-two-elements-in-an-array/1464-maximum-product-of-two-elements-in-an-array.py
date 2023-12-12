class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_index = -1
        second_max_index = -2

        if len(nums) == 2:
            return (nums[max_index]-1)* (nums[second_max_index]-1)

        for i in range(len(nums)):

            if nums[i] > nums[max_index]:
                second_max_index = max_index
                max_index = i
            
            elif nums[i] > nums[second_max_index]:
                second_max_index = i

        return (nums[max_index]-1)* (nums[second_max_index]-1)
