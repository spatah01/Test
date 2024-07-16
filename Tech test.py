#!/usr/bin/env python
# coding: utf-8

# # Problem 1: Design a function that reverses the digits of an integer. For example, 50 should become 5 and -12 should become -21.

# In[33]:


def reverse_integer(num):
    sign = -1 if num < 0 else 1
    reversed_num = int(str(abs(num))[::-1])
    return sign * reversed_num
print("Reversed Integer:")
print(reverse_integer(50))  # Should Output: 5
print(reverse_integer(-12)) # Should Output: -21


# # Problem 2: Recursive Function to Calculate the Factorial of a Number

# In[43]:


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("\nFactorial is:")
print(factorial(7))  
print(factorial(2)) 


# # Problem 3: Design a function that takes a string or sequence of characters as input and returns the character that appears most frequently.
# 

# In[47]:


from collections import Counter

def most_frequent_char(s):
    count = Counter(s)
    return count.most_common(1)[0][0]

print("\nMost Frequent Character :")
print(most_frequent_char("15559")) 
print(most_frequent_char("Week")) 


# # Problem 4: Check if a String is a Pangram

# In[57]:


import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())

print("\nPangram :")
print(is_pangram("The quick brown fox jumps over the lazy dog")) 
print(is_pangram("Hello, world!")) 


# # Problem 5: Check for Consecutive Threes in a List

# In[63]:


def contains_consecutive_threes(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print("\nConsecutive Threes Test:")
print(contains_consecutive_threes([2, 3, 3, 4])) #true
print(contains_consecutive_threes([2, 3, 1, 3,4])) #false


# # Problem 6: Reverse Words in a Sentence like Master Yoda

# In[65]:


def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

# Test
print("\nYoda Speak Test:")
print(reverse_words("Come back")) 
print(reverse_words("May the grace be with you")) # 


# In[ ]:




