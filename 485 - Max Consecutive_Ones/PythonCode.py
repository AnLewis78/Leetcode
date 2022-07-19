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