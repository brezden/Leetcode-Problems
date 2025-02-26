from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        answer: int = 0
        LP = 0
        RP = len(nums) - 1
        nums.sort()

        while (LP < RP):
            answer = max(answer, nums[LP] + nums[RP])
            LP += 1
            RP -= 1

        return answer

solution = Solution()
print(solution.minPairSum([3,5,2,3]))