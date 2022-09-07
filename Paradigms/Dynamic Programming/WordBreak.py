"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/word-break


Brute Force Solution:
-----------------------------------------------
@description:
Use recursion and backtracking.
Check every possible prefix of that string in the dic
    If it is found in the dictionary
        Recursively check the remaingni portion of the string
If in some function call it is found that the complete string is in dic, then return True.

@complexity:
Time:   O(2^n), given a string of length n there are n+1 ways to split it into two parts
              , at each step, we have a choice: to split or not to spit
              , in the wost case when all choices are to be checked, that results in 2^n steps
Space:  O(n), the depth of the recursion tree can go upto n


DP Solution:
-----------------------------------------------
@description:
The idea is that we go over the combinations of substrings of s and see whether they are available in the dictionary.

We initialize dp to take care of cases that sub-string exists in the wordDict.
dp[i] shows whether subarray s[0:i] is available in the wordDict.
Based on this, dp[0] is basically an empty string, that's why we set it to True before the for loops begin.
Then we first loop over s and check each substring by starting a new for loop that checks the availability of each substring between j and i (s[j:i]).
For example if s = "leetcode", wordDict = ["leet", "code"], and i = 2, in the inner loop j takes values of 0, 1. Then if d[j] is true, meaning that up to that particular j is found already, and s[j:i] is in the wordDict, it would turn dp[i] to true showing that we've found s[:i] already in the wordDict somewhere.
In the below example, dp = [ True, False, False, False, True ..] since we found leet in the wordDict. Note that between index 0 and 4, there are Falses. This is because we don't have l or le or lee in wordDict. All the available combinations would be True in the dp (given the possibility of multiple segmentation) and while the second loop is checking substrings, the if statement would take care of all of them. This means that there might be multiple possible segmentations in the wordDict and once we found the first one, we're done.

Question: Imagine wordDic = ["leet","code", "lee","tcode"] and s= "leetcode", alright? Can you tell which combinations the code will find first? lee and tcode because when doing the second loop and checking s[j:i] when i = 8, tcode comes before code (note the break that gets us out of second loop). Note that it finds both lee and leet as correct substrings and will turn the dp to True for them (dp[3] = True and dp[4] = True).

You might ask why dp[j] is there in the if statement? Consider this wordDict = ["leet","ode"]. If that wasn't for dp[j] in the if statement, dp[i] could be turned to True while we were missing a letter in the s. Basically, dp[j] marks a safe station for the loop to move forward with the searching having in mind that up to this point is taken care of.


@complexity:
Time:   O(n^3), where n is the length of the input string
              , there are two nested loops, and substring computation at each iteration

Space:  O(n), length of dp array is n+1
"""


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]
