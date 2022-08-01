"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/longest-substring-without-repeating-characters/


Sliding Window Solution:
-----------------------------------------------
@description:
In a naive approach, we would repeatedly check a substring to see if it has duplicate character in O(n^3) time.
But it is unnecessary. If a substring s{ij} from index i to j-1 is already checked to have no duplicate characters,
we only need to check if s[j] is already in the substring s{ij}.
To check if a character is already in the substring, we can scan the substring, which leads to an O(n^2)algorithm.
But we can do better.

By using HashSet as a sliding window, checking if a character in the current can be done in O(1).

A sliding window is an abstract concept commonly used in array/string problems.
A window is a range of elements in the array/string which usually defined by the start and end indices,
i.e. [i, j) (left-closed, right-open).
A sliding window is a window "slides" its two boundaries to the certain direction.
For example, if we slide [i, j) to the right by 1 element, then it becomes [i+1, j+1) (left-closed, right-open).

We use HashSet to store the characters in current window [i, j) (j = i initially).
Then we slide the index j to the right.
If it is not in the HashSet, we slide j further.
Doing so until s[j] is already in the HashSet.
At this point, we found the maximum size of substrings without duplicate characters start with index i.
If we do this for all i, we get our answer.
@complexity:
Time:   O(2n) = O(n). In the worst case each character will be visited twice by i and j.
Space:  O(min(m,n)). We need O(k) space for the sliding window, where k is the size of the Set.
        The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m.


HashTable + Sliding Window Solution:
-----------------------------------------------
@description:
The above solution requires at most 2n steps.
In fact, it could be optimized to require only n steps.
Instead of using a set to tell if a character exists or not,
we could define a mapping of the characters to its index.
Then we can skip the characters immediately when we found a repeated character.

The reason is that if s[j] have a duplicate in the range [i, j) with index j',
we don't need to increase i little by little.
We can skip all the elements in the range [i, j']
and let i to be j′+1 directly.

@complexity:
Time:   O(n), we traverse once the n characters of the given string
Space:  O(min(m,n)), we need O(k) space for the sliding window, where k is the size of the hash map
                     the size of the hash map is upper bounded by the size of the string n and the size of the charset m


ASCII Table + Sliding Window Solution:
-----------------------------------------------
@description:
The previous implements all have no assumption on the charset of the string s.
If we know that the charset is rather small, we can replace the Map with an integer array as direct access table.
Commonly used tables are:
    int[26] for Letters 'a' - 'z' or 'A' - 'Z'
    int[128] for ASCII
    int[256] for Extended ASCII

@complexity:
Time:   O(n), we traverse once the n characters of the given string
Space:  O(m), m is the size of the charset.

"""


class Solution:
    def lengthOfLongestSubstringSlidingWindow(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res

    def lengthOfLongestSubstringHashMap(self, s: str) -> int:
        hm = {}
        maxLen = 0
        start = 0

        for end in range(len(s)):
            if s[end] in hm:
                start = max(hm[s[end]], start)

            maxLen = max(maxLen, end - start + 1)
            hm[s[end]] = end + 1

        return maxLen

    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]

            index = chars[ord(r)]
            if index != None and index >= left and index < right:
                left = index + 1

            res = max(res, right - left + 1)

            chars[ord(r)] = right
            right += 1
        return res


class Tests:
    def __init__(self):
        s = Solution()
        assert s.lengthOfLongestSubstring("abcabcbb") == 3
        assert s.lengthOfLongestSubstring("bbbbb") == 1
        assert s.lengthOfLongestSubstring("pwwkew") == 3

        assert s.lengthOfLongestSubstringHashMap("abcabcbb") == 3
        assert s.lengthOfLongestSubstringHashMap("bbbbb") == 1
        assert s.lengthOfLongestSubstringHashMap("pwwkew") == 3


t = Tests()
