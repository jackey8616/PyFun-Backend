##Variable Type
##Strings are defined either with a single quote or a double quotes
veriable_name="string"
#example 1
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

##python supports two types of numbers - integers and floating point numbers
ver_name=4 #integer
ver_name=4.0 #float

##Long integer number, use of L or l makes variable as long integer
var_name  = 12L 

##The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed,
#while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. 
#Tuples can be thought of as read-only lists

#!/usr/bin/python

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print tuple           # Prints complete list
print tuple[0]        # Prints first element of the list
print tuple[1:3]      # Prints elements starting from 2nd till 3rd 
print tuple[2:]       # Prints elements starting from 3rd element
print tinytuple * 2   # Prints list two times
print tuple + tinytuple # Prints concatenated lists

##Python Lists
#!/usr/bin/python

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd 
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists

##Python Dictionary
#Python's dictionaries are kind of hash table type.

#!/usr/bin/python

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values

##Condition
#if Statements
The syntax of the if...else statement is −

if expression:
   statement(s)
else:
   statement(s)
   
  ## Example 1
 Live Demo
#!/usr/bin/python

var1 = 100
if var1:
   print "1 - Got a true expression value"
   print var1
else:
   print "1 - Got a false expression value"
   print var1

var2 = 0
 

print "Good bye!"

## Example 2
  
#!/usr/bin/python

var = 100
if var == 200:
   print "1 - Got a true expression value"
   print var
elif var == 150:
   print "2 - Got a true expression value"
   print var
 
else:
   print "4 - Got a false expression value"
   print var

print "Good bye!"

##Loop

##Syntax of for Loop
#for val in sequence:
#	Body of for
##For Example
# Program to find the sum of all numbers stored in a list

# List of numbers
numhttps://www.programiz.com/python-programming/for-loopbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("The sum is", sum)
  


## Example OF While
 
#The syntax of a while loop in Python programming language is −

#while expression:
 #  statement(s)
 
#!/usr/bin/python

count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"

## Function 
#Syntax
#def functionname( parameters ):
#   "function_docstring"
  # function_suite
 #  return [expression]
# Example 
#!/usr/bin/python

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist

#Example 2
#!/usr/bin/python

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

