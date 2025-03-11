from typing import List

class Solution:
    def solution(self, nums: List[int]) -> List[int]:
        # [1,2,3,4]
        # [1,2,6,24]
        # [24,12,8,6]

        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        result = [0] * n

        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]

        for i in range(n - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]

        return result

solution = Solution()
print(solution.solution([1,2,3,4]))
