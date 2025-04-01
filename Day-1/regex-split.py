import re 
string = "kavitha,barath,venu,jeevitha,kalyani,hema"
pattern = r","
split_txt = re.split(pattern,string)
print("split_text :", split_txt)