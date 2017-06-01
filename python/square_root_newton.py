def average(a, b):
    return (a + b) / 2.0

def improve(guess, x):
    return average(guess, x/guess)

def is_good_enough(guess, x, tolerance):
    d = abs(guess*guess - x)
    return (d < tolerance)

def _square_root(guess, x, tolerance):
    while(not is_good_enough(guess, x, tolerance)):
        guess = improve(guess, x)
    return guess

def square_root(x, tolerance):
    r = _square_root(1, x, tolerance)
    return r


print(square_root(4, 0.001))


