from typing import List

# Original approach I did with an array but realized after that we really only need to know the previous value
# which is the approach that was taken in the uncommented section

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         dp = [0] * len(nums)
#         dp[0] = nums[0]
#         maximum: int = dp[0]
#
#         for idx, num in enumerate(nums[1:], start=1):
#             dp[idx] = num + (dp[idx-1] if dp[idx-1] > 0 else 0)
#
#             maximum = max(maximum, dp[idx])
#
#         return maximum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        previous: int = nums[0]
        maximum: int = previous

        for idx, num in enumerate(nums[1:], start=1):
            currentValue = num + (previous if previous > 0 else 0)

            maximum = max(maximum, currentValue)
            previous = currentValue

        return maximum

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))