import re

def remove_vowels(s):
    pattern = r'[aeiouAEIOU]'
    return re.sub(pattern, '', s)
input_string = input()
output_string = remove_vowels(input_string)
print(output_string)  
