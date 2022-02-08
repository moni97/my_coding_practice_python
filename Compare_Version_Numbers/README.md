**Compare Version Numbers**

<img width="511" alt="image" src="https://user-images.githubusercontent.com/25766765/153034338-31330a48-3822-4c7b-bde1-5f0bd16a4e49.png">

<img width="518" alt="image" src="https://user-images.githubusercontent.com/25766765/153034374-6da2359e-7ae0-46d6-85ee-e063e245dfd3.png">

Notes:

The mistakes which I made:
1. Used a separate loop to loop through the '0's in the string. But this is totally unncessary as we can compare the strings by converting it to int.
2. Used differnt pointers to keep track of bpth the string are they are of different length. Use an inline if statement to return the values of the string or '0' based on the iterator.

Runtime: 28 ms, faster than 91.38% of Python3 online submissions for Compare Version Numbers.
Memory Usage: 13.9 MB, less than 96.88% of Python3 online submissions for Compare Version Numbers.
