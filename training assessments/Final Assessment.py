### Final Assessment 

## 18.6 test cases for functions 


# 18.6.2 
def update_counts(letters, counts_d):
    for c in letters:
        if c in counts_d:
            counts_d[c] = counts_d[c] + 1 
        else: 
            counts_d[c] = 1 

counts = {"a": 3, "b": 2}

update_counts("aaab", counts)

# 3 more occurrences of a, so 6 in all
assert counts["a"] == 6

# 1 more occurrence of b, so 3 in all
assert counts["b"] == 3


## 19.2 exception handling flow-of-control 


# below, we have provided a list of tuples that consist of student names, final exam scores, and whether or not they will pass the class. For some students, the tuple does not have a third element because it is unknown whether or not they will pass. 
# Currently, the for loop does not work. Add a try/except clause so the code runs without an error - if there is no third element in the tuple, no changes should be made to the dictionary.
students = [('Timmy', 95, 'Will pass'), ('Martha', 70), ('Betty', 82, 'Will pass'), ('Stewart', 50, 'Will not pass'), ('Ashley', 68), ('Natalie', 99, 'Will pass'), ('Archie', 71), ('Carl', 45, 'Will not pass')]

passing = {'Will pass': 0, 'Will not pass': 0}
for tup in students:
    try: 
        if tup[2] == 'Will pass':
            passing['Will pass'] += 1
        elif tup[2] == 'Will not pass':
            passing['Will not pass'] += 1
    except: 
        print (tup[0] + " Unknown") 

print (passing) 


# below, we have provided code that does not run. Add a try/except clause so the code runs without errors. 
# if an element is not able to undergo the addition operation, the string ‘Error’ should be appended to plus_four.
nums = [5, 9, '4', 3, 2, 1, 6, 5, '7', 4, 3, 2, 6, 7, 8, '0', 3, 4, 0, 6, 5, '3', 5, 6, 7, 8, '3', '1', 5, 6, 7, 9, 3, 2, 5, 6, '9', 2, 3, 4, 5, 1]

plus_four = []

for num in nums:
    try: 
        plus_four.append(num+4)
    except: 
        plus_four.append("Error") 

print (plus_four) 


## 20.4 adding parameters to the constructor 

# 1 create a class called NumberSet that accepts 2 integers as input, and defines two instance variables: num1 and num2, which hold each of the input integers. 
# create an instance of NumberSet where its num1 is 6 and its num2 is 10. Save this instance to a variable t.
class NumberSet: 
    
    def __init__(self, initNum1, initNum2): 
        
        self.num1 = initNum1 
        self.num2 = initNum2 
        
t = NumberSet(6, 10) 
print (t) 


## 20.5 adding other methods to a class 

# create a class called Animal that accepts two numbers as inputs and assigns them respectively to two instance variables: arms and legs. 
# create an instance method called limbs that, when called, returns the total number of limbs the animal has. 
# to the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. call the limbs method on the spider instance and save the result to the variable name spidlimbs.
class Animal: 
    def __init__(self, initArms, initLegs): 

        self.arms = initArms 
        self.legs = initLegs 
    
    def limbs(self): 

        return (self.arms + self.legs) 

spider = Animal(4, 4) 

spidlimbs = spider.limbs() 

print (spidlimbs) 


## 20.7 converting an object to a string 

# create a class called Cereal that accepts three inputs: 2 strings and 1 integer, and assigns them to 3 instance variables in the constructor: name, brand, and fiber. 
# when an instance of Cereal is printed, the user should see the following: “[name] cereal is produced by [brand] and has [fiber integer] grams of fiber in every serving!” 
# to the variable name c1, assign an instance of Cereal whose name is "Corn Flakes", brand is "Kellogg's", and fiber is 2. To the variable name c2, assign an instance of Cereal whose name is "Honey Nut Cheerios", brand is "General Mills", and fiber is 3. Practice printing both!
class Cereal: 
    
    def __init__ (self, initName, initBrand, initFiber): 

        self.name = initName 
        self.brand = initBrand
        self.fiber = initFiber 
        
    def __str__ (self): 

        return self.name + " cereal is produced by " + self.brand + " and has " + str(self.fiber) + " grams of fiber in every serving!" 

c1 = Cereal ("Corn Flakes", "Kellogg's", 2) 
c2 = Cereal ("Honey Nut Cheerios", "General Mills", 3) 

print (c1) 
print (c2) 


## 20.14 tamagotchi game 



## 20.17 exercises 

# add a method reflect_x to Point which returns a new Point, one which is the reflection of the point about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY
    
    def reflect_x(self): 

        self.y = 0 - self.y 
        return self.y 
    
pointOne = Point(6, -9) 
pointOne.reflect_x() 
assert pointOne.y == 9 

pointTwo = Point(7, 0) 
pointTwo.reflect_x() 
assert pointTwo.y == 0 

pointThree = Point(4, -9) 
pointThree.reflect_x() 
assert pointThree.y == 9 

# add a method called move that will take two parameters, call them dx and dy. The method will cause the point to move in the x and y direction the number of units given. (Hint: you will change the values of the state of the point)
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY
    
    def move(self, dx, dy): 
        
        self.x += dx 
        self.y += dy 
    
pointOne = Point(5, 5) 
pointOne.move(2, 4) 

