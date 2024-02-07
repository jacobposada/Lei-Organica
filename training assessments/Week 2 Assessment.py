# Week 2 Assessment

## 12.5 returning a value from a function 

# 1 write a function named same that takes a string as input, and simply returns that string.
def same (x): 
    return(x) 
y = "hello" 
same(y) 

# 2 write a function called same_thing that returns the parameter, unchanged.
def same_thing(x): 
    return(x) 

# 3 write a function called subtract_three that takes an integer or any number as input, and returns that number minus three.
def subtract_three(x): 
    y = x - 3 
    return(y) 
subtract_three(10) 

# 4 write a function called change that takes one number as its input and returns that number, plus 7.
def change(x): 
    y = x + 7 
    return(y) 

# 5 write a function named intro that takes a string as input. This string ist intended to be a person’s name and the output is a standardized greeting. For example, given the string “Becky” as input, the function should return: “Hello, my name is Becky and I love SI 106.”
def intro(x): 
    return("Hello, my name is " + x + " and I love SI 106.") 
intro("Becky")  

# 6 write a function called s_change that takes one string as input and returns that string, concatenated with the string “ for fun.”.
def s_change(x): 
    return(x + " for fun.")  

# 7 write a function called decision that takes a string as input, and then checks the number of characters. If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”.
def decision(x): 
    str_len = len(x) 
    if str_len > 17: 
        return("This is a long string") 
    else: 
        return("This is a short string") 


## 12.8 a function that accumulates 

# 1 write a function named total that takes a list of integers as input, and returns the total value of all those integers added together.
def total(x): 
    sum = 0 
    for i in x: 
        sum = sum + i 
    return(sum) 

# 2 write a function called count that takes a list of numbers as input and returns a count of the number of elements in the list.
def count(x): 
    list_count = len(x)  
    return(list_count) 


## 12.11 fucntions can call other functions (composition) 

# 1 write two functions, one called addit and one called mult. addit takes one number as an input and adds 5. mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result.
def addit(x): 
    addit_result = x + 5 
    return(addit_result) 
def mult(y): 
    addit_result = addit(y) 
    mult_result = addit_result * y 
    return(mult_result) 
mult(1) 


## 12.17 exercises 

# 1 write a function named num_test that takes a number as input. If the number is greater than 10, the function should return “Greater than 10.” If the number is less than 10, the function should return “Less than 10.” If the number is equal to 10, the function should return “Equal to 10.”
def num_test(x): 
    if x > 10: 
        return("Greater than 10.") 
    if x < 10: 
        return("Less than 10.") 
    if x == 10: 
        return("Equal to 10.") 

# 2 write a function that will return the number of digits in an integer.
def numDigits(x):
    x_str = str(x) 
    return(len(x_str)) 

# 3 write a function that reverses its string argument.
def reverse(astring):
    rev_string = "" 
    for i in astring: 
        rev_string = i + rev_string 
    return(rev_string) 

# 4 write a function that mirrors its string argument, generating a string containing the original string and the string backwards.
def mirror(mystr):
    mirror_str = "" 
    for i in mystr: 
        mirror_str = i + mirror_str 
    return (mystr + mirror_str) 

# 5 write a function that removes all occurrences of a given letter from a string.
def remove_letter(theLetter, theString):
    newString = ''  
    theStr_list = list(theString) 
    for i in range(len(theStr_list)): 
        if theStr_list[i] != theLetter: 
            newString = newString + theStr_list[i] 
    return(newString) 

# 6 write a function replace(s, old, new) that replaces all occurences of old with new in a string s 
def replace(s, old, new):
    newstring = '' 
    for i in range(len(s)): 
        if s[i] == old: 
            newstring = newstring + new 
        if s[i] != old: 
            newstring = newstring + s[i] 
    return(newstring) 
replace('Bookkeeper', 'e', 'A') 

# 7 write a Python function that will take a the list of 100 random integers between 0 and 1000 and return the maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)
import random as r
lst = []
for i in range(100):
    num = r.randint(1, 1000)
    lst.append(num)
def largest(lst):
    max = lst[1] 
    for i in range(len(lst)): 
        if lst[i] > max: 
            max = lst[i] 
    return(max) 

# 8 write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29: 
def sum_of_squares(xs):
    sum = 0 
    for i in xs: 
        square = i * i 
        sum+=square 
    return(sum) 

# 9 write a function to count how many odd numbers are in a list.
def countOdd(lst): 
    odd = 0 
    for i in lst: 
        if i % 2 != 0: 
            odd+=1 
    return odd 

# 10 sum up all the even numbers in a list 
def sumEven(lst): 
    sum = 0 
    for i in lst: 
        if i % 2 == 0: 
            sum+=i 
    return sum 

# 11 sum up all the negative numbers in a list.
def sumNegatives(lst): 
    sum = 0 
    for i in lst: 
        if i < 0: 
            sum+=i 
    return sum 

# 12 write a function findHypot. The function will be given the length of two sides of a right-angled triangle and it should return the length of the hypotenuse. (Hint: x ** 0.5 will return the square root, or use sqrt from the math module)
def findHypot(a,b):
    hypot = (a**2 + b**2) ** 0.5 
    return hypot 

# 13 write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd. 
def is_even(n): 
    if n % 2 == 0: 
        return True 
    else: 
        return False 
    
# 14 now write the function is_odd(n) that returns True when n is odd and False otherwise.
def is_odd(n): 
    if n % 2 == 0: 
        return False 
    else: 
        return True 
    
# 15 Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.
def is_rightangled(a, b, c):
    return abs(c**2 - (a**2 + b**2)) < 0.001


## 12.18 chapter assessment 

# 1 write a function called int_return that takes an integer as input and returns the same integer.
def int_return(x): 
    return x 

# 2 write a function called add that takes any number as its input and returns that sum with 2 added.
def add (x): 
    result = x + 2 
    return result 

# 3 write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.
def change (x): 
    new = x + "Nice to meet you!" 
    return new 

# 4 write a function, accum, that takes a list of integers as input and returns the sum of those integers.
def accum(x): 
    sum = 0 
    for num in x: 
        sum += num 
    return sum 

# 5 write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.
def length(x): 
    list_length = len(x) 
    if list_length >= 5: 
        return "Longer than 5" 
    else: 
        return "Less than 5" 

# 6 you will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.
def divide(x): 
    return x / 2 

def sum(x): 
    result = divide(x) 
    return result + 6 


## 17.2 nested dictionaries 

# 1 extract the value associated with the key color and assign it to the variable color. Do not hard code this.
info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }
color = info['personal_data']['physical_features']['color'] 

## 17.4 nested iteration 

# 1 below, we have provided a list of lists that contain information about people. Write code to create a new list that contains every person’s last name, and save that list as last_names.
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
last_names = [] 
for person in info: 
    last_names.append(person[1]) 

#2 below, we have provided a list of lists named L. Use nested iteration to save every string containing “b” into a new list named b_strings.
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings = [] 
for x in L: 
    for y in x: 
        if 'b' in y: 
            b_strings.append(y) 

