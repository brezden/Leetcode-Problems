from typing import List

class NumArray:
    newNums: List[int] = []

    def __init__(self, nums: List[int]):
        self.newNums = self.createArray(nums)

    def sumRange(self, left: int, right: int) -> int:
        if (left == 0):
            return self.newNums[right]

        return self.newNums[right] - self.newNums[left - 1]

    def createArray(self, nums: List[int]) -> List[int]:
        newValue = 0

        for index, num in enumerate(nums):
            newValue += num
            nums[index] = newValue

        return nums

numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
