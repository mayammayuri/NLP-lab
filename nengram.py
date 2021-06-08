from spellchecker import SpellChecker
from tabulate import tabulate

word=input("Give a word ")

def ngram(word):
    splitword=[char for char in word]
    res = [i + j +z for i, j , z in zip(splitword, splitword[1:],splitword[2:])]
    return res

wordbigram=ngram(word)
print("The bigram of given wordd is ",wordbigram)



spell = SpellChecker()
bestword=spell.correction(word)
print(spell.correction(word))
candidates=spell.candidates(word)
print("these are the candidates",candidates)

def editDistance(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)

    insertion=[]
    delition=[]
    insertion.append(editDistance(str1, str2, m, n-1))
    delition.append(editDistance(str1, str2, m-1, n))
    #print("Insertion",insertion)
    #print("deletion",delition)
    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert
                   editDistance(str1, str2, m-1, n),    # Remove
                   editDistance(str1, str2, m-1, n-1)    # Replace
                   )
    
 
splitword=[]
count=0
collection={}
for ele in candidates:
    splitword=ngram(ele)
    for i in splitword:
        if i in wordbigram:
            count=count+1
    collection[ele]=count
    count=0
    
    #print("the distace between word",str1,"and", str2,editDistance(str1, str2, len(str1), len(str2)))
str1=word
str2=bestword
print(collection)
print("The best word is ",bestword) #hello
print("The distance of best word is",collection[bestword]) #hllo
tablelist=[]
for num,letter in enumerate(bestword):
    for letter2 in word:
        if (num+1 < len(bestword) and num-1 >= 0):
            if letter==letter2:
                tablelist.append("same")
            elif letter2==bestword[num+1] and letter==letter2:
                tablelist.append("same")
            elif letter2==bestword[num+1]:
                new="insert--"+letter
                tablelist.append(new)
print(tablelist)



