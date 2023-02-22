**Find the Duplicate Number**

<img width="412" alt="image" src="https://user-images.githubusercontent.com/25766765/220773615-0aae687d-c049-4755-a8c3-ca43df367211.png">

Notes:
1. Floyd's algorithm to find the beginning of the cycle.
2. The numbers in the indexes are used as the pointers.
3. First use slow and fast pointer to find the intersection.
4. Now use two slow pointer, one from intersection, other from start, they both will intersect at the right position.

Runtime
683 ms
Beats
39.95%
Memory
27.9 MB
Beats
88.50%
