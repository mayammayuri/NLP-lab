def calcfreq(mylist):
    freq={}
    for items in mylist:
        freq[items]=mylist.count(items)
    for key,value in freq.items():
        print(key,":",value)
f=open(r"F:\EBOOKS\Sixth sem\NLP\LAB\with.txt","r")
stop_words=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 
'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 
'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "thatll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 
'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 
'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 
'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 
'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 
'so', 'than', 'too', 'very','can', 'will', 'just', 'don', "don't", 'should', 'now', 
'y', 'ain', 'are', "aren't", 'couldn','didn','doesn', 
'isn', 'ma', 'mightn', 'mustn', 'needn', "neednt", "shant", 'shouldn', "shouldnt", 'wasn', "wasnt", 
'weren', "werent", 'won', "wont", 'wouldn', "wouldnt"]
content=""
stops=""
stopcount=0

for ele in f:
        content=content+ele

#with stop
stoparr=[]
contentx=content.split()
for i in contentx:
    if i in stop_words:
        stoparr.append(i)
        stopcount=stopcount+1
print("Number of tokens with punctuations", len(contentx))
calcfreq(contentx)
#without stop
print("Frequency of stopwords")
calcfreq(stoparr)
print("Number of stopwords", stopcount)

#without punctuation
print("")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
without=""
withscount=0
onlywith=''
for eles in content:
    if eles not in punctuations:
        without=without+eles
    if eles in punctuations:
        withscount=withscount+1
        onlywith=onlywith+eles
contentg=without.split()
print("Number of tokens without punctuations", len(contentg))
print("")
print("Number of punctuations",withscount)
print("Types of punctution found in text and their frequencies")
calcfreq(onlywith)