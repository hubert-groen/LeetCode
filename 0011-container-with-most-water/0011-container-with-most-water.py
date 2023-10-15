class Solution:
    def maxArea(self, height: List[int]) -> int:

        area_record = 0

        lower_index = 0
        higher_index = len(height) - 1

        while lower_index != higher_index:

            current_area = (higher_index - lower_index) * min(height[lower_index], height[higher_index])

            area_record = max(area_record, current_area)

            if height[lower_index] >= height[higher_index]:
                higher_index -= 1
            else:
                lower_index += 1

        return area_record