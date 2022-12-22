def longest_palindrome_substring(s):
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    odd_count = 0
    for count in char_count.values():
        if count % 2 == 1:
            odd_count += 1
    if odd_count > 1:
        return len(s) - odd_count + 1
    else:
        return len(s)
print(longest_palindrome_substring(input()))