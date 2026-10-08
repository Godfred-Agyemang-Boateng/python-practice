'''
Question: What are Python's rules for valid variable names, and what's one naming convention (not a hard rule) that experienced Python developers follow?
Answer: Must start with a letter (a-z, A-Z) or an underscore. 
 Cannot Start with a Number. 
 Case-Sensitive: age, Age, and AGE are three distinct variables.
 No Reserved Keywords: Cannot use Python's built-in keywords (e.g., class, def, if, import, for).
Source: https://www.w3schools.com/python/python_variables_names.asp

Answer: Experienced Python developers follow snake_case for variable and function names (e.g., my_variable, calculate_sum).
Source: Gemini

Question: What is an f-string, and what problem did it solve compared to how strings used to be formatted in older Python code?
Answer: Before Python 3.6 introduced f-strings, string formatting relied on % formatting or the .format() 
 method, both of which were verbose, hard to read, and error-prone when handling multiple variables.
 F-strings solved readability issues by putting expressions directly where they appear in the final output string and improved
 execution speed over older methods.
 Source: Gemini

 Question: What's the difference between int and float in Python, and which type will birth_year end up as?
 Answer: In the calculation (birth_year = current_year - age), both current_year (datetime.now().year) and age are integers, hence 
 birth_year will end up as an int.
  Int is a whole number without a decimal point, while float is a number that can have a fractional part (decimal point).
 Source: Gemini
'''
# 
from datetime import datetime
name = "Boateng Godfred Agyemang" # A variable name that storess my name
age = 18 # my current age stores int the variable age

current_year = datetime.now().year # A variable that stores the current year using the datetime module
# Calculate the birth year 
birth_year = current_year - age

#This code gives a formatted string that includes my name in uppercase, my birth year, and my age. It uses an f-string to embed the variables directly into the string.
print(f"My name is {name.upper()} and I was born around {birth_year}, so I'm {age} years old.")

#A variable that stores a string representing a website(google's) URL
website = "www.google.com"
print(website)

# Removing the www. prefix and storing the cleaned website in a new variable clean_website. The removeprefix() method is used to remove the specified prefix from the string.
clean_website = website.removeprefix("www.")
print(clean_website)# Outputs the cleaned website URL without the "www." prefix.

# storing integers in the variables a, b, and c
a, b, c = 3, 5, 7
print("Sum:", a + b + c)# outputs the sum of the integers stored in a, b, and c

print("a^5:", a ** 5) #outputs the result of raising a to the power of 5
print("b^5:", b ** 5) #outputs the result of raising b to the power of 5
print("c^5:", c ** 5) #outputs the result of raising c to the power of 5

# using the string method len() to calculate the length of the string "welcome to hotel transylvania" and storing it in the variable greeting
greeting = len("welcome to hotel transylvania")
print(greeting)# outputs the length of the string stored in greeting

