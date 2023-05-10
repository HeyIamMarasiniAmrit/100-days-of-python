import re
name = input("whats your name?").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first}  {last}"
print(f"hello, {name}")