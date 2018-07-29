#modules

#import cool_int
#import cool_int as ci #renaming modules

from cool_int import to_eng
from cool_int import awesome_student

# ci.to_eng(5)
# ci.to_eng(6)

to_eng(5)
to_eng(6)

# c = ci.awesome_student["city"]
c = awesome_student["city"]
print(c)

import platform
p = platform.system()
print(p)

#dir() - shows what is inside a module

# d = dir(platform)
# print(d)

# o = dir(ci)
# print(o)
