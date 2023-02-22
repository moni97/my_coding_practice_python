**Time Based Key-Value Storage**

<img width="341" alt="image" src="https://user-images.githubusercontent.com/25766765/220768085-fbaf47dc-87f4-4ea5-9c4e-0677eaeb26af.png">

<img width="315" alt="image" src="https://user-images.githubusercontent.com/25766765/220768114-6f586db2-478a-4e3f-bcce-ca647b20bde6.png">

Notes:
1. Start with the basics, hashmap, they key will be a string, the values will be an array of values, storing the value and the time.
2. Get the values for a given key, for the values returned, do binary search.
3. Dont implement binary search directly, see what is required for this case.
4. One important thing is, if a value is less than the timestamp, then store that current value as the result.

Runtime
815 ms
Beats
47.27%
Memory
72.5 MB
Beats
6.49%
