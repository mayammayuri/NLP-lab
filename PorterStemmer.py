from nltk.stem import *
stemmer=PorterStemmer()
example={
    "fly":"flies",
    "key":"keys",
    "run":"runs",
    "read":"reader",
    "paint":"painter",
    "bat":"bats",
    "sheep":"sheep",
    "head":"headed",
    "pony":"ponies"
}
f=open("LAB\with.txt","r+")
words=list(example.keys())
root_form=example.values()
rootformlist=list(example.values())
rootword=[stemmer.stem(word) for word in words]
correctwords=[]
incorrectwords=[]
incorrectkey=[]
i=0
for key,val in zip(root_form,rootword):
    if key==val:
        correctwords.append(val)
    else:
        incorrectwords.append(words[i])
        incorrectkey.append(rootformlist[i])
    i+=1
print("By porter stemmer")
print("incorrect key",incorrectwords)
print("incorrect words",incorrectkey)
print("correct ",correctwords)

def logic(word):
    suffix=["ly","s","er","d","ed","ied","y","hood"]
    
    if word.endswith("ies"):
            length=len("ies")
            return word[:len(word)-length]+"y"
    if word.endswith("ming"):
        length=len("ming")
        return word[:len(word)-length]
    elif word.endswith("ing"):
        length=len("ing")
        return word[:len(word)-length]
    else:
        for ele in suffix:
            if word.endswith(ele):
                    length=len(ele)
                    return word[:len(word)-length]

    
    return word
res=list(map(logic,incorrectkey))
print("total no of words",words)
print("\nwords",res)
inputword=input("\nenter the word")
inputroot=input("\n enter the root word of the above word")
print("\nporter is showing",stemmer.stem(inputword))
print("\nroot words of incoorect words are",logic(inputword))
if(inputroot==logic(inputword)):
    print("The function result is matching the actual root word")
if(inputroot==stemmer.stem(inputword)):
    print("porter stemmer is matching the actual root word")
