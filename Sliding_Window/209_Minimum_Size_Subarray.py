from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Calculate Prefix Array
        for (idx, num) in enumerate(nums[1:], start=1):
            nums[idx] += nums[idx - 1]

        leftPoint = rightPoint = 0
        curMinLen = 99999999

        while leftPoint <= rightPoint:
            currentTotal = 0

            if leftPoint == 0:
                currentTotal = nums[rightPoint]
            else:
                currentTotal = nums[rightPoint] - nums[leftPoint - 1]

            if currentTotal >= target:
                curMinLen = min(curMinLen, (rightPoint - leftPoint + 1))
                leftPoint += 1
            else:
                rightPoint += 1

                if rightPoint > (len(nums) - 1):
                    break

        if (curMinLen == 99999999):
            return 0

        return curMinLen

solution = Solution()
print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))