import pandas as pd


def calcfreq(mylist):
    freq={}
    for i,items in enumerate(mylist):
        freq[(i,items)]=mylist.count(items)
    for key,value in freq.items():
        print(key,":",value)

    return freq


doc1="Cosine similarity is a metric, helpful in determining, how similar the data objects are irrespective of their size."
doc2="Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space."
doc3="Cosine similarity is a metric used to measure how similar the documents are irrespective of their size."
doc=[doc1,doc2,doc3]
worddict={}
i=1
for ele in doc:
    words=ele.split(" ")
    data=calcfreq(words)
        
    i=i+1

df=pd.DataFrame(data)