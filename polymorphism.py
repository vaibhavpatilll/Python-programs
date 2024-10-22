#  in-built polymorphic functions

# len() being used for a string
print(len("geeks"))

# len() being used for a list
print(len([10, 20, 30]))


# A simple Python function to demonstrate 
# Polymorphism

def add(x, y, z = 0): 
    return x + y+z

# Driver code 
print(add(2, 3))
print(add(2, 3, 4))
