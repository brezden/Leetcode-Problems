from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxMoneySeen: int = 0
        lowestMoney: int = prices[0]
        previousValue = prices[0]

        for i in range(1, len(prices)):
            currentValue = prices[i]
            lowestMoney = min(lowestMoney, previousValue)

            if (currentValue > previousValue):
                maxMoneySeen = max(maxMoneySeen, currentValue - lowestMoney)

            previousValue = currentValue

        return maxMoneySeen

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))