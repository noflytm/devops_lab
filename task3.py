"""3.	You need to check Vasya Pupkin's homework in which he wrote equality.
For example, a record like “2 + 3 = 5” is correct.“23 * 7 = 421” is incorrect, but valid.
A valid record is a sequence: number, operation ("+", "-", "*", "/"), number, equal sign, number.
A number is a sequence of one or more decimal digits, before which there can be one minus sign.
There are no spaces in the valid expression entry.
If the record does not comply with the described rule, then it is considered an error.
For example, the entries “2 * = 3”, ''173 `` and ''2 + 2 = a” are errors.
Print “YES” if the record is correct. “NO”  if valid, but incorrect.
 And “ERROR” if there are errors in the record
"""

# Import regular expression
import re


# check vailid user equality
def validchecker(seq):
    result = re.match(r'[\d+*\-/\d=\d\s]', seq)
    if result:
        return True
    return False


# check correct user equality
def correctchecker(seq):
    equal = seq.split('=')
    correct = eval(equal[0])
    if correct == int(equal[1]):
        return True
    return False


# wrote user equality
seq = input()

# Output YES
if validchecker(seq) and correctchecker(seq):
    print('YES')
# Output ERROR
elif not validchecker(seq):
    print('ERROR')
# Output No
elif validchecker(seq) and not correctchecker(seq):
    print('NO')
