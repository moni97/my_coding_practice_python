**Diameter of Binary Tree**

<img width="392" alt="image" src="https://user-images.githubusercontent.com/25766765/221100647-f64d656b-44fc-430e-a9fc-f1a78376271e.png">

<img width="380" alt="image" src="https://user-images.githubusercontent.com/25766765/221100672-c142e6d1-f6d4-4fce-b9c1-605513817c0c.png">

Notes:
1. Intuition is do dfs left and right subtree separately
2. While returning, return 1 + max of left and right
3. While traversing in each tree, store max of res and sum of left and right.
4. Get the result of left and right.

Runtime
50 ms
Beats
50.86%
Memory
16.4 MB
Beats
33.65%
