from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        LP = 0
        RP = len(height) - 1
        maxHeight = 0

        while (LP < RP):
            leftValue = height[LP]
            rightValue = height[RP]

            currentArea = (min(leftValue, rightValue) * (RP - LP))
            maxHeight = max(maxHeight, currentArea)

            if (leftValue < rightValue):
                LP += 1
            else:
                RP -= 1

        return maxHeight

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))