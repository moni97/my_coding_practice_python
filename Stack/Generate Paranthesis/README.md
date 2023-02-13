**Generate Paranthesis**

<img width="341" alt="image" src="https://user-images.githubusercontent.com/25766765/218369802-2e95c939-5048-4591-b4fa-9b66897ea2d6.png">

Notes:
1. Backtracking solution
2. Keep adding "(" until the count is less than the given number.
3. Keep adding ")" until the count is less than the count of open brackets.
4. The key here is, when one backtracking is done, remove the last added value and continue with the loop.
5. When the count is equal to the given number add the collected value to the result.

Runtime
32 ms
Beats
86.31%
Memory
14.2 MB
Beats
70.20%
