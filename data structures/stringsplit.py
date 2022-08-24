msg="Love Hope Magic"
thought=input("enter ur thoughts about:")
words=msg.split()
print(words,len(words),"words found",thought)

v=input("enter ur sentece:")
word=v.split()
print(word,len(word),"words found")
words=v.split(",")
print(word,len(word))
words=v.split("is")
print(words,len(words))

print(v.split()[-3:])