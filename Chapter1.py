import sys


#  Print Statement
# The print statement is used to display output on the console.
print("My name is Muhammad")

# Varialbes
# Variables are used to store data values. Each variable has a name and a value.
name = "Muhammad"
age = 32
price = 9.99
is_active = True
current_year = None

# Print Statement with Variables
# You can print variables along with text using commas or f-strings.

# Method 1: Using commas
# Commas separate values and automatically add spaces between them.
print("My name is", name, "and I am", age, "years old.")

# Method 2: Using f-strings
# f-strings allow you to embed variables directly inside strings using curly braces {}.
print(f"My name is {name} and I am {age} years old.")

# type() function
# The type() function returns the data type of a variable.
print(type(name))         # Output: <class 'str'>
print(type(age))          # Output: <class 'int'>
print(type(price))        # Output: <class 'float'>
print(type(is_active))    # Output: <class 'bool'>
print(type(current_year)) # Output: <class 'NoneType'>

# Type Conversion
# Type conversion means changing the data type of a value to another type.

# Converting int to float
# Converts an integer to a floating-point number.
age_float = float(age)
print(age_float)          # Output: 32.0

# Converting float to int
# Converts a floating-point number to an integer (removes decimal part).
price_int = int(price)
print(price_int)         # Output: 9

# Converting int to str
# Converts an integer to a string.
age_str = str(age)
print(age_str)          # Output: "32"

# Converting str to int
# Converts a string containing digits to an integer.
age_from_str = int(age_str)
print(age_from_str)      # Output: 32

# Converting str to float
# Converts a string containing a decimal number to a float.
price_from_str = float("19.99")
print(price_from_str)    # Output: 19.99

#type conversion with error handling
# Error handling is used to prevent the program from crashing if conversion fails.

# Safe str conversion function
# Converts any value to string, handles unexpected errors.
def safe_str_conversion(value):
    try:
        return str(value)
    except Exception as e:
        print(f"Error: {e}")
        return None

