from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        answer: float = 51
        LP = 0
        RP = len(nums) - 1
        nums.sort()

        while (LP < RP):
            answer = min(answer, ((nums[LP] + nums[RP]) / 2))

            LP += 1
            RP -= 1

        return answer


solution = Solution()
print(solution.minimumAverage([7,8,3,4,15,13,4,1]))