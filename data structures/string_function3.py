#strng validation
val=input('enter ur name:')
if val.startswith('mr.'):
    print("welcome sir")
elif val.startswith("ms."):
    print('welcome maam')
elif val.startswith('dr.'):
    print('welcome doctor')
else:
    print("u are not invited,fokat me khana nhi milega")

