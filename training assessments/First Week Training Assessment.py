### First Week Training Assessment 
    # No multiple choice questions included 

## List Methods Assessment 9.18 
# Question 1 
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(2, "horseback riding") 
print (sports) 

# Question 2 
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
trav_dest.remove("London") 
print(trav_dest) 

# Question 3
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
trav_dest.append("Guadalajara") 
print (trav_dest) 

## Split and Join Assessment 9.18.2 

# Question 1
awards = ['Emmy', 'Tony', 'Academy', 'Grammy']
pos = awards.index("Tony") 
print(pos) 

## For Loop Mechanics Assessment 9.18.3 

# Question 1 
str1 = "I love python"
chars = [] 
for ch in str1: 
    chars.append(ch) 
print(chars) 

## Accumulator Pattern Assessment 9.18.4 

# Question 1 - For each character in the string saved in ael, append that character to a list that should be saved in a variable app.
ael = "python!"
app = [] 
for ch in ael: 
    app.append(ch) 
print(app) 

# Question 2 - For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called past_wrds.
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = [] 
for wrd in wrds: 
    past_wrds.append(wrd + "ed")
print(past_wrds) 

# Question 3 - Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the answer to a variable num_words_list. (You should use the len function).
original_str = "The quick brown rhino jumped over the extremely lazy fox"
split_str = original_str.split() 
num_words_list = [] 
for str in split_str: 
    num_words_list.append(len(str)) 
print(num_words_list) 

# Question 4 - Create an empty string and assign it to the variable lett. Then using range, write code such that when your code is run, lett has 7 b’s ("bbbbbbb").
lett = [] 
lett = "b" * len(range(7)) 
print(lett) 

## Problem Solving Assessment 9.18.5 

# Question 1 - Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores_split = scores.split(" ") 
a_scores = 0 
for score in scores_split: 
    score = int(score) 
    if score >= 90: 
        a_scores+=1    
print (a_scores) 

# Question 2 - 
    # Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = "" 
lst = org.split() 
for i in lst: 
    if i in stopwords: 
        lst.remove(i) 
for j in lst: 
    acro+=j[0] 
acro = acro.upper() 
print(acro) 

# Question 3 - 
    # Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. “ (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = "" 
lst = sent.split() 
for i in lst: 
    if i in stopwords: 
        lst.remove(i)    
for j in lst: 
    acro = acro + j[0] + j[1] 
    if j != lst[-1]: 
        acro += ". "   
acro = acro.upper() 
print (acro) 

# Question 4 - A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.
p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]
print (p_phrase) 
print (r_phrase) 

# Question 5 - Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for item in inventory:
    item = item.split(',')
    str1="The store has{} {}, each for{} USD."
    str1=str1.format(item[1],item[0],item[2])
    print(str1)
