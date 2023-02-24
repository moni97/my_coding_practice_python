Binary Tree Right Side View

<img width="400" alt="image" src="https://user-images.githubusercontent.com/25766765/221286276-4e438718-654c-46b7-a3d8-c5ad168c877c.png">

<img width="394" alt="image" src="https://user-images.githubusercontent.com/25766765/221286315-b876c4de-9ee9-4c08-8e1f-dc66fb52135e.png">

NoteS:
1. Intuition is to use deque and BFS here.
2. When putting the node in the stack, also put the level.
3. When traversing in the stack, traverse to the length of the stack.
4. When removing an element from the stack, remove it from the starting and not from the ending.

Runtime
43 ms
Beats
20.1%
Memory
13.9 MB
Beats
16.8%
