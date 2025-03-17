class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        leftPointer = rightPointer = answerCount = 0

        while (leftPointer <= rightPointer and (leftPointer <= len(s) and rightPointer <= len(s))):
            if (rightPointer > len(s) - 1):
                leftPointer += 1
                rightPointer = leftPointer
                continue

            zeroCounter = 0
            oneCounter = 0

            currentIndex = leftPointer

            for i in range((rightPointer - leftPointer) + 1):
                if (s[currentIndex] == "0"):
                    zeroCounter += 1
                else:
                    oneCounter += 1

                currentIndex += 1

            if (zeroCounter <= k or oneCounter <= k):
                answerCount += 1
                rightPointer += 1
            else:
                leftPointer += 1
                rightPointer = leftPointer

        return answerCount

solution = Solution()
print(solution.countKConstraintSubstrings("1010101", 2))