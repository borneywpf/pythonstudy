# /usr/bin/env python

import re

# print "9 errors, 201 warnings"
print re.match('[0-9]*', '3453').group(0)
print re.match('[0-9]*\s.', '3453 ]').group(0)
print re.match('[0-9]*\serrors,', '9 errors,').group(0)

print re.match('[0-9]*\serrors,\s[0-9]*\s', '9 errors, 201 ').group(0)
if re.match('[0-9]*\serrors,\s[0-9]*\swarnings', '9 errors, 201 warnings') != None:
    print re.match('[0-9]*\serrors,\s[0-9]*\swarnings', '9 errors, 201 warnings').group(0)
