#       In python, functions can be passed as arguments to other functions, returned from functions, or assigned to variables
#       E.g.

def add_one(x):
    return x + 1

def apply_function(f, x):
    return f(x)

print(apply_function(add_one, 1))

#       Lambda functions
#   Lambda functions are small, nameless functions which are defined in the normal flow of the program, typically as they are needed

add_one = lambda x: x + 1 # NOQA E731
print(add_one(1))

#   We have assigned the lambda function to a variable, so we can see it more clearly, but we'd normally use it immediately. 
#   Most style guides (we'll come back to these later in the course) consider it bad style to assign a lambda to a variable. 
#   This is because the main point of lambdas in Python is to avoid having to name the function - it's a bit strange to do that and then give it a name. 
#   Because of this, if you find yourself wanting to name a lambda, just use a normal function instead.

#       Higher order functions 

#   Higher-order functions are functions that take another function as an argument or that return a function. 
#   One of the main uses of lambda functions is to create temporary functions to pass into higher-order functions.

def sum(data):
    result = 0
    for x in data:
        result = result + x
    return result

def maximum(data):
    result = 0
    for x in data:
        result = max(result, x)
    return result

#   These are really exactly the same algorithm, except that we change the binary operation done on the RHS of the statement in the loop
#   herefore combine these functions into one higher-order function.

def reduce(data, bin_op):
    result = 0
    for x in data:
        result = bin_op(result, x)
    return result


data = [1, 2, 3, 4, -1]
print(sum(data))
print(maximum(data))
print(reduce(data, max))
print(reduce(data, min))
print(reduce(data, lambda a, b: a + b))
print(reduce(data, lambda a, b: a * b))
print(reduce(data, lambda a, b: max(a, b)))
print(reduce(data, lambda a, b: min(a, b)))

#       Map, Filter, and reduce

#   Python has a number of higher-order functions built in, including map, filter and reduce. Note that the map and filter functions in Python use lazy evaluation. 
#   This means that values in an iterable collection are not actually calculated until you need them.

#       Map:
#   The map function, takes a function and applies it to each value in an iterable.
l = [1, 2, 3]

def add_one(x):
    return x + 1

# Returns a <map object> so need to convert to list
print(list(map(add_one, l)))
print(list(map(lambda x: x + 1, l)))

#       Filter
#   Like map, filter takes a function and applies it to each value in an iterable, keeping the value if the result of the function application is True.

l = [1, 2, 3]

def is_gt_one(x):
    return x > 1

# Returns a <filter object> so need to convert to list
print(list(filter(is_gt_one, l)))
print(list(filter(lambda x: x > 1, l)))

#       Reduce
#   The reduce function uses a function which accepts two values to accumulate the values in the iterable. 
from functools import reduce

l = [1, 2, 3]

def add(a, b):
    return a + b

print(reduce(add, l))
print(reduce(lambda a, b: a + b, l))

#       Use map and reduce to write a function that calculates the sum of the squares of the values in a list

from functools import reduce

def sum_of_squares(l):
    squares = map(lambda x: x * x, l)
    return reduce(lambda a, b: a + b, squares)
print(sum_of_squares([0]))
print(sum_of_squares([1]))
print(sum_of_squares([1, 2, 3]))
print(sum_of_squares([-1]))
print(sum_of_squares([-1, -2, -3]))

#       Assuming we're reading in these numbers from an input file, so they arrive as a list of strings.
from functools import reduce

def sum_of_squares(l):
    integers = map(int, l)
    squares = map(lambda x: x * x, integers)
    return reduce(lambda a, b: a + b, squares)

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))

#       Finally, like comments in Python, we'd like it to be possible for users to comment out numbers in the input file they give to our programme

from functools import reduce

def sum_of_squares(l):
    not_comments = filter(lambda x: x[0] != '#', l)
    integers = map(int, not_comments)
    squares = map(lambda x: x * x, integers)
    return reduce(lambda a, b: a + b, squares)

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))
print(sum_of_squares(['1', '2', '#100', '3']))