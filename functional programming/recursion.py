## Recuresion
#    Instead of using loops to iteratively apply an operation, we can express a result in terms of previous results. 
#   To do this, the function needs to call itself to get the previous result, this is called recursion.

#       Recursion and itteration do the same thing essentially

#       Iteration

def factorial(n):
    """Calculate the factorial of a given number.

    :param int n: The factorial to calculate
    :return: The resultant factorial
    """
    if n < 0:
        raise ValueError('Only use non-negative integers.')

    factorial = 1
    for i in range(1, n + 1): # iterate from 1 to n
        # save intermediate value to use in the next iteration
        factorial = factorial * i

    return factorial

print(factorial(5))

print(factorial(100))

#       Recursion
def factorial(n):
    """Calculate the factorial of a given number.

    :param int n: The factorial to calculate
    :return: The resultant factorial
    """
    if n < 0:
        raise ValueError('Only use non-negative integers.')

    if n == 0:
        return 1 # exit from recursion, prevents infinite loops
    else:
        return  n * factorial(n-1) # recursive call to the same function
    
print(factorial(100))

#   Recursion on trees

class Node(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.value = name
        self.children = children or []

    def __repr__(self):
        return f"Node({self.value}, {self.children})"

#    +
#   / \
#  1  *
#    / \
#   2   3
t = Node('+', [Node('1'),
               Node('*', [Node('2'),
                          Node('3')])])

def count_nodes(tree):
    """Count the number of nodes in a tree.

    :param Node tree: The tree to count the nodes of
    :return: The number of nodes in the tree
    """
    if not tree.children:
        return 1
    else:
        return 1 + sum(count_nodes(child) for child in tree.children)

def evaluate(tree):
    """Evaluate the result of a tree representing a mathematical expression.

    :param Node tree: The tree to evaluate
    :return: The result of the expression
    """
    if not tree.children:
        return int(tree.value)
    else:
        left = evaluate(tree.children[0])
        right = evaluate(tree.children[1])
        if tree.value == '+':
            return left + right
        elif tree.value == '-':
            return left - right
        elif tree.value == '*':
            return left * right
        elif tree.value == '/':
            return left / right
        else:
            raise ValueError(f"Unknown operator: {tree.value}")


print(evaluate(t))
print(count_nodes(t))

##  Recursion is a programming technique where a function calls itself, allowing solutions to problems that can be broken down into smaller subproblems
##  Recursion is a useful approach for calculation and operations on tree data structures.
