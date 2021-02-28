"""A self-dividing number is a number that is divisible
by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0,
 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible
self dividing number, including the bounds if possible.
"""

def checkdivide(inp):
    def selfcheck(sin):
        for num in str(sin):
            if num == '0' or sin % int(num) > 0:
                return False
        return True

    outputs = []
    for s in range(inp[0], inp[1] + 1):

        if selfcheck(s):
            outputs.append(s)
    return outputs


# Input values
inputnum = [int(x) for x in input().split(' ')]


# Print result of function
print(checkdivide(inputnum))
