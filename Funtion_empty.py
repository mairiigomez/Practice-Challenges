"""Función empty
"""
def empty(x):
    """Check if the parameter is empty"""
    # If the argument x is true = Has something in it
    # and after taking away the blank spaces also has something
    # return False is not empty
    if x and x.strip():
        return False
    return True 

name=input()
print(empty(name))
