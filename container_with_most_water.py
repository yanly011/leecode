class Solution:
    def maxArea(self, height: List[int]) -> int:
        lh = len(height)
        if (lh < 2):
            return 0
        if (lh == 2):
            return min(height[0], height[1])

        real_height = 0
        width = 0
        max_area = 0
        previous_left = 0
        right_archor = lh - 1
        left = 0
        while (left < right_archor):
            left_height = height[left]
            if (left_height > previous_left):
                for right in range(lh - 1, left, -1):
                    width = right - left
                    right_height = height[right]
                    real_height = min(left_height, right_height)
                    if (real_height == 0):
                        break
                    else:
                        max_area = max(max_area, (real_height * width))
                        if (right_height >= left_height):
                            right_archor = right
                            break
                previous_left = left_height
            left = left + 1
        return max_area

