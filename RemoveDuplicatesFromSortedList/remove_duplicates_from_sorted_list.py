def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _move = head
        _start = None
        _prevstart = None
        while _move and _move.next:
            if _move.val != _move.next.val:
                _start = _move
                _move = _move.next
            else:
                while _move.next and _move.val == _move.next.val:
                    _move = _move.next
                if _start:
                    _start.next = _move.next
                else:
                    head = _move.next
                _move = _move.next
        return head
