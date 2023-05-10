email = input("Whats your email?").strip()

username, domain = email.split("@")

if username and domain.endwith(".edu"):
    print("valid")
else:
    print("invalid")