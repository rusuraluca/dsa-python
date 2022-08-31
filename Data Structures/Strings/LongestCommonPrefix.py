"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/longest-common-prefix


Horizontal Scanning Solution:
-----------------------------------------------
@description:
The idea is to horizontally scan all the characters of the array of strings one by one
and find the Longest Common Prefix among them.
The LCP can be obtained as follows – LCP(S1…SN) = LCP(LCP(LCP(S1, S2), S3),…., SN)

@pseudocode:
Iterate through the string one by one from S1 till SN.
For each iteration till ith index, the LCP(S1…Si) can be obtained.
In case, the LCP is an empty string, terminate loop and return the empty string.
Else, continue and after scanning of N strings, the LCP(S1…SN) can be obtained.

@complexity:
Time:   O(n), where n is the number of characters in the string
Space:  O(1), no auxiliary space required


Vertical Scanning Solution:
-----------------------------------------------
@description:
The idea is to scan and compare the characters from top to bottom of the ith index for each string.
This approach is efficient in cases when the LCP string is very small.
Hence, we do not need to perform K comparisons.

@pseudocode:
Iterate through the string one by one from S1 till SN.
Start comparing the 0th index, 1st index … ith index simultaneously for each string.
In case, any of the ith index characters doesn’t match, terminate the algorithm and return the LPS(1,i)
Else, continue and after scanning of N strings, the LCP(S1…SN) can be obtained.

@complexity:
Time:   O(k), where k is the sum of all the characters in all strings
Space:  O(1), no auxiliary space required


Divide and Conquer Solution:
-----------------------------------------------
@description:
The approach is to divide the given array of strings into various subproblems
and merge them to get the LCP(S1..SN).
First, divide the given array into two parts.
Then, in turn, divide the left and right array obtained into two parts
and recursively keep dividing them, until they cannot be divided further.
Mathematically, LCP(S1….SN) = LCP(S1….Sk) + LCP(Sk+1…SN),
where LCP(S1..SN) is the LCP of the array of strings and 1 < k < N.

@pseudocode:
Recursively divide the input array of strings into two parts.
For each division, find the LCP obtained so far.
Merge the obtained LCP from both the subarrays and return it.
I.e. LCP(LCP(S[left…mid], LCP(S[mid + 1, right])) and return it.

@complexity:
Time:   O(k), where k is the sum of all the characters in all strings
Space:  O(mlogn), as there are logn recursive stack calls and each needs a space of m


Sorting Solution:
-----------------------------------------------
@description:
Sort the given set of n strings.
Compare the first and last string in the sorted array of strings.
The string with prefix characters matching in the first and last string will be the answer.

@complexity:
Time:   O(n*logn), where n is the number of characters in the string
Space:  O(1), no auxiliary space required


Binary Search Solution:
-----------------------------------------------
@description:
Another way to approach the problem is to use the concept of Binary Search.

@pseudocode:
Consider the string with the smallest length. Let the length be L.
Consider a variable low = 0 and high =  L – 1.
Perform binary search:
    Divide the string into two halves, i.e. low – mid and mid + 1 to high.
    Compare the substring upto the mid of this smallest string to every other character of the remaining strings at that index.
    If the substring from 0 to mid – 1 is common among all the substrings, update low with mid + 1, else update high with mid – 1
    If low == high, terminate the algorithm and return the substring from 0 to mid.

@complexity:
Time:   O(k*logn), where k is the sum of all the characters in all strings and n is the number of characters in the string
Space:  O(1), no auxiliary space required


Follow-Up Questions:
-----------------------------------------------
What is the best time and space complexity of finding the longest prefix string?
- The best time complexity is O(N) and the space complexity is O(1) using the horizontal and vertical scanning approach.

Is the binary search approach better than the other approaches?
- No, the binary search takes O(K*logN) time complexity. Hence, it is not the most efficient approach.
"""


class Solution:
    def longestCommonPrefixHorizontal(self, s) -> str:
        if "" in s or s == []:
            return ""
        prefix = s[0]
        for i in range(1, len(s)):
            while prefix != "":
                try:
                    if str.index(str(s[i]), prefix) == 0:
                        break
                    else:
                        prefix = prefix[:-1]
                except:

                    prefix = prefix[:-1]
        return prefix

    def longestCommonPrefixVertical(self, s) -> str:
        if len(s) == 0:
            return ""
        for i in range(len(s[0])):
            c = s[0][i]
            for j in range(len(s)):
                if i == len(s[j]) or s[j][i] != c:
                    return s[0][0:i]
        return s[0]

    def longestCommonPrefixSorting(self, strs) -> str:
        strs.sort(reverse=False)

        str1 = strs[0]
        str2 = strs[len(strs) - 1]

        n1 = len(str1) - 1
        n2 = len(str2) - 1

        i = 0
        j = 0

        result = ""

        while i <= n1 and j <= n2:
            if str1[i] != str2[j]:
                break
            result += str1[i]
            i += 1
            j += 1

        return result

    def longestCommonPrefixDivide(self, s) -> str:
        left, right = 0, len(s)
        str1, str2 = '', ''
        if right > 2:
            pivot = left + (right - left) // 2
            str1 = self.longestCommonPrefixDivide(s[left:pivot + 1])
            str2 = self.longestCommonPrefixDivide(s[pivot + 1:right])
        elif right == 2:
            return self.longestCommonPrefixConquer(s[left], s[right - 1])
        else:
            return s[0]
        return self.longestCommonPrefixDivide([str1, str2])

    def longestCommonPrefixConquer(self, str1: str, str2: str) -> str:
        if not str1 or not str2: return ''
        output = ''
        for i, j in enumerate(str1):
            if i == len(str2) or j != str2[i]:
                return output
            output += j
        return output

    def longestCommonPrefixTrie(self, s) -> str:
        trie = {}

        # enter words in a trie.
        for word in s:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}

                node = node[c]

            node["#"] = word

        res = ""

        # iterate over the trie
        while trie:
            keys = list(trie.keys())
            # check if length of keys in trie is greater than 1 or # is present in the keys
            if len(keys) > 1 or "#" in keys:
                return res
            # add common prefix to result
            res += keys[0]
            # move over next key in trie
            trie = trie[keys[0]]


if __name__ == "__main__":
    # Your code goes here
    s = ['flower', 'flow', 'flight']
    sol = Solution()
    print(sol.longestCommonPrefixHorizontal(s))
