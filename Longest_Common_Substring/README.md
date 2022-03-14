**Longest Common Subsequence**

<img width="395" alt="image" src="https://user-images.githubusercontent.com/25766765/158098656-79bc249d-76f3-4952-b14d-1a3f606ef300.png">

<img width="407" alt="image" src="https://user-images.githubusercontent.com/25766765/158098739-73274734-90ba-475f-bda8-0c28b4790b6c.png">


Notes:
Basic dynamic programming problem, solution inspired from "Introduction to algorithms" by Cormann.
1. Form a matrix of col length of text1 and row length of text2.
2. If both the letters in are equal increase the length of the matrix plus one in the previous diagnol.
3. If both the letters are not equal put the maximum from the diagnol, the previous col and previous row.

Runtime: 733 ms, faster than 37.81% of Python3 online submissions for Longest Common Subsequence.
Memory Usage: 22.7 MB, less than 58.47% of Python3 online submissions for Longest Common Subsequence.
