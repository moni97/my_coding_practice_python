# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        moveHead = head
        while moveHead:
            if newHead == None:
                newHead = ListNode(moveHead.val)
            else:
                newNode = ListNode(moveHead.val)
                newNode.next = newHead
                newHead = newNode
            moveHead = moveHead.next
        return newHead 