print(safe_str_conversion(123))        # Output: "123"
print(safe_str_conversion(45.67))      # Output: "45.67"
print(safe_str_conversion(True))       # Output: "True"
print(safe_str_conversion(None))       # Output: "None"
print(safe_str_conversion([1, 2, 3])) # Output: "[1, 2, 3]"
print(safe_str_conversion({"key": "value"})) # Output: "{'key': 'value'}"
print(safe_str_conversion((1, 2)))     # Output: "(1, 2)"
print(safe_str_conversion(set([1, 2, 3]))) # Output: "{1, 2, 3}"
print(safe_str_conversion(b'bytes'))   # Output: "b'bytes'"
print(safe_str_conversion(complex(1, 2))) # Output: "(1+2j)"
print(safe_str_conversion(lambda x: x)) # Output: "<function <lambda> at ...>"
print(safe_str_conversion(float('nan'))) # Output: "nan"
print(safe_str_conversion(float('inf'))) # Output: "inf"
print(safe_str_conversion(float('-inf'))) # Output: "-inf"
print(safe_str_conversion(object()))    # Output: "<object object at ...>"
print(safe_str_conversion(Exception("error"))) # Output: "error"
print(safe_str_conversion(range(5)))   # Output: "range(0, 5)"
print(safe_str_conversion(bytearray(b'byte array'))) # Output: "bytearray(b'byte array')"
print(safe_str_conversion(memoryview(b'memory view'))) # Output: "<memory at ...>"
print(safe_str_conversion(frozenset([1, 2, 3]))) # Output: "frozenset({1, 2, 3})"
print(safe_str_conversion(type))       # Output: "<class 'type'>"
print(safe_str_conversion(sys))        # Output: "<module 'sys' (built-in)"
print(safe_str_conversion(object))     # Output: "<class 'object'>"
print(safe_str_conversion(print))      # Output: "<built-in function print>"
print(safe_str_conversion(len))        # Output: "<built-in function len>"
print(safe_str_conversion(id))         # Output: "<built-in function id>"
print(safe_str_conversion(dir))        # Output: "<built-in function dir>"
print(safe_str_conversion(help))       # Output: "<function help at ...>"
print(safe_str_conversion(type(None))) # Output: "<class 'NoneType'>"
print(safe_str_conversion(type(True))) # Output: "<class 'bool'>"
print(safe_str_conversion(type(123)))  # Output: "<class 'int'>"
print(safe_str_conversion(type(45.67))) # Output: "<class 'float'>"
print(safe_str_conversion(type("string"))) # Output: "<class 'str'>"
print(safe_str_conversion(type([])))   # Output: "<class 'list'>"
print(safe_str_conversion(type(())))   # Output: "<class 'tuple'>"
print(safe_str_conversion(type({})))   # Output: "<class 'dict'>"
print(safe_str_conversion(type(set()))) # Output: "<class 'set'>"
print(safe_str_conversion(type(range(5)))) # Output: "<class 'range'>"
print(safe_str_conversion(type(bytearray()))) # Output: "<class 'bytearray'>"
print(safe_str_conversion(type(memoryview(b'')))) # Output: "<class 'memoryview'>"
print(safe_str_conversion(type(frozenset()))) # Output: "<class 'frozenset'>"
print(safe_str_conversion(type(lambda x: x))) # Output: "<class 'function'>"
print(safe_str_conversion(type(Exception))) # Output: "<class 'type'>"
print(safe_str_conversion(type(sys)))  # Output: "<class 'module'>"
print(safe_str_conversion(type(object))) # Output: "<class 'type'>"
print(safe_str_conversion(type(print))) # Output: "<class 'builtin_function_or_method'>"
print(safe_str_conversion(type(len)))  # Output: "<class 'builtin_function_or_method'>"
print(safe_str_conversion(type(id)))   # Output: "<class 'builtin_function_or_method'>"
print(safe_str_conversion(type(dir)))  # Output: "<class 'builtin_function_or_method'>"
print(safe_str_conversion(type(help))) # Output: "<class 'function'>"
print(safe_str_conversion(type(type))) # Output: "<class 'type'>"

# Safe int conversion function
# Tries to convert a value to int, prints error if it fails.
def safe_int_conversion(value):
    try:
        return int(value)
    except ValueError:
        print(f"Error: Cannot convert {value} to int.")
        return None

print(safe_int_conversion("abc"))  # Output: Error message and None
print(safe_int_conversion("100"))  # Output: 100
print(safe_int_conversion("   42   "))  # Output: 42
print(safe_int_conversion("45.67"))  # Output: Error message and None
print(safe_int_conversion("12abc34"))  # Output: Error message and None
print(safe_int_conversion(""))  # Output: Error message and None
print(safe_int_conversion("0x1A"))  # Output: Error message and None
print(safe_int_conversion("NaN"))  # Output: Error message and None
print(safe_int_conversion("Infinity"))  # Output: Error message and None
print(safe_int_conversion("True"))  # Output: Error message and None
print(safe_int_conversion("False"))  # Output: Error message and None
print(safe_int_conversion("None"))  # Output: Error message and None

# Safe float conversion function
# Tries to convert a value to float, prints error if it fails.
def safe_float_conversion(value):
    try:
        return float(value)
    except ValueError:
        print(f"Error: Cannot convert {value} to float.")
        return None

