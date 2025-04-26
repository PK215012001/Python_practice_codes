# programme to check whether a given password is strong or not
import re
password = 'abc1234ghijk'
pattern1 = re.compile(r'(.)\1\1')
weak = pattern1.finditer(password)
for match in weak:
    print(match)