class Solution:
    def maxArea(self, heights: list[int]) -> int:
        MAX_HEIGHT = max(heights)

        max_area = 0
        start = 0
        end = len(heights) - 1
        target_height = 0
        while target_height <= MAX_HEIGHT and start < end:
            target_height = max_area / (end - start)
            start_height = heights[start]
            end_height = heights[end]
            if start_height > target_height and end_height > target_height:
                max_area = min(start_height, end_height) * (end - start)
            else:
                if start_height < end_height:
                    start += 1
                else:
                    end -= 1

        return max_area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))

