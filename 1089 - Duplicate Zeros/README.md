**Question:**

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

**Example Given:**

	Input: arr = [1,0,2,3,0,4,5,0]
	Output: [1,0,0,2,3,0,0,4]
	Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

**Pre-Planning:**

- From the question, we will need to use a insert() method to be able to duplicate every 0 we see: 
- Secondly, we need to figure / find a way to push the elements of the array to the right every time a 0 is inserted
- Lastly from what we are given, we need to figure a way to get rid of the numbers that are falling off the end of the array per the example given to us

**Python Approach:**

- To start this, we will need a loop to go through each element of the array we are passing in. The best option we have to start with is a while loop. The question of "Why use a while loop, rather than a for loop?" is what I first thought of while going through this. While this is able to be accomplished with a for loop, a while loop consumes less memory because we are able to alter with the index. With the for loop method, we would need to add a flag in order solve our index issue.  View the code / resource I have provided below as to how I reached this conclusion.
- Next after looking at our preplanning, we will need to check if the current element is a 0. If true, we will get to use the .insert() method in order to insert an extra zero at the next element of the array.
- Third, we will need to get rid of the element that we pushed off the end of the array. Using the pop method, we can easily accomplish this. Just as a stack pushes and pops, we can use that method to get rid of the last element easily.
- Lastly, we will need to increment the index by 1, this will allow for the program to not get stuck in a infinite loop, and move onto the next array element.

**Python Code Using While Loop:**

    def duplicateZeros(arr):
        i = 0
        while (i < len(arr)):
            if arr[i] == 0: # if the current element is a 0
                arr.insert(i, 0) # insert a 0 after the current element
                arr.pop() # pop the element that has fallen off our array
                i += 1 # increment by one so we arn't in a infinite loop
            i += 1

        return arr

    def main():
        arr = [1,0,2,3,0,4,5,0]
        print(duplicateZeros(arr))
    
    
    # Initalizing main function
    if __name__=="__main__":
        main()


**Python Code Using For Loop:**

	def duplicateZeros(arr):
        flag = False
        for x in range(len(arr) - 1):
            if flag == True: 
                flag = False
                continue
            if arr[x] == 0:
                arr.insert(x,0)
                arr.pop()
                flag = True
                continue

        return arr

    def main():
        arr = [1,0,2,3,0,4,5,0]
        print(duplicateZeros(arr))
    
    
    # Initalizing main function
    if __name__=="__main__":
        main()

----

**Java Approach:**

- To start in Java, we will can start by having a for loop until the end of the array we are given.
- Next thing to think about is how to go about the insert method for Java. Java doesn't have a method to easily insert a duplicate 0 into the array. The two best ways I thought were to use duplicate array or array list.
- To start, we would need a loop to go through the whole array. In this loop, we will use j as out way to pop off the elements that are falling off our array
- From here, we will immediately copy the next element to the temporary array
- If the current element is a 0, then we will increment the J and copy another 0 to the temporary array. I have added a resource below on how to copy when dealing with an array list.
- Once we have gone through the whole array, we will use a loop to overwrite the array we started with, with the newly formed temporary array

**Java Code Using Duplicate Array:**

	class Solution {
		public void duplicateZeros(int[] arr) {

			int[] temp = new int [arr.length];
			int j = 0;

			for (int i = 0 ; i < arr.length - j; i++) {
				temp[i + j] = arr[i]; 
				if (arr[i] == 0) {                        
					j++; 
					temp[i+j] = arr[i]; 
				}
			}

			for (int i = 0; i < arr.length; i++) {
				arr[i] = temp[i];   
			}  
		}
	}
		
**Java Code Using Duplicate Array List:**

	class Solution {
		public void duplicateZeros(int[] arr) {
			List<Integer> temp = new ArrayList();
			int j = 0;
			for (int i = 0; i < arr.length && j < arr.length; i++) {
				if (arr[i] != 0) {
					temp.add(j, arr[i]);
					j = j + 1;
				} else {
					temp.add(j, arr[i]);
					temp.add(j + 1, arr[i]);
					j = j + 2;
				}
			}
			for (int i = 0; i < arr.length; i++) {
				arr[i] = temp.get(i);
			}
		}
	}
----

**Python Loop Resources:** https://stackoverflow.com/questions/14785495/how-to-change-index-of-a-for-loop

**Python Pop Method Resource:** https://www.geeksforgeeks.org/python-list-pop/

**Java Array List Resource:** https://www.geeksforgeeks.org/how-to-add-an-element-to-an-array-in-java/

**Java Copy To Another Array:** https://www.geeksforgeeks.org/how-to-add-an-element-to-an-array-in-java/

**Thanks For Reading**
