**Kth Largest Element in the Stream**

<img width="395" alt="image" src="https://user-images.githubusercontent.com/25766765/221477028-12e09e76-f8ab-49b9-b4f1-993d18103856.png">

<img width="389" alt="image" src="https://user-images.githubusercontent.com/25766765/221477042-6128d17c-64a2-4bde-841d-d20c162281d0.png">

Notes:
1. Use priority queue or heap.
2. The size of the heap should be the k value.
3. Whenever an element is added in the queue, heappop operation should be performed to remove the element.
4. heappush operation is performed to push an element to the heap.
5. whenever an element is added the first element in the heap is returned.

Runtime
100 ms
Beats
64.66%
Memory
18.5 MB
Beats
6.76%
