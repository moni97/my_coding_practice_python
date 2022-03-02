def maxArea(self, height: List[int]) -> int:
        n = len(height)
        copy_height = height
        max_area = -99999
        if (len(height) == 2):
            return height[0] if height[0] < height[1] else height[1]
        pivot_1 = 0
        pivot_2 = len(height) - 1
        while pivot_1 < pivot_2:
            area = (height[pivot_1] if height[pivot_1] < height[pivot_2] else height[pivot_2]) * abs((pivot_1) - (pivot_2))
            if area > max_area:
                max_area = area
            if height[pivot_1] < height[pivot_2]:
                pivot_1 += 1
            else:
                pivot_2 -= 1
        return max_area
