# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, multiplier = 1):
    # Write your code here.
    sum = 0
    for el in array:
        if type(el) is list:
            sum += productSum(el, multiplier + 1)
        else:
            sum += el
    return sum * multiplier
    
