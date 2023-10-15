class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged_array = []

        nums2_index = 0

        for i in range(len(nums1)):
           
            if nums2_index != len(nums2) and nums1[i] <= nums2[nums2_index]:
               merged_array.append(nums1[i])

            else:
                while nums2_index < len(nums2) and nums2[nums2_index] < nums1[i]:
                    merged_array.append(nums2[nums2_index])
                    nums2_index += 1

                merged_array.append(nums1[i])

        for k in range(nums2_index, len(nums2)):
            merged_array.append(nums2[k])

        

        if len(merged_array) % 2 == 0:
            
            center_index = (len(merged_array) // 2) - 1
            median = (merged_array[center_index] + merged_array[center_index + 1]) / 2

        else:
            
            center_index = (len(merged_array) // 2) - 1
            median = merged_array[center_index + 1]

        return median