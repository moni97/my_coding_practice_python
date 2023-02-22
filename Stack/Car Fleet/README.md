**Car Fleet**

<img width="340" alt="image" src="https://user-images.githubusercontent.com/25766765/220534738-f27e96a9-6542-4606-8bcb-94babc89007e.png">

<img width="335" alt="image" src="https://user-images.githubusercontent.com/25766765/220534767-5ca78c4e-cf94-4946-bfb2-dac23f6d4d79.png">

Notes:
1. Stack should be used.
2. Important thing here is the intuition behind this, the intuition is treating this problem as a linear system of equations.
3. Form pairs of position and speed and sort in the reverse order.
4. The target minus position, divided by the distance gives an answer, that should be inserted in the stack.
5. Whenever the len of the stack is greater or equal to 2, then compare the top 2 items in the stack. If the topmost item is less than or equal to the item before it, then pop that element from the stack. Because if this value is greater then the previous value it means that, the car in the back position will overtake the car before this. In this case these two are separate fleet. We no need to check the topmost with the other value than the adjacent value to it, because those values would already been checked.

Runtime
1749 ms
Beats
9.42%
Memory
33.6 MB
Beats
85.9%
