**Sort Colors**

<img width="446" alt="image" src="https://user-images.githubusercontent.com/25766765/223605062-405ed1b5-889f-4f7d-a5e0-0dd3a50705d9.png">

Notes:
Solution1:
1. Count the frequency of 0, 1, and 2
2. loop through the frequency and correct the numbers in the array

Solution2:
1. Have two pointers, one for start, one for end, one to count through the array.
2. When there is 1 just increment.
3. When it is 0, swap with the left.
4. When it is 2, swap with the right.

Runtime
33 ms
Beats
77.74%
Memory
13.8 MB
Beats
52.8%