print(safe_float_conversion("abc"))    # Output: Error message and None
print(safe_float_conversion("19.99"))  # Output: 19.99
print(safe_float_conversion("   45.67   "))  # Output: 45.67
print(safe_float_conversion("100"))    # Output: 100.0
print(safe_float_conversion("12.34abc"))  # Output: Error message and None
print(safe_float_conversion(""))       # Output: Error message and None
print(safe_float_conversion("NaN"))    # Output: nan
print(safe_float_conversion("Infinity")) # Output: inf
print(safe_float_conversion("-Infinity")) # Output: -inf
print(safe_float_conversion("0x1A"))   # Output: Error message and None
print(safe_float_conversion("True"))   # Output: Error message and None
print(safe_float_conversion("False"))  # Output: Error message and None
print(safe_float_conversion("None"))   # Output: Error message and None
print(safe_float_conversion("1e10"))   # Output: 10000000000.0
print(safe_float_conversion("3.14e-2")) # Output: 0.0314
print(safe_float_conversion("  -123.456  ")) # Output: -123.456
print(safe_float_conversion("0.0"))    # Output: 0.0
print(safe_float_conversion("-.5"))    # Output: -0.5
print(safe_float_conversion(".75"))    # Output: 0.75
print(safe_float_conversion("1_000.50")) # Output: 1000.5
print(safe_float_conversion("2.5e+3"))  # Output: 2500.0
print(safe_float_conversion("3.4028235e+38")) # Output: 3.4028235e+38
print(safe_float_conversion("1.7976931348623157e+308")) # Output: 1.7976931348623157e+308
print(safe_float_conversion("5e-324"))  # Output: 5e-324
print(safe_float_conversion("1.0e+309")) # Output: inf
print(safe_float_conversion("-1.0e+309")) # Output: -inf
print(safe_float_conversion("3.14.15")) # Output: Error message and None
print(safe_float_conversion("1,000.50")) # Output: Error message and None
print(safe_float_conversion("ten"))     # Output: Error message and None
print(safe_float_conversion("1/2"))    # Output: Error message and None
print(safe_float_conversion("0b101"))   # Output: Error message and None
print(safe_float_conversion("0o12"))    # Output: Error message and None
print(safe_float_conversion("0xA"))     # Output: Error message and None
print(safe_float_conversion("3.14f"))   # Output: Error message and None
print(safe_float_conversion("infinit"))  # Output: Error message and None
print(safe_float_conversion("null"))    # Output: Error message and None

# Safe boolean conversion function
# Converts certain string values to boolean True or False, else prints error.
def safe_bool_conversion(value):
    if value in ["True", "true", "1"]:
        return True
    elif value in ["False", "false", "0"]:
        return False
    else:
        print(f"Error: Cannot convert {value} to boolean.")
        return None

print(safe_bool_conversion("True"))   # Output: True
print(safe_bool_conversion("False"))  # Output: False
print(safe_bool_conversion("1"))      # Output: True
print(safe_bool_conversion("0"))      # Output: False
print(safe_bool_conversion("yes"))    # Output: Error message and None

# Safe None conversion function
# Checks if value is None or string "None", else prints error and returns value.
def safe_none_conversion(value):
    if value is None or value == "None":
        return None
    else:
        print(f"Error: Cannot convert {value} to None.")
        return value

print(safe_none_conversion(None))     # Output: None
print(safe_none_conversion("None"))   # Output: None
print(safe_none_conversion("abc"))    # Output: Error message and "abc"

# Type Casting
# Type casting is converting a variable from one type to another.

# Converting variables to string
# str() converts any value to string.
name_str = str(name)          # Convert name to string (already is)
age_str = str(age)            # Convert age to string
price_str = str(price)        # Convert price to string
is_active_str = str(is_active) # Convert is_active to string
current_year_str = str(current_year) # Convert current_year to string
print(f"Name: {name_str}, Age: {age_str}, Price: {price_str}, Active: {is_active_str}, Year: {current_year_str}")
print(type(name_str), type(age_str), type(price_str), type(is_active_str), type(current_year_str))

# Converting variables to int
# int() converts values to integer if possible.
name_int = int(name)            # Convert name to int (name cannot be converted)
age_int = int(age)              # Convert age to int (already is)
price_int = int(price)          # Convert price to int (float to int)
is_active_int = int(is_active)  # Convert is_active to int (bool to int)
current_year_int = int(current_year) # Convert current_year to int (already is)
print(f"Name: {name_int}, Age: {age_int}, Price: {price_int}, Active: {is_active_int}, Year: {current_year_int}")
print(type(name_int), type(age_int), type(price_int), type(is_active_int), type(current_year_int))

