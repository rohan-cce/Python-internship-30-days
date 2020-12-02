import re
def re_fun(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(re_fun("ABCDEFabcdef123450")) 
print(re_fun("*&%@#!}{"))
