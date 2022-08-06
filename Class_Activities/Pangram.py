import string

def is_pangram(s):
    alphabet = string.ascii_lowercase
    s = s.lower()

    for i in s:
        if s[i] in alphabet:
            