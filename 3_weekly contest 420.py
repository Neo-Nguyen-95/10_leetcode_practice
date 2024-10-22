#%% Q2 THINKING ABOUT IT
"""Example 1:

Input: s = "abacb", k = 2

Output: 4

Explanation:
The valid substrings are:
"aba" (character 'a' appears 2 times).
"abac" (character 'a' appears 2 times).
"abacb" (character 'a' appears 2 times).
"bacb" (character 'b' appears 2 times).

Example 2:
Input: s = "abcde", k = 1

Output: 15
"""


def f(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    substring_list = []
    for substring_len in range(len(s)):
        i = 0
        while i <= len(s)-substring_len-1:
            substring_list.append(s[i : i+substring_len+1])
            i += 1
    if k == 1:
        return len(substring_list)
    else:
    
        letter_list = set(s)
        c=0
        for a_letter in letter_list:
            for substring in substring_list[:]:
                count = sum([letter == a_letter for letter in list(substring)])
                if count >= k:
                    c += 1
                    try:  
                        substring_list.remove(substring)
                    except:
                        pass
        
        return c


f('abacb', 2)








#%% Q1
import string
"""
Example 1:
Input: target = "abc"
Output: ["a","aa","ab","aba","abb","abc"]
Princple:
    abc => a, b, c
    a => a
    aa => ab
    aba => abc

Example 2:
Input: target = "he"
Output: ["a","b","c","d","e","f","g","h","ha","hb","hc","hd","he"]
Principle:
    ha => h, e
    a b c d e f g h
    a b d e
"""

target = 'he'


def f(target):
    result = []
    for i in range(len(target)):
        array = ([target[:i] + a for a in string.ascii_lowercase 
                 if target[:i] + a <= target[:i+1]]
                 )
        result.extend(array)
    return result

f(target)
