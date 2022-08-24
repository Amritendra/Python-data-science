# string validation function


v=input('enter the value:')

#test
if v.isnumeric():
    print("only numbers",v.isnumeric())
if v.isalpha():
    print("only alphaets",v.isalpha())
if v.isalnum():
    print("alphabets&nnumbers",v.isalnum())
if v.isspace():
    print("only spaces",v.isspace())
if v.isupper():
    print('uppercase alphabets',v.isupper())
if v.islower():
    print("lowercase alphabets",v.islower())
else:
    print('galat hai beta')
    

