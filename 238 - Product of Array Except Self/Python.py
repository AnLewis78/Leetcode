def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        temp = 1
        # Go through each of the element in the list
        for i in range(len(nums)):
            for count, value in enumerate(nums):
                if count != i:
                    temp *= value
            answer.append(temp)
            temp = 1
        return answer
        



# Public Case 1
print(productExceptSelf([1,2,3,4]))

# Public Case 2
print(productExceptSelf([-1,1,0,-3,3]))