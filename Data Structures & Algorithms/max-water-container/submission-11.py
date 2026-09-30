class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        total = 0
        maxtotal = 0
        while l < r:
            width = r-l
            length = min(heights[l], heights[r])
            total = length * width
            maxtotal = max(total,maxtotal)
            
            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1

        return maxtotal