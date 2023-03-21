**LRU Cache**

<img width="435" alt="image" src="https://user-images.githubusercontent.com/25766765/226495850-95d53824-fad7-4742-b5fc-989a321c9135.png">

Notes:
"Two ways to solve:
Less efficient:
1. Use deque to store the usage of the keys.
2. when a key is retreived pop from the left and insert it in the right. Use python deque for this operation.
3. While inserting, append in the right.
More efficient:
1. Implement the deque with a left and right pointer,
2. Create a doubly linked  list with two pointer for the front and the back.
3. do the same operation as before with the pointers."

Runtime
889 ms
Beats
58.1%
Memory
76.5 MB
Beats
31.33%
