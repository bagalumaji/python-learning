def is_palindrome_string(s):
    rev = ''
    for i in range(len(s) - 1, -1, -1):
        rev += s[i]
    if rev == s:
        print(s," is palindrome string")
    else:
        print(s, " is not palindrome string")


is_palindrome_string('aba')
