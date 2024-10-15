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
    
## input
value = input('Please enter a value:\n')
print(value)

Similar to scanners .next

#### sys.exit(") will print stuff and end code
for sys.exit, import sys is needed
