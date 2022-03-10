**Remove Duplicates from sorted list**

<img width="395" alt="image" src="https://user-images.githubusercontent.com/25766765/157564849-270a2c6c-1052-4606-b725-9633e6a857fa.png">

Notes:
Take two pointers, use one pointer to traverse throught the nodes and one to keep track of the last non duplicate node.
When a duplicate node is found, traverse through the nodes until the nodes are not duplicate. Link the last start node to next node of duplicates.

Runtime: 65 ms, faster than 37.81% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 13.9 MB, less than 53.56% of Python3 online submissions for Remove Duplicates from Sorted List II.
