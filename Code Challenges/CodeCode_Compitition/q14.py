"""

Let f(x,y) is defined for x,y belongs N and satisfies f(x,y) = x 
f(x,x+y) = (1+x/y) * f(x,y)
f(x,y) = f(y,x) , then find f(52,14) is :

"""

def f(x,y):
    if x == y:
        return x
    elif x < y:
        return f(y,x)
    else:

        return (1 + x/y) * f(x-y, y)

print(f(52,14))
