**Word Search**
<img width="389" alt="image" src="https://user-images.githubusercontent.com/25766765/154388742-fb2f549d-85b6-4dc6-a848-382ebc189e7d.png">

<img width="394" alt="image" src="https://user-images.githubusercontent.com/25766765/154388777-f2fbb8b3-2084-4e34-ad55-4268c258c639.png">


Notes:
Thought of this as a dfs problem and wrote a recursive solution first. But got TLE error.
So i tried to reduce the space consumed in each function call(as if the stack limit is reached can also lead to TLE). So I tried reducing the number of var I am passing in the function calls and I was not getting TLE error.

**TLE does not always mean our solution is not optimized but also means that we need to reduce the amount of space consumed.**

Runtime: 7340 ms, faster than 48.10% of Python3 online submissions for Word Search.
Memory Usage: 14 MB, less than 67.74% of Python3 online submissions for Word Search.
