# Shalev Gabay
# Targil 1:

def make_power(b,p): # Make tuple (b,p) - Immutible type
    def dispatch(x):
        if x==1:
            return b
        if x==2:
            return p
    return dispatch # Returns dispatch func

def base(x): # return Base of x
    return x(1)

def power(x): # return Power of X
    return x(2)

def print_power(x):
    if type(x) is int: # if x i int it print the number
        print(x)
    elif power(x) == 1: # if power of x is 1 it's print only the base
        print(base(x))
    elif power(x) == 0: # if power of x is 0 it's print 1
        print(1)
    else: # if it's not int, and the power isn't 1/0 so it's must be tuple.
        print(base(x),'^',power(x))



def calc_power(x): # calc the b^p
    return base(x)**power(x)

def mul_power(x,y):
    if base(x) == base(y): # if the bases are equals it's make b^(p1+p2)
        return make_power(base(x),power(x)+power(y))
    return calc_power(x)*(calc_power(y)) # return b1^p1 * b2^p2

def div_power(x,y):
    if base(x) == base(y): # if the bases are equals it's make b^(p1-p2)
        if calc_power(x) < calc_power(y):
            return make_power(base(x),-1)
        if power(x)>power(y):
            return make_power(base(x),power(x)-power(y))
        else:
            return make_power(base(x), power(y) - power(x))
    return calc_power(x)//calc_power(y) # return x//y

def improve_power(x):
    y=1
    while y<base(x): # loop until y large then b (base of x)
        for i in range(0,20): # check the index until 20, in the work 15 is the max
            if calc_power(x) == y**(power(x)*i): # check if the calc's are equals
                return make_power(y,(power(x)*i)) # return new tuple of [y, power(x) * i]
        y+=1
    print("No Number Exist!") # if there is no improvement so it's send appropriate message


# Main:

x=make_power(4,5) # Make Power X
print(x) # <function make_power.<locals>.dispatch at 0x10a509c10>
print(base(x)) # 4
print(power(x))# 5
print_power(x)# 4 ^ 5
print_power(improve_power(x)) # 2 ^ 10
print_power(mul_power(improve_power(x),make_power(2,5))) # 2 ^ 15
y=make_power(9,2) # Make Power Y
print_power(mul_power(x,y)) # 82944
print_power(mul_power(improve_power(y),make_power(3,5))) # 3 ^ 9
print_power(div_power(improve_power(y),make_power(3,5))) # 3 ^ -1
print_power(div_power(mul_power(make_power(2,3),make_power(2,8)), make_power(2,4))) # 2 ^ 7
print_power(div_power(mul_power(improve_power(make_power(8,1)), improve_power(make_power(256,1))),improve_power(make_power(16,1)))) # 2 ^ 7
print_power(make_power(12,1)) # 12
print_power(make_power(12,0)) # 1