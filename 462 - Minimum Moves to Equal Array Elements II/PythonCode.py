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