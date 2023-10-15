class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        output = []

        for i in range(len(nums) - 1):

            if i != 0 and nums[i] == nums[i-1]:
                continue
           
            j = i + 1
            k = len(nums) - 1

            target = -nums[i]

            while j < k:

                if nums[j] + nums[k] == target:

                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j != len(nums)-1 and nums[j] == nums[j-1]:
                        j += 1
                
                else:
                    if nums[j] + nums[k] > target:
                        k -= 1
                    else:
                        j += 1

        return output