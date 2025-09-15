# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return 0
maximo_total = max_of_two(9,5)
#print(f"Retorna: {maximo_total}")

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if (x>y) and (x>z):
        return x
    elif (y>z) and (y>x):
        return y
    elif (z>x) and (z>y):
        return z
    else:
        return 0
maximo_total_2 = max_of_three(8, 6, 4)
#print(f"Retorna: {maximo_total_2}")
   
