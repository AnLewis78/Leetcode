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