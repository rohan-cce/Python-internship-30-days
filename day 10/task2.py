import re
def ab_match(text):
        patterns = 'ab'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(ab_match("ac"))
print(ab_match("abc"))
print(ab_match("abbc"))