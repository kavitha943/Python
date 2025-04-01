import re

text = "The quick fox is brown"
pattern = r"brown"
replacement = "red"
new_text = re.sub(pattern,replacement,text)
print ("new_string :", new_text)