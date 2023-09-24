"""******************************string Questions*****************************
Exercise 1A: Create a string made of the first, middle and last character
Q : Write a program to create a new string made of an input string’s first, middle, and last character."""

# str = "james"
# str1=str[0]
# mid=int(len(str)/2)
# last=str[4]
# str1=str1+str[mid]+last
# print(str1)

""" Exercise 1B: Create a string made of the middle three characters
Q : Write a program to create a new string made of the middle three characters of an input string."""
# str1 = "JhonDipPeta"
# str2 = "JaSonAy"
# l= int(len(str2)/2)
# new=str2[l-1]+str2[l]+str2[l+1]
# print(new)

"""Exercise 2: Append new string in the middle of a given string
 Given two strings, s1 and s2.
 Q:  Write a program to create a new string s3 by appending s2 in the middle of s1."""

# s1 = "Ault"
# s2 = "Kelly"
# mid =int(len(s1)/2)
# x=s1[:mid:]
# x=x+s2+s1[mid:]
# print(x)

"""Exercise 3: Create a new string made of the first, middle, and last characters of each input string...
Given two strings, s1 and s2, 
Q: write a program to return a new string made of s1 and s2’s 
first, middle, and last characters."""

# s1 = "America"
# s2 = "Japan"
# x=s1[0]+s2[0]
# mid1=int(len(s1)/2)
# mid2=(int(len(s2)/2))
# x=x+s1[mid1]+s2[mid2]+s1[6]+s2[4]
# print(x)

"""Exercise 4: Arrange string characters such that lowercase letters should come first......
Given string contains a combination of the lower and upper case letters. 

Q: Write a program to arrange the characters of a string so that all lowercase letters should come first"""


"""Exercise 5: Count all letters, digits, and special symbols from a given string"""



""" Exercise 6: Create a mixed String using the following rules
Q : Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
 then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.
Any leftover chars go at the end of the result.
Given:
s1 = "Abc"
s2 = "Xyz" """



"""Exercise 7: String characters balance Test

Q: Write a program to check if two strings are balanced. 
For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
The character’s position doesn’t matter.
Given:

Case 1:
s1 = "Yn"
s2 = "PYnative"
Expected Output:
True

Case 2:
s1 = "Ynf"
s2 = "PYnative"
Expected Output:
False"""




"""Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
Q : Write a program to find all occurrences of “USA” in a given string ignoring the case.

Given:

str1 = "Welcome to USA. usa awesome, isn't it?"
Expected Outcome:

The USA count is: 2"""



"""Exercise 9: Calculate the sum and average of the digits present in a string
Q: Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

Given:

str1 = "PYnative29@#8496"
Expected Outcome:

Sum is: 38 Average is  6.333333333333333"""




"""Exercise 10: Write a program to count occurrences of all characters within a string
Given:

str1 = "Apple"
Expected Outcome:

{'A': 1, 'p': 2, 'l': 1, 'e': 1}"""




"""Exercise 11: Reverse a given string
Given:

str1 = "PYnative"
Expected Output:

evitanYP"""




"""Exercise 12: Find the last position of a given substring
Q: Write a program to find the last position of a substring “Emma” in a given string.

Given:

str1 = "Emma is a data scientist who knows Python. Emma works at google."
Expected Output:

Last occurrence of Emma starts at index 43"""


"""Exercise 13: Split a string on hyphens
Q: Write a program to split a given string on hyphens and display each substring.

Given:

str1 = Emma-is-a-data-scientist
Expected Output:

Displaying each substring

Emma
is
a
data
scientist"""



"""Exercise 14: Remove empty strings from a list of strings
Given:

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
Expected Output:

Original list of sting
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']"""



"""Exercise 15: Remove special symbols / punctuation from a string
Given:

str1 = "/*Jon is @developer & musician"
Expected Output:

"Jon is developer musician" """



"""Exercise 16: Removal all characters from a string except integers
Given:

str1 = 'I am 25 years and 10 months old'
Expected Output:

2510"""


"""Exercise 17: Find words with both alphabets and numbers
Q: Write a program to find words with both alphabets and numbers from an input string.

Given:

str1 = "Emma25 is Data scientist50 and AI Expert"
Expected Output:

Emma25
scientist50"""



"""Exercise 18: Replace each special symbol with # in the following string
Given:

str1 = '/*Jon is @developer & musician!!'
Expected Output:

##Jon is #developer # musician##"""


