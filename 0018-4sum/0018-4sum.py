class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)
        final_output = []

        def threeSum(first_index, target):

            three_output = []

            for i in range(first_index, len(nums) - 2):

                if i != first_index and nums[i] == nums[i - 1]:
                    continue

                j = i + 1
                k = len(nums) - 1

                new_target = target - nums[i]

                while j < k:

                    if nums[j] + nums[k] == new_target:
                        three_output.append([nums[i], nums[j], nums[k]])

                        j += 1
                        k -= 1

                        while j != len(nums)-1 and nums[j] == nums[j-1]:
                            j += 1

                    else:

                        if nums[j] + nums[k] > new_target:
                            k -= 1
                        else:
                            j += 1

            return three_output

        for k in range(len(nums) - 3):

            if k != 0 and nums[k] == nums[k-1]:
                continue
            new_target = target - nums[k]
            result = threeSum(k+1, new_target)
            for t in range(len(result)):
                four_sum = result[t]
                four_sum.insert(0, nums[k])
                final_output.append(four_sum)
            
        return final_output