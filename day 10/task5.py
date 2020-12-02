import re
print(bool(re.match('^[A-Z]+$', '123aAbc')))
print(bool(re.match('^[A-Z]+$', 'ABC')))