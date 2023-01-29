"""
    Time Complexity: O(n log n) - sorted method takes n log n time
    Space Complexity: O(n)
"""

def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numsDict = {}
        answer = []

        # Add all of the nums to the dictionary, and increment the count of duplicate chars
        for i in range(len(nums)):
            numsDict[nums[i]] = 1 + numsDict.get(nums[i], 0)

        # sort based on the keys (count of duplicate chars), and reverse the list to get greatest count first
        sortedDict = sorted(numsDict, key=lambda x: numsDict[x], reverse=True)

        # Append the top greatest values based on how many wants to be displayed
        for key in sortedDict:
            if k > 0:
                k -= 1
                answer.append(key)
            else:
                break

        return answer

# Public Case One
print(topKFrequent([1,1,1,2,2,3], 2))

# Public Case Two
print(topKFrequent([1], 1))

# Public Case Three
print(topKFrequent([4,1,-1,2,-1,2,3], 2))