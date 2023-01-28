def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        for i in range(len(nums)):
            count = 0
            if nums[i] in nums:
                for x in nums:
                    if x == nums[i]:
                        count+= 1
                if count > 1:
                    return True
        return False

# Case 1
print(containsDuplicate([1,2,3,1]))

# Case 2
print(containsDuplicate([1,2,3,4]))

# Case 3
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))