**Pre-Planning:**
	
	A) To start, I knew I needed to have a counter for this problem. 
	B) Next, I thought I would need to initalize a loop in order to go through the whole array
	C) Next, I thought I should have a comparison to see if the next array element is a 0 or 1
	D) Lastly, I figured that if the number is 1, I would need to increment the counter, but also check if the current count is greater than the overall max count. From here, I realized I will need to add a second counter in order to store the maximum count. Check the "How I could of made this better" section to see a better way of going about this
	E) Lastly, I knew if the count was zero, I would need to reset the counter
	
**Explanation:**
	
	A) Using my preplanning, I started by initalizing a counter, and a max counter I discovered in step D of my preplanning
	B) From here, I started my for loop that went to the end of the array
	C) Next, I used an if statement to check if the current element the loop is on if a 1 or 0. 
	D) For if the current element is a 1, I incremented the counter by 1. Next, I figured I would need to check if the counter is greater than the max counter count. If true, I would overwrite the max counter with the current counters count. Please check the "How I could of made this better"/ Better Code section to see a better way of writing my code.
	E) For if the current element is a 0, I reset the count back down to zero, and moved onto the next array's element.

**Code:**

	def findMaxConsecutiveOnes(nums):
        count = 0
        maxCount = 0
        for x in range(0,len(nums)):
            if nums[x] == 1:
                count += 1
                if count > maxCount:
                    maxCount = count
                    continue
            else:          
                count = 0
                continue

        return maxCount
    
    def main():
        nums = [1,1,0,1,1,1]
        print(findMaxConsecutiveOnes(nums))
    
    
    # Initalizing main function
    if __name__=="__main__":
        main()
		
----

**How I Could Of Made This Better:**

One way I discovered how to make this code better is by rewriting the for loop.
Making a simple "For x in nums:" will cut down on the time it takes to write the code. Next, I found replace the if statement that checks if the counter is greater than the max counter. There is a max function that can be used that takes less runtime to compute which value is greater. Please view below to see how to implement this into the previous code provided.

**Better Code:**
	
	def findMaxConsecutiveOnes(nums):
        maxCount, count = 0, 0
        for num in nums:
            if num == 1:
                count += 1
                maxCount = max(count, maxCount)
            else:
                count = 0
        return maxCount
    
    def main():
        nums = [1,1,0,1,1,1]
        print(findMaxConsecutiveOnes(nums))
  
  
    # Initalizing main function
    if __name__=="__main__":
        main()
		
----
**Leetcode Link:** https://leetcode.com/problems/max-consecutive-ones/discuss/2219606/Python-or-Explanation-Provided

**Thank You For Reading**
	