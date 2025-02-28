from typing import List

# This is a pretty messy solution. Def could have broke this up into methods and not repeated
# myself so much in it.

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        totalMetal = totalPlastic = totalGlass = 0
        lastIndexMetal = lastIndexPlastic = lastIndexGlass = 0

        tempTravel = 0

        # Prefix Travel Array
        for (idx, time) in enumerate(travel):
            travel[idx] = tempTravel + time
            tempTravel += time

        for (idx, trash) in enumerate(garbage):
            for unit in trash:
                if unit == 'M':
                    totalMetal += 1
                    lastIndexMetal = idx
                if unit == 'G':
                    totalGlass += 1
                    lastIndexGlass = idx
                if unit == 'P':
                    totalPlastic += 1
                    lastIndexPlastic = idx

        maxTravelCount = len(travel) - 1
        lastIndexMetal = min(maxTravelCount, lastIndexMetal - 1)
        lastIndexPlastic = min(maxTravelCount, lastIndexPlastic - 1)
        lastIndexGlass = min(maxTravelCount, lastIndexGlass - 1)

        answer = 0

        if lastIndexMetal >= 0:
            answer += travel[lastIndexMetal]
        if lastIndexPlastic >= 0:
            answer += travel[lastIndexPlastic]
        if lastIndexGlass >= 0:
            answer += travel[lastIndexGlass]

        answer += (totalMetal + totalGlass + totalPlastic)

        return answer

solution = Solution()
print(solution.garbageCollection(["G","M"], [1]))
