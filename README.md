# AVLtree

Usage:
1. Rename the dataset to “ops-half.txt”
2. Relocate the renamed dataset to AVL file

(If you are using the my dataset, ignore the first two lines)

3. Open command prompt
4. cd to AVL
5. Input: 
	AVL.exe “./ops-half.txt”
6. If the exe file cannot run properly due to the compatibility problem of windows version,
    please try to input:
	python AVL.py “./ops-half.txt”
The python version I used is 2.7

Background:
1. The algorithm I constructed is AVL tree. Undoubtedly, querying is efficient. In return, insertion and deletion are costly because of the rotation.

2. The dataset I dealt with contains only 50 queries and 500,000 insertions. I need to find the predecessor and do insertion whenever I encountered the query commands and insertion commands respectively. The target time to process all of the command is 5 seconds.

3. It is not possible to perform querying after all of the insertion as the queries distributed randomly in the dataset.

4. Doing the insertion one by one is very costly because we probably have to implement rebalancing for every insertion. Remember, we have to process all of the commands within 5 seconds.

5. In order to improve the algorithms, I decided not to use rotation to manage the tree.


Steps:
1. Append the number to the array whenever “ins” command is encountered.
2. Do the step 1 repeatedly until we meet “qry” command.
3. Sort that array by quick sort algorithm.
4. Convert the sorted array into AVL tree by binary search algorithm. The time complexity for this step is O(n).
5. Empty the sorted array.
5. Append the AVL tree to a specific array which used to stored AVL tree.
6. Query the number by searching the AVL trees in the AVL tree array.
7. If do it properly, it should return one number in the first query, two numbers in the second query, and so on. 
8. The predecessor of the query number should be the largest one in the returned value.
9. Keep repeating Step 1 to Step 9 until all of the insertions and queries are done.

Advance version:
1. In step 2, we stop appending the array until we encounter query command. 
2. Indeed, the appending action can be stopped earlier. For example, stop appending after 500 numbers were added. 
3. More tree would be constructed. 
4. Time can be saved in sorting process. 
5. However, each AVL tree should not contain too few nodes. Otherwise, it would backfire us in searching process. We would lose the query advantage.

PS. All of the commands can be done in 4 - 8 seconds.

PS2. As I am using quick sort, it can finish it within 5 seconds if being lucky.

PS3. It used around 95 seconds to process all of the actions if the original AVL tree (with rotation) is being applied.
