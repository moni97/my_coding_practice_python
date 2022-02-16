    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        copy_head = head
        head2 = head.next if head and head.next else head
        prev_node = None
        while copy_head and copy_head.next:
            
            next_node = copy_head.next
            next_next_node = copy_head.next.next
            
            copy_head.next = next_next_node
            next_node.next = copy_head
            
            if prev_node:
                prev_node.next = next_node
            prev_node = copy_head
            copy_head = copy_head.next
        return head2
