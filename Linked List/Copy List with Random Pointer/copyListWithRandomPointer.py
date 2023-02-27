"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        list_dict= {None: None}
        copy_head = head
        while copy_head:
            list_dict[copy_head] = Node(copy_head.val)
            copy_head = copy_head.next
        copy_head = head
        new_head = None
        while copy_head:
            curr_node = list_dict[copy_head]
            curr_node.next = list_dict[copy_head.next]
            curr_node.random = list_dict[copy_head.random]
            copy_head = copy_head.next
        return list_dict[head]
