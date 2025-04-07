import sys
x = int(sys.argv[1])
y = int(sys.argv[2])

and_operation = x and y # Returns "Y" if both are truthy 
or_operation = x or y   # Returns first truthy 
not_x_operation = not x 
not_y_operation = not y
print("x and y :",and_operation)
print("x or y :",or_operation)
print(" not_x_operation :",not_x_operation)
print("not_operation : ",not_y_operation)