assert (pointOne.x == 7) & (pointOne.y == 9) 

## 20.18 chapter assessment 

# define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price. 
# assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0.
class Bike: 
    
    def __init__(self, color, price): 
        
        self.color = color 
        self.price = price 

testOne = Bike("blue", 89.99) 
testTwo = Bike("purple", 25.0) 

# create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples. the constructor should initialize two instance variables: apple_color and apple_quantity. 
# write a class method called increase that increases the quantity by 1 each time it is invoked. you should also write a __str__ method for this class that returns a string of the format: "A basket of [quantity goes here] [color goes here] apples." 
class AppleBasket: 
    
    def __init__ (self, apple_color, apple_quantity): 
        
        self.apple_color = apple_color 
        self.apple_quantity = apple_quantity 
    
    def increase(self): 
        
        self.apple_quantity += 1 
        return self.apple_quantity 
    
    def __str__(self): 
        
        return f"A basket of {self.apple_quantity} {self.apple_color} apples." 

sundayBasket = AppleBasket("red", 17) 
print (sundayBasket) 

# define a class called BankAccount that accepts the name you want associated with your bank account in a string, and an integer that represents the amount of money in the account. the constructor should initialize two instance variables from those inputs: name and amt. 
class BankAccount: 

    def __init__ (self, name, amt): 

        self.name = name 
        self.amt = amt 
    
    def __str__ (self): 

        return f"Your account, {self.name}, has {self.amt} dollars."

t1 = BankAccount("Bob", 100)
print (t1) 


## 21 building programs 

# build a program that replicates a physical dictionary that you might use. the program should that take five different input from the user. each input will have two words and we will build a dictionary where the words are the keys and values.
user_purchases = {} 

for purchase in range(5): 

    response = input("Please enter two values to add to a dictionary. The first word should be the name of the purchase, and the second should be the amount spent.")

    separated_response = response.split() 
    purchase_key = separated_response[0] 
    purchase_value = separated_response[1] 

    user_purchases[purchase_key] = purchase_value 


## 23 map, filter, list comprehension, and zip 
    
# 23.4 list comprehensions 

# use list comprehension to accomplish the same thing. assign it the the variable lst2. only one line of code is needed.
num_list = [12, 34, 21, 4, 6, 9 ,42] 

lst2 = [num for num in num_list if num > 10]
print (lst2) 

# write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the dictionary tester. Do this using a list comprehension.
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
info_list = tester['info'] 

compri = [person['name'] for person in info_list]
compri = [person['name'] for person in tester['info']] 

# 23.5 zip 

# using zip and list comprehension, create a new list, L3, that sums the two numbers if the number from L1 is greater than 10 and the number from L2 is less than 5. this can be accomplished in one line of code.
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [n1 + n2 for (n1, n2) in zip(L1, L2) if (n1 > 10) & (n2 < 5)] 


# better pizza predictions with linear regression 
diameter = [6, 8, 10, 14, 18] 
price = [7, 9, 13, 17.5, 18] 

def compute_y(x, m, b): 
    
    return (x * m + b) 

def compute_all_y(list_of_x, m, b): 
    
    return [compute_y(x, m, b) for x in list_of_x] 

def compute_mse(list_of_known, list_of_predictions): 
    
    errors = [pred - known for (pred, known) in zip(list_of_predictions, list_of_known)] 
    squared_errors = [error ** 2 for error in errors] 
    return (sum(squared_errors) / len(squared_errors)) 

def fit(x_values, y_values, increment, iterations): 
    
    m = 0 
    b = 0 
    
    coefficients = [(m, b)] 
    errors = [] 
    
    for i in range(iterations): 
        m = 0 
        for j in range(iterations): 
            predictions = compute_all_y(x_values, m, b) 
            
            error = compute_mse(y_values, predictions) 
            
            errors.append(error) 
            coefficients.append((m, b))
            
            m += increment
        
        b += increment 
        
    min_error_index = errors.index(min(errors)) 
    print ("These are the coefficients (m,b):", coefficients[min_error_index]) 
    print ("This is the MSE:", errors[min_error_index]) 
    print (coefficients) 

fit(diameter, price, .1, 100) 



## project 19 - better pizza predictions with multiple regression 

def dot(a,b):
    return sum(x * y for x, y in zip(a,b)) 

import sys
# Give this program more time to run
sys.setExecutionLimit(60000)

openFile = open("pizza_toppings.csv", "r")  
listFile = list(openFile) 
print (listFile) 

numData = [i.split(",") for i in listFile[1:]]
print (numData) 

for i in numData: 
    training_inst = [int(var[0]) for var in numData] 
    diameter = [int(var[1]) for var in numData] 
    toppings = [int(var[2]) for var in numData] 
    price = [float(var[3]) for var in numData] 

print (diameter) 
print (toppings) 
print (price) 

def mean(values): 
    return sum(values) / len(values) 

def covariance(x_values, x_mean, y_values, y_mean): 
    
    x_covar = [x_values - x_mean for x in x_values] 
    y_covar = [y_values - y_mean for y in y_values] 
    return dot(x_covar, y_covar) 

def variance(values, mean_value): 
    
    return [value - mean_value for value in values] 

def coefficients(x, y): 

    # columns of 1s for intercept 
    x = [[1] + value for value in x] 


