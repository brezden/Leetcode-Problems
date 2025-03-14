class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if (len(s) < 3):
            return 0

        leftPointer = 0
        rightPointer = 2

        answer = 0

        for i in range(len(s) - 2):
            firstElement = s[leftPointer]
            secondElement = s[leftPointer + 1]
            thirdElement = s[rightPointer]

            if (firstElement != secondElement and firstElement != thirdElement and secondElement != thirdElement):
                answer += 1

            leftPointer += 1
            rightPointer += 1

        return answer

solution = Solution()
print(solution.countGoodSubstrings('aababcabc'))