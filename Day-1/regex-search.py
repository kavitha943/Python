import re
string = "The quick fox is brown"
pattern = r"brown"
search = re.search(pattern,string)
if search:
    print("search found:", search.group())
else:
    print("search not found")