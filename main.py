# --------Day 01--------

# 01 Indentation
# Python uses indentation to indicate a block of code
# Example
if 1 > 2:
  print("Hello!")

# ------------------------

# 02 Comments
# Comments are of Two types: Normal Comment & Multiline Comment
# Example
# Normal Comment
"""
Multiline Comment
"""

# ------------------------

# 03 Variable
"""  
Variables in Python doesn't need a Declaration
Python is Case-sensitive
You can use Single Or Double Quote to Store a String
Variable can only have A-Z, 0-9 & _
Variable can't begin with Numbers
"""
# Example
a = 1
print(a)
b = "Shyam"
print(b)

# ------------------------

# 04 Type Casting
# Coverting Values from One to another
c = str(5)
print(c)
d = float(5)
print(d)

# ------------------------

# 05 Find Data Type
atype = type(a)
print(atype)
btype = type(b)
print(btype)

# --------Day 02--------

# 06 Multiple Variables & Multiple Values
Pat_Name, Pat_DOS, Pat_DOB = "Shyam", "05/01/1995", "05/10/1920"
print(Pat_Name)
print(Pat_DOS)
print(Pat_DOB)

# ------------------------

# 07 Multiple Variables & One Values
e = f = g = "Sundar"
print(e)
print(f)
print(g)

# ------------------------

# 08 Unpacking
# Assigning Values to Independent Variables from a List/Tuple
Pat_Demo = ["Shyam", "05/01/1995", "05/10/1920"]
LPat_Name, LPat_DOS, LPat_DOB = Pat_Demo
print(LPat_Name)
print(LPat_DOS)
print(LPat_DOB)

# ------------------------

# 09 Printing Output Value
FName = "Shyam "
LName = "Sundar "
SName = "Shankar"

# Generic printing of Output value
print(FName)
# Combining/Concatenating Multiple Variables Using +
print(FName + LName + SName)
# Combining/Concatenating Multiple Variables Using , (Automatically Adds Space)
print(FName, LName, SName)

# ------------------------

# 10 Global Variables
# Variables would be Global by default &  It should be declared as Global when we want to use a Variable inside a Function
global MName
MName = "Sundar"

# ------------------------

# 11 Data Types
# 11.01 - Text:	str
# String can be stored in a Variable with Double Quotes, Single Quotes & 3 Double Quotes
h = 5
i = "5"
j = '5'
k = """Multiline Data
Multiline Data
Multiline Data
Multiline Data
"""
print(h)
print(i)
print(j)
print(k)

# ------------------------

# 11.01.01 - String Arrays


# ------------------------

# 11.01.02 - In String (Check Value inside a String)


# ------------------------

# 11.01.03 - Not In String (Check Value not inside a String)


# ------------------------

# 11.01.04 - String Slicing


# ------------------------

# 11.01.05 - String Slicing From Start


# ------------------------

# 11.01.06 - String Slicing To End


# ------------------------

# 11.02 - Numeric:	int, float, complex


# ------------------------

# 11.03 - Sequence:	list, tuple, range
# 11.04 - Mapping:	dict
# 11.05 - Boolean:	bool

# 12 - Inbuilt Functions/Formulas

# 11.01.08 - Upper
# 11.01.09 - Lower
# 11.01.10 - String Slicing To End
