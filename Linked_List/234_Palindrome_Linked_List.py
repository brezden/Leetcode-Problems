from typing import Optional, List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        temp = []
        currentNode = self

        while (currentNode != None):
            temp.append(currentNode.val)
            currentNode = currentNode.next

        print(temp)

    def addNodes(self, nodes: List[int]):
        currentNode = self

        for node in nodes:
            newNode = ListNode(node)

            currentNode.next = newNode
            currentNode = newNode

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []

        while (head != None):
            nums.append(head.val)
            head = head.next

        left, right = 0, len(nums) - 1

        while (left < right):
            if (nums[left] != nums[right]):
                return False

            left += 1
            right -= 1

        return True

nodes: List[int] = [2,2,1]
head = ListNode(1)
head.addNodes(nodes)

solution = Solution()
print(solution.isPalindrome(head))
