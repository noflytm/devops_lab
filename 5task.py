"""A self-dividing number is a number that is divisible
by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0,
 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible
self dividing number, including the bounds if possible.
"""

def CheckDivide(input):
    def selfcheck(s):
        for num in str(s):
            if num == '0' or s % int(num) > 0:
                return False
        return True

    outputs = []
    for s in range(input[0], input[1] + 1):
        if selfcheck(s):
            outputs.append(s)
    return outputs


# Input values
input = [int(x) for x in input().split(' ')]


# Print result of function
print(CheckDivide(input))
