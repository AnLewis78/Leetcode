"""
    Time Complexity: O(n)
    Space Complexity: O(n)
"""

def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        #Check to make sure they are the same length
        if len(s) != len(t):
            return False

        dictS = {}; dictT = {}
        p0 = 0; p1 = len(s) -1

        # Double head pointer to add string s to the dictS dictionary
        while p0 < p1:
            dictS[s[p0]] = 1 + dictS.get(s[p0], 0)
            dictS[s[p1]] = 1 + dictS.get(s[p1], 0)
            p0 += 1 ; p1 -= 1
        # If the string is an odd length, add the odd string to the dictonary
        if p0 == p1:
            dictS[s[p0]] = 1 + dictS.get(s[p0], 0)

        p0 = 0; p1 = len(t) - 1

        # Double head pointer to add string t to the dictT dictionary
        while p0 < p1:
            dictT[t[p0]] = 1 + dictT.get(t[p0], 0)
            dictT[t[p1]] = 1 + dictT.get(t[p1], 0)
            p0 += 1 ; p1 -= 1
        # If the string is an odd length, add the odd string to the dictonary
        if p0 == p1:
            dictT[t[p0]] = 1 + dictT.get(t[p0], 0)

        # Compare the characters in both dictionaries to make sure they have the same amount
        for key in dictS:
            if key not in dictT or dictS[key] != dictT[key]:
                return False 
        return True

# Public Case 1
print(isAnagram("anagram", "nagaram"))

# Public Case 2
print(isAnagram("rat", "car"))