**Maximum Width of a Binary Tree**
<img width="389" alt="image" src="https://user-images.githubusercontent.com/25766765/155901653-00b6a8b1-b9b9-4fa2-afcf-55045152748f.png">
<img width="398" alt="image" src="https://user-images.githubusercontent.com/25766765/155901665-d1e76495-c3c5-4da2-8212-4b0a75a398e0.png">

Notes:
The trick here is to include the null nodes between non null nodes if present. This is one type of question where knowing intuition really helps. 
Here the intuition is to have a position added to each children in the node based on the position of the parent based on the following conidition,
1. The left will have pos, parent_pos * 2
2. The right will have pos, parent_pos * 2 + 1
At each level get the minimum pos, and subtract it with the maximum position and add it by 1, store the maxi positions in var maxpos.

Runtime: 45 ms, faster than 81.80% of Python3 online submissions for Maximum Width of Binary Tree.
Memory Usage: 14.8 MB, less than 88.04% of Python3 online submissions for Maximum Width of Binary Tree.