# Converting variables to float
# float() converts values to floating-point number if possible.
name_float = float(name)          # Convert name to float (name cannot be converted)
age_float = float(age)            # Convert age to float (already is)
price_float = float(price)        # Convert price to float (already is)
is_active_float = float(is_active) # Convert is_active to float (bool to float)
current_year_float = float(current_year) # Convert current_year to float (already is)
print(f"Name: {name_float}, Age: {age_float}, Price: {price_float}, Active: {is_active_float}, Year: {current_year_float}")
print(type(name_float), type(age_float), type(price_float), type(is_active_float), type(current_year_float))

# Converting variables to bool
# bool() converts values to boolean. Non-empty/non-zero values are True.
name_bool = bool(name)            # Convert name to bool (non-empty string is True)
age_bool = bool(age)              # Convert age to bool (non-zero int is True)
price_bool = bool(price)          # Convert price to bool (non-zero float is True)
is_active_bool = bool(is_active)  # Convert is_active to bool (already is)
current_year_bool = bool(current_year) # Convert current_year to bool (non-zero int is True)
print(f"Name: {name_bool}, Age: {age_bool}, Price: {price_bool}, Active: {is_active_bool}, Year: {current_year_bool}")
print(type(name_bool), type(age_bool), type(price_bool), type(is_active_bool), type(current_year_bool))

# Converting variables to None
# None is a special value representing "no value". Here, variables are set to None if they are empty/zero.
name_none = None if name else None            # Convert name to None (non-empty string is not None)
age_none = None if age else None              # Convert age to None (non-zero int is not None)
price_none = None if price else None          # Convert price to None (non-zero float is not None)
is_active_none = None if is_active else None  # Convert is_active to None (True is not None)
current_year_none = None if current_year else None # Convert current_year to None (non-zero int is not None)
print(f"Name: {name_none}, Age: {age_none}, Price: {price_none}, Active: {is_active_none}, Year: {current_year_none}")
print(type(name_none), type(age_none), type(price_none), type(is_active_none), type(current_year_none))

# Keywords in Python
# Keywords are reserved words in Python that have special meaning and cannot be used as variable names.

# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield

# Note: Keywords are case-sensitive and cannot be used as variable names.

#Operators in Python
# Operators are special symbols used to perform operations on values and variables.

# Arithmetic Operators: +, -, *, /, %, **, //
# Used for mathematical calculations.
# Comparison Operators: ==, !=, >, <, >=, <=
# Used to compare values.
# Logical Operators: and, or, not
# Used to combine conditional statements.
# Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=
# Used to assign values to variables.
# Membership Operators: in, not in
# Used to check if a value is present in a sequence.
# Identity Operators: is, is not
# Used to compare memory locations of two objects.
# Bitwise Operators: &, |, ^, ~, <<, >>
# Used to perform operations on binary numbers.
# Ternary Operator: value_if_true if condition else value_if_false
# Used for conditional expressions.

#Operators examples
# Examples of how each operator works.

# Arithmetic Operators
a = 10
b = 3
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.3333333333333335
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 1000
print(a // b) # Floor Division: 3

# Comparison Operators
print(a == b)  # Equal: False
print(a != b)  # Not Equal: True
print(a > b)   # Greater Than: True
print(a < b)   # Less Than: False
print(a >= b)  # Greater Than or Equal: True
print(a <= b)  # Less Than or Equal: False

# Logical Operators
x = True
y = False
print(x and y) # Logical AND: False
print(x or y)  # Logical OR: True
print(not x)   # Logical NOT: False

# Assignment Operators
c = 5
c += 2  # Equivalent to c = c + 2
print(c)  # Output: 7
c *= 3  # Equivalent to c = c * 3
print(c)  # Output: 21
c -= 4  # Equivalent to c = c - 4
print(c)  # Output: 17
c /= 2  # Equivalent to c = c / 2
print(c)  # Output: 8.5
c %= 3  # Equivalent to c = c % 3
print(c)  # Output: 2.5
c **= 2 # Equivalent to c = c ** 2
print(c)  # Output: 6.25
c //= 2 # Equivalent to c = c // 2
print(c)  # Output: 3.0

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 not in my_list)  # Output: True
print(10 in my_list)  # Output: False

# Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)  # Output: False (different objects)
print(x is z)  # Output: True (same object)
print(x == y)  # Output: True (same values)

# Bitwise Operators
p = 5  # Binary: 0101
q = 3  # Binary: 0011
print(p & q)  # Bitwise AND: 1 (Binary: 0001)
print(p | q)  # Bitwise OR: 7 (Binary: 0111)
print(p ^ q)  # Bitwise XOR: 6 (Binary: 0110)
print(~p)     # Bitwise NOT: -6 (Binary: ...11111010)
print(p << 1) # Left Shift: 10 (Binary: 1010)
print(p >> 1) # Right Shift: 2 (Binary: 0010)

# Ternary Operator
# The ternary operator is a one-line if-else statement.
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"{name} is an {status}.")

# Note: Python does not have a specific operator for string concatenation. The + operator can be used to concatenate strings.

# Take input from user
# input() is used to get input from the user. The value is always a string, so you may need to convert it.
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_price = float(input("Enter the price: "))
user_is_active = input("Is the user active? (yes/no): ").strip().lower() == "yes"
user_current_year = int(input("Enter the current year: "))

print(f"User Name: {user_name}, Age: {user_age}, Price: {user_price}, Active: {user_is_active}, Year: {user_current_year}")

# Take input from user with error handling
# This function keeps asking for input until the user enters a valid value of the expected type.

def safe_input(prompt, expected_type):
    while True:
        user_input = input(prompt)
        try:
            if expected_type == int:
                return int(user_input)
            elif expected_type == float:
                return float(user_input)
            elif expected_type == bool:
                return user_input.strip().lower() in ["yes", "true", "1"]
            elif expected_type == str:
                return user_input
            else:
                print("Unsupported type.")
                return None
        except ValueError:
            print(f"Error: Please enter a valid {expected_type.__name__}.")

user_name = safe_input("Enter your name: ", str)
user_age = safe_input("Enter your age: ", int)
user_price = safe_input("Enter the price: ", float)
user_is_active = safe_input("Is the user active? (yes/no): ", bool)
user_current_year = safe_input("Enter the current year: ", int)

print(f"User Name: {user_name}, Age: {user_age}, Price: {user_price}, Active: {user_is_active}, Year: {user_current_year}")

# Practice Problem
# This is a sample problem to practice the concepts learned above.

# Calculator Program with Error Handling
# This program performs basic arithmetic operations and handles errors like invalid input and division by zero.

def calculator():
    print("Welcome to the Calculator Program!")
    print("Available operations: +, -, *, /, %, **, //")
    
    while True:
        num1 = safe_input("Enter the first number (or 'exit' to quit): ", float)
        if num1 is None:
            break
        
        operator = input("Enter an operator: ").strip()
        if operator not in ['+', '-', '*', '/', '%', '**', '//']:
            print("Error: Invalid operator. Please try again.")
            continue
        
        num2 = safe_input("Enter the second number: ", float)
        if num2 is None:
            break
        
        try:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            elif operator == '%':
                result = num1 % num2
            elif operator == '**':
                result = num1 ** num2
            elif operator == '//':
                result = num1 // num2
            
            print(f"The result of {num1} {operator} {num2} is: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        
        continue_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_calculation != 'yes':
            break

    print("Thank you for using the Calculator Program!")

calculator()

# End of the program