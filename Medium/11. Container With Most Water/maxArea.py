class Solution:
    def maxArea(self, height: list[int]) -> int:
        current_max = 0
        for start, h1 in enumerate(height):
            if start == len(height) - 1:
                break
            for end, h2 in enumerate(height[-1:start:-1]):
                if h1 * (len(height) - end - start) <= current_max:
                    break
                if min(h1, h2) * (len(height) - end - start - 1) > current_max:
                    current_max = min(h1, h2) * (len(height) - end - start - 1)

        return current_max

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))

