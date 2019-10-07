# Define a function full_name to take in first and last name
def full_name(first_name, last_name):
    first_name = first_name.lower().capitalize()
    last_name = last_name.lower().capitalize()
    return first_name + ' ' + last_name


# Define a calculator_sum, to add 2 integers
def calculator_sum(integer_1, integer_2):
    integer_1 = int(integer_1)
    integer_2 = int(integer_2)
    sum = integer_1 + integer_2
    return sum

# Define a calculator_subtract, to subtract 2 integers
def calculator_subtract(integer_1,integer_2):
    integer_1 = int(integer_1)
    integer_2 = int(integer_2)
    subtract= integer_1 - integer_2
    return subtract

# Define a calculator_multiply, to multiply 2 integers
def calculator_multiply(integer_1, integer_2):
    integer_1 = int(integer_1)
    integer_2 = int(integer_2)
    multiply = integer_1 * integer_2
    return multiply

# Define a area_square, to multiply 2 integers
def area_square(length):
    length = int(length)
    area = length*length
    return area


# Define a area_triangle, to multiply 2 integers
def area_triangle(base, height):
    base=float(base)
    height=float(height)
    area=0.5*base*height
    return area

