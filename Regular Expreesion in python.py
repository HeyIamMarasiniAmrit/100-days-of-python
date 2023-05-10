import re
pattern = "is"
text = '''The most viable troubleshooting action is to try installing the problematic package on the selected Python interpreter using the terminal. If you get an identical error message, then the problem is not in the IDE and you should review the rationales and typical cases, or search for a solution on the Internet.'''
match = re.search(pattern, text)
print(match)