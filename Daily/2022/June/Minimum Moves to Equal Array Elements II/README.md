**Pre-Planning:**
	A) In starting, I had to think how to get the number out of the array that was in the middle.
	B) Next, I figured I would need to establish a loop that would go through all the array elements, and find the subtracted difference between      that  element and the middle element
	C) Lastly I knew I would need to add a counter that would let me store those difference values into one variable
	
**Explination:**
	A) In following my pre-planning I wrote out, I started with using nums.sort(), to sort the array. From there I divided the the nums length by 2, and typcasted the result as a integer instead of a float so I could find the middle index.
	B) Once I had this middle index, I created a for loop starting at 0 to the end of the nums array. Next, I checked if the middle element was greater than or less than the current element the loop was on. If it was greater than, I subtracted it by the smaller number. Else, if the middle number was less than, I subtracted by the greater number. I did it this way, so I could get a positive number. Read my section of how I could of made this better, for a better solution. 
	C) Finally, I would add the number to the counter, and let the loop go back through its next iteration until the end was reached.
	
**How I could of made this better:**
	A) As this was just my first go through of the code, I see one better way to write this. Instead of wasting computation time with asking two if statements for each loop that is happening, you could just take the absolute value of the difference and add it to the counter instead.
	
**Code:**
	
	def minMoves2(nums):
    #sort the nums in order, so you can set up getting the median of the list
    nums.sort()
    #Find the median while typecasting it as a int
    middleIndex = int(len(nums) /2)
    count = 0
    for x  in range(0,len(nums)):
        #if the number at index of x is less than the median number 
        if nums[x] < nums[middleIndex]:
            #subtract the difference from the median number, and add it to the count
            difference = nums[middleIndex] - nums[x]
            count += difference
        #if the number at the index of x is greater than the median number
        if nums[x] > nums[middleIndex]:
            #find the difference from the greater number, and add it to the count
            difference = nums[x] - nums[middleIndex]
            count += difference
        
    return count

    
    def main():
        nums = [1,10,2,9]
        print(minMoves2(nums))
  
  
    # Initalizing main function
    if __name__=="__main__":
        main()
		
----

**Leetcode Link:**
[https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/2219022/Python-or-Explanation-Provided](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/2219022/Python-or-Explanation-Provided)

**Thank you for reading**

