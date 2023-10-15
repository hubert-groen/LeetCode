class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums = sorted(nums)
        record = float('inf')

        for i in range(len(nums) - 1):

            j = i + 1
            k = len(nums) - 1
            to_get = target - nums[i]
            
            while j < k:

                pair_sum = nums[j] + nums[k]

                if pair_sum == to_get:
                    return target
                
                elif pair_sum < to_get:
                    j += 1
                
                else:
                    k -=1

                if abs(to_get - pair_sum) < record:
                    record = abs(to_get - pair_sum)
                    output = nums[i] + pair_sum

        return output