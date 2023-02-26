""" Given that f(x) is a function define on R, satisfying f(1)=1 and for any x belongs to R, f(x+5) >= f(x) + 5
and f(x+1)<=f(x)+1. if g(x) = f(x) +5 - x, then g(2022) is equal to ?"""


def f(x):
    # this holds true for any value of x in f(x+1) and f(x+5)
    return x

# Define the function g
def g(x):
  return f(x) + 5 - x

# Find g(2022)
g_2022 = g(2022)

# Print the result
print("g(2022) =", g_2022)


