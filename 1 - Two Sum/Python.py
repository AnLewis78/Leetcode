def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        p0 = 0; p1 = len(nums) -1

        while True:
            sum = nums[p0] + nums[p1]

            if p0 == p1:
                #counter += 1
                p1 = len(nums) -1 
                p0 += 1
            elif sum == target:
                return [p0, p1]
            else:
                p1 -= 1

            
# Public Case 1
print(twoSum([2,7,11,15], 9))

# Public Case 2
print(twoSum([3,2,4], 6))

# Public Case 3
print(twoSum([3,3], 6))