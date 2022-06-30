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