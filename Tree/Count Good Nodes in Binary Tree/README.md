**Count Good Nodes in Binary Tree**

<img width="387" alt="image" src="https://user-images.githubusercontent.com/25766765/221289736-dc2d5aba-4890-41b0-a051-4e766f2a1b29.png">

<img width="408" alt="image" src="https://user-images.githubusercontent.com/25766765/221289675-b9cd521f-c2c6-4811-a0ef-37864791c451.png">

<img width="410" alt="image" src="https://user-images.githubusercontent.com/25766765/221289794-1ef8c152-9357-4ae3-95f9-6a89773b9c6a.png">


Notes:
1. Use DFS approach in recursive call.
2. When calling DFS also send the max value until now in the function.
3. In each call update the maximum value when compared to the current value in the node.
4. Have a value res, which stores the values from dfs of right and left subtree.
5. if the current node value is greater than or equal to the maximum value, then return 1 + the res.

Runtime
259 ms
Beats
68.41%
Memory
32.6 MB
Beats
36.96%
