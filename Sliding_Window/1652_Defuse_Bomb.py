from typing import List

# Forgot the mod trick

# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         answer = [0] * len(code)
#
#         if (k == 0):
#             return [0] * len(code)
#
#         if (k > 0):
#             direction = 1
#         else:
#             direction = -1
#
#         rightPointer = k
#
#         for (idx, num) in enumerate(code):
#             leftPointer = idx + direction
#             currentSum = 0
#
#             if rightPointer > (len(code) - 1):
#                 rightPointer = rightPointer - len(code)
#
#             if leftPointer > (len(code) - 1):
#                 leftPointer = 0
#
#             for i in range(abs(k)):
#                 currentSum += code[leftPointer]
#                 leftPointer += direction
#
#                 if (leftPointer > (len(code) - 1)):
#                     leftPointer = 0
#
#             answer[idx] = currentSum
#             rightPointer += direction
#
#         return answer

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = [0] * len(code)

        if (k == 0):
            return [0] * len(code)

        if (k > 0):
            direction = 1
        else:
            direction = -1

        rightPointer = k

        for (idx, num) in enumerate(code):
            leftPointer = (idx + direction) % len(code)
            currentSum = 0

            for i in range(abs(k)):
                currentSum += code[leftPointer]
                leftPointer = (leftPointer + direction) % len(code)

            answer[idx] = currentSum
            rightPointer = (rightPointer + direction) % len(code)

        return answer

solution = Solution()
print(solution.decrypt([2,4,9,3], -2))