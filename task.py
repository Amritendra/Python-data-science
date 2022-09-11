from helper import read
data=read('pride_n_prejudice.txt')
# 1.count all the words in the file
words=data.split()
print(f'number of all the words in the file:{len(words)}')

#2.count the occurance of different conjuctions in the file
#3.count all the lines in the file
counter=0
lines=data.split("\n")
for i in lines:
    if i:
        counter +=1

print(f"total number of lines:{counter}")

#3.display the top 100 words that occur in the file

def clean(data):
    from string import punctuation
    for p in punctuation:
        data=data.replace(p,'')
    return data

def word_count(words):
    wordcount={}
    for w in set(words):
        wordcount[w]=words.count(w)
    return wordcount


words=clean(data).lower().split()
wc=word_count(words)
wc=sorted(wc.items(),key=lambda d:d[-1])
print(wc[-100:])
        


