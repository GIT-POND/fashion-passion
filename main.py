import math

def main():
    # main()
    datatypes()
    print(f"slope: {slope(2, 3, 1)}") # preview

def multiply(x, y):
    '''
     This functon does x y z.
     param x: is base num
     param y: multiple
    '''
    return x * y

def datatypes():
    ANDREA_ETHNICITY = 'Hispanic'
    andrea = 24
    andrea_name = 'andrea'
    andrea_height = 66.5
    andrea_girl = True

    print(f"data: { andrea_name + ' was here' }, {andrea}, {andrea_height}, {andrea_girl}, {ANDREA_ETHNICITY + ' heritage'}")
    print(andrea_name, ANDREA_ETHNICITY)

    andrea_name = 'violet'
    print(andrea_name, ANDREA_ETHNICITY)

#preview ----
def slope(m, x, b): # y = mx+b
    y = (m * x) + b
    return y


main()