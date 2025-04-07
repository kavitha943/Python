import sys
a= int(sys.argv[1])
b= int(sys.argv[2])
less_than =  a<b
greater_than = a>b 
less_than_or_equalto = a<=b
greater_than_or_equalto = a>=b
not_equalto = a!=b
equalto = a==b
print("a < b :",less_than)
print("a > b :", greater_than)
print("a >= b :", greater_than_or_equalto)
print("a <= b:",less_than_or_equalto)
print("a != b :", not_equalto)
print("a == b :", equalto)