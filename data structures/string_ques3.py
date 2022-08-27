#import string
'''
msg="you are mine and i am yours , you are mine and i am yours , you are mine"
new_msg=msg.translate((","),string.punctuation)
print(new_msg,len(new_msg))
'''
from string import punctuation

msg='hh254775kh53425bhhhgg2233@#@3@$4'
for p in punctuation:
    msg=msg.replace(p,'')
    print(msg)