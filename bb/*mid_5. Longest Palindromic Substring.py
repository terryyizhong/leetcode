'''

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
'''
'''
Basic thought is simple. when you increase s by 1 character, you could only increase maxPalindromeLen by 1 or 2, and that new maxPalindrome includes this new character. Proof: if on adding 1 character, maxPalindromeLen increased by 3 or more, say the new maxPalindromeLen is Q, and the old maxPalindromeLen is P, and Q>=P+3. Then it would mean, even without this new character, there would be a palindromic substring ending in the last character, whose length is at least Q-2. Since Q-2 would be >P, this contradicts the condition that P is the maxPalindromeLen without the additional character.

So, it becomes simple, you only need to scan from beginning to the end, adding one character at a time, keeping track of maxPalindromeLen, and for each added character, you check if the substrings ending with this new character, with length P+1 or P+2, are palindromes, and update accordingly.
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen, start = 1, 0
        for i in range(len(s)):
            if i - maxlen - 1 >= 0 and s[i-maxlen-1:i+1] == s[i-maxlen-1:i+1][::-1]:
                start, maxlen = i - maxlen - 1, maxlen + 2
            elif i - maxlen >= 0 and s[i-maxlen:i+1] == s[i-maxlen:i+1][::-1]:
                start, maxlen = i - maxlen, maxlen + 1
        return s[start:start+maxlen] if len(s) != 0 else 0                
            
