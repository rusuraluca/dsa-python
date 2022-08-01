"""
Problem:
-----------------------------------------------
Given a word and a text, return the count of occurrences of the anagrams of the word in the text.

Input: text = gotxxotgxdogt, word = "got"
Output : 3
Explanation: Words — got, otg, ogt are anagrams of got.

Input: text = forxxorfxdofr, word = "for"
Output : 3
Explanation: Words — for, orf, ofr are anagrams of for.

Input:  text = aabaabaa, word = aaba
Output: 4
Explanation : Anagrams of the word aaba - aaba, abaa each appear twice in the text and hence the count is 4.


Sliding-Window + Heap Solution:
-----------------------------------------------
@description:
Consider 2 heaps of English letters, i.e. of 26 characters - word heap and text heap - initialized with 0
Consider our starting point of the sliding window - initialized with 0
Consider our count variable - initialized with 0
Traverse once the word, char by char
    Update the word heap with words characters
Traverse once the text, char by char
    Update the text heap with texts characters
    If our sliding window has length equal to the length of the given word
        If the text heap is equal to the word heap i.e. the window and the given word have same chars
            Then increase count
        Shrink sliding window, i.e. remove the first char - update text heap at first char with 0
                                                          - starting point increases by 1
Return the count variable

@complexity:
Time: O(n+w), where n is the number of characters in the input text string
              where w is the number of characters in the input word string
Space: O(1)
"""


class Solution:
    def countOccurrencesofAnagram(self, text, word):
        # text chars heap
        tHeap = [0] * 26
        # word chars heap
        wHeap = [0] * 26

        # count for occurrences
        count = 0

        for c in word:
            wHeap[ord(c) - ord('a')] = 1

        windowStart = 0
        for windowEnd in range(len(text)):
            tHeap[ord(text[windowEnd]) - ord('a')] = 1
            if (windowEnd - windowStart + 1) == len(word):
                if tHeap == wHeap:
                    count += 1

                tHeap[ord(text[windowStart]) - ord('a')] = 0
                windowStart += 1

        return count


    def countOccurrencesofAnagram2(self, text, word):
        def isAnagram(s, word):
            if len(s) != len(word):
                return False

            d = [0] * 26
            for c in s:
                d[ord(c) - ord('a')] = 1

            for c in word:
                if d[ord(c) - ord('a')] == 0:
                    return False

            return True


class Tests:
    def __init__(self):
        s = Solution()
        assert s.countOccurrencesofAnagram("g", "got") == 0
        assert s.countOccurrencesofAnagram("gotxxotgxdogt", "got") == 3
        assert s.countOccurrencesofAnagram("aabaabaa", "aaba") == 2


t = Tests()
