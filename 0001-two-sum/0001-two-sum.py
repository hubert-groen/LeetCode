class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
                

my_list = [3,5,6,8,11]
target = 13

answer = Solution().twoSum(my_list, target)

print("Answer is: " + str(answer))