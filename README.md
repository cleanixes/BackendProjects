# Notes

### imports
import sys for like sys.exit
import random for .random like rockpaper scissors


from enum import Enum for 
(short for "enumeration") is a special data type that allows you to define a variable that can hold a set of predefined constants. The enum import would typically allow you to use enumerations defined in another module or library.

Here are some key points about enum:

Definition: An enum is a collection of related values, usually defined as a list of named constants. For example, you might define an enum for days of the week, colors, or states in a process.

Usage: Enums make your code more readable and maintainable. Instead of using arbitrary integers or strings to represent states or categories, you can use meaningful names.

Examples: 

from enum import Enum

class Col(Enum):


    RED = 1
    
    GREEN = 2
    
    BLUE = 3
    
print(Col(1)) - "Col.RED"

print(Col(GREEN))  - "Col.GREEN"

print(Col['GREEN'])  - "Col.GREEN"

print(Col.GREEN.value) - 2

can use .replace to get rid of Col.
## input
value = input('Please enter a value:\n')
print(value)

Similar to scanners .next

#### sys.exit(") will print stuff and end code
for sys.exit, import sys is needed

## lists and tuples
users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in emptylist) - will check if the string is in the emptylist

you can print the index like [0] will give first element
#### This is important, an index of [-1] will give the last element, serving as 0 on the end side, [-2] is second to last, etc.
print(users[0:2]) will print all elements from the first index all the way to the element in the index before 2, so element at index 0, and at index 1, but not 2, in this case
print(users[1:]) will print all elements from the second index onward, till the end, if no second parameter is given
print(users[-3:-1]) can take negative, backtracks.

print(len(data)) will print the amount of elements/items in the list

.index is the same as indexof in java, users.index('Sara') will print the index of the element Sara in the list users

adding an element to a list, at the end, users.append('elsa') will add an element 'elsa', can also use +=[list]
append uses () and += uses []

users.extend is same as append, but takes multiple elements

users.insert(0, 'Bob') will insert 'Bob' at 0 index of the list called users

users[2:2] = ['Eddie', 'Alex'] will insert the two names at index 2 and ends at index 2, therefore these two will be placed between the 2nd and 3rd element in the list

users[1:3] = ['Robet', 'JPJ'] will replace the 2nd and 3rd element, since there is a range of 2 and starts at the second element

users.remove('Bob') will get rid of Bob from the list

print(users.pop()) will remove the last element of the list, and will return the element

del users[0] will delete whatever element is in the 0 index
del users will delete the whole list

users.clear will empty the list, users, and will then return an empty list of the users is printed

users.sort in this case sorts the list alpha
when sorting, lowercase strings are after every uppercase

users.sort(key=str.lower) will sort the users list and make them all lower case

.reverse will reverse the list, if reverse=true inside of sort function, it will sort and reverse
