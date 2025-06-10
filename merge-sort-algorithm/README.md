# merge-sort-algorithm

This project implements a merge sort function using the merge sort algorithm. The algorithm utilizes recursion to sort an unsorted list of numbers in ascending order. 
To do this, the array is first split in half. Then, the array is split in half recursively until the length of the array becomes <= 1, then the two smallest halves are sorted, with smaller number on the left,
then, the sorted halves are combined and sorted again as the algorithm travels up the chain of `merge_sort()` calls. Finally, `merge_sort(numbers)` returns a sorted list.

## Output
![image](https://github.com/user-attachments/assets/8b781778-b201-4e50-9c78-aabe57b49c3f)
