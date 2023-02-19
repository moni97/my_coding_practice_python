**Daily Temperatures**

<img width="323" alt="image" src="https://user-images.githubusercontent.com/25766765/219908031-36c67b78-2946-4280-b513-8c2c73fcf542.png">

Notes:
1. Using an array approach wont work, as the time complexity will be O(n2)
2. Use a stack approach, by maintaining a monotonically decreasing stack.
3. Pop from the stack whenever the current number is greater than the top of the stack.
4. Whenever popping, update the ans index of that corresponding index.

Runtime:
1455 ms
Beats
52.21%
Memory
29.3 MB
Beats
32.32%
