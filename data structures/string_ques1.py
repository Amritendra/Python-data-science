#wap to count all the alphabts in astring
#nd display the output like
#a-3
#b-4..............
str="we strive for excellence"
for i in str:
    print(i,str.lower().count(i))

from string import ascii_lowercase

msg="life before death,love hope nd magic"
for char in ascii_lowercase:
    print(f'{char}-{msg.count(char)}')