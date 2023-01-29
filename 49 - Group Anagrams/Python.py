def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in ans:
                ans[sorted_s] = []
            ans[sorted_s].append(s)
        return list(ans.values())

# Public Case 1
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# Public Case 2
print(groupAnagrams([""]))

#public Case 3
print(groupAnagrams(["a"]))