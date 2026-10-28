print(not True and False)       # not goes first: not True is False; False and False is False
print(True or False and False)  # and goes before or: False and False is False; True or False is True
print(not (5 > 3))              # parentheses first: 5 > 3 is True; not True is False
print(10 == 10 and 4 != 4)      # 10 == 10 is True; 4 != 4 is False; True and False is False
print(not False or not True)    # not False is True; not True is False; True or False is True