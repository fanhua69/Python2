firststring = "abcdef"
secondstring = "ghijkl"
thirdstring = "a"

string = "abcdef"

print("Original string: ", string)
translation = string.maketrans(firststring,secondstring,thirdstring)
print("translated string:", string.translate(translation))

