**Pre-Planning:**
	
- To start, I knew I needed to start with a counter in order to store how many even lined numbers are in the array
- Second, I knew I needed a for loop to go through each element within the array. In my pre-planning, I was thinking of using a "for x in nums:" instead of a "for x in nums loop instead of a for x in range(0,len(nums)) ", as that is not needed and "for x in nums:" is simple
- Third, I knew I needed to have a if statement to check and make sure the current element the loop is on, is a even length
- Lastly, I would increment the counter if the length of the number was even
	
**Explanation:**
	
- First, I used my preplanning and started by initalizing a counter. I used this counter to hold the count of how many array elements are of even length
- Second, I initalized a for loop to go through each of the array elements. As I thought in my pre-planning, I used a simple "for x in nums:" as this is the most simple / easy to read approach for this problem.
- Third, I needed to set up a if statement to check if the array elements length is even. This can be tricky at first, but can be solved through typecasting. We needed to typecast the array element as a string, and from there we could mod the element by 2 and see if it came out to an even number.
- Lastly, I incremented the total count if the numbers length came out even


**Code:**

	def findNumbers(nums):
		count = 0
		for x in nums:
			if len(str(x)) % 2 == 0:
				count += 1
		
		return count
    
	def main():
		nums = [555,901,482,1771]
		print(findNumbers(nums))
  
  
	# Initalizing main function
	if __name__=="__main__":
		main()
			
----

**Leetcode Question:**
[https://leetcode.com/problems/find-numbers-with-even-number-of-digits/](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)

**Leetcode Post:**
[https://leetcode.com/problems/find-numbers-with-even-number-of-digits/discuss/2219874/Python-or-Explanation-Provided](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/discuss/2219874/Python-or-Explanation-Provided)

**Thank You For Reading**