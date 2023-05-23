**Maximum length of concatenated string with unique characters**

<img width="368" alt="image" src="https://github.com/moni97/my_coding_practice_python/assets/25766765/e618725f-93f0-403f-a45f-00cd38349561">

Notes:
1. Usual backtracking approach.
2. Have a generic set which has all the characters
3. At every index we have two choices to make, either consider that string or not.
4. First check if the string have unoque characters.
5. Add characters in the charSet and call backtrack with the next index.
6. Remove the characters added and call backtrack with next index.

Runtime
561 ms
Beats
22.39%
Memory
16.4 MB
Beats
34.71%
