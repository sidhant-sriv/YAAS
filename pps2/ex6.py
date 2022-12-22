import re
n = input()
def check_string(s):
    if len(s) < 10:
        return False

    first_half = s[:len(s)//2]
    if not re.match(r'^[a-zA-Z]+$', first_half):
        return False

    if not re.match(r'^[a-zA-Z]$', s[-1]):
        return False

    rest_of_string = s[len(s)//2:-1]
    if not re.match(r'^[0-9]+$', rest_of_string):
        return False

    return True

if check_string(n):
    print('valid')
else:
    print('invalid')
