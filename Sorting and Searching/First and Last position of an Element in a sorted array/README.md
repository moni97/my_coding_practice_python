**First and Last position of an element in a sorted array**

<img width="448" alt="image" src="https://user-images.githubusercontent.com/25766765/224245538-774cd16a-0cd3-4177-a434-85ec0d5086ca.png">

Notes:
1. Very interesting problem.
2. since it is mentioned runtime should be O(log n), it is a binary solution.
3. Now we have to think how to tweak a binary solution.
4. Go to the left and right of the array, and do binary search each side.
5. whenever the mid is equal to the target store the value of mid separately.
6. Set a bias based on which we should decide which side to search.

Runtime
95 ms
Beats
26.80%
Memory
15.4 MB
Beats
87.59%
