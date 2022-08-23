#create a fake user registration system
#username >4& <25 char
#email should have @ char
#password should be equal confirm password

un=input("enter ur username:")
if len(un)>4 & len(un)<25:
    print('ur username is ',un)
else:
    print('username is not valid ')
em=input('enter ur email:')
if "@" in em:
    print('uremail is ',em)
else:
    print("invalid email")
pwd=input('enter ur password')
cfpwd=input("re enter ur password")
if pwd==cfpwd:
    print('ur password is correct:',pwd)

print("u r registered")
