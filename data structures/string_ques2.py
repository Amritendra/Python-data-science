#wap to find all the ooccurance of a word in a string and display its index
'''
from string import ascii_lowercase
msg="you are mine and i am yours , you are mine and i am yours , you are mine"
words=msg.split()
print(words)
start=0
for word in words:
    print(f"{word}-{words.count(word)}")
'''

msg="you are mine and i am yours , you are mine and i am yours , you are mine"
start=0
query="mine"
while True:
    idx=msg.find(query,start)
    if idx==-1:
        break
    print(f"{query} at {idx}")
    start=idx+1

