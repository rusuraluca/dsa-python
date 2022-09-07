"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/group-anagrams


HashMap Solution:
-----------------------------------------------
@description:
We can group the anagrams in a hashmap
where we create a key representing their letters sorted.

Actually, designing a key is to build a mapping relationship by yourself
between the original information and the actual key used by hash map.
When you design a key, you need to guarantee that:
1. All values belong to the same group will be mapped in the same group.
2. Values which needed to be separated into different groups will not be mapped into the same group.

This process is similar to design a hash function, but here is an essential difference.
A hash function satisfies the first rule but might not satisfy the second one.
But your mapping function should satisfy both of them.

In the example above, our mapping strategy can be:
sort the string and use the sorted string as the key.
That is to say, both "eat" and "ate" will be mapped to "aet".

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

["eat","tea","tan","ate","nat","bat"]

key       value
["aet"] - ["eat","tea", "ate"]
["ant"] - ["nat","tan"]
["abt"] - ["bat"]

@complexity:
Time:   O(n*klogk), where n is the number of anagrams and k is the max_len_anagram out of them
Space:  O(n), for the hashmap of all strings with no repetition + the sorted versions of each anagram as keys
"""
class Solution:
    def groupAnagrams(self, strs):
        if len(strs) == 0:
            return [[""]]

        hash_map = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key in hash_map:
                hash_map.get(key).append(s)
            else:
                hash_map[key] = [s]

        return hash_map.values()

