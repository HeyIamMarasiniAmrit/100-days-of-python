import re
email = input("Whats your email?").strip()

if re.search(".+@.edu",email):
    print("valid")
else:
    print("invalid")