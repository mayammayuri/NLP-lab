text="In statistics, a central tendency ( or measure of central tendency ) is a central or typical value for a probability distribution . [ 1 ] It may also be called a center or ! location of the distribution . Colloquially , measures of central tendency are often called averages . The term central tendency dates from the late 1920s . The most common measures of central tendency are the arithmetic mean , the median , and the mode. A middle tendency can be calculated for either a finite set of values or for a theoretical distribution , such as the normal distribution . Occasionally authors use central tendency to denote the tendency of quantitative data to cluster around some central value . The central tendency of a distribution is ? typically contrasted with its dispersion or variability ; dispersion and central tendency are the often characterized properties of distributions . Analysis may judge whether data has a strong or a weak central tendency based on its dispersion ."
def calcfreq(mylist):
    freq={}
    for items in mylist:
        freq[items]=mylist.count(items)
    #for key,value in freq.items():
     #   print(key,":",value)
    return freq
content=text.split()
corpuslen=len(content)
print("corpus length is", corpuslen)
unigram=calcfreq(content)
unigram_probability=[]
for i in unigram.values():
    unigram_probability.append((i/corpuslen))
print(unigram_probability)

bigmatrix=[]
for i,word in enumerate(filtered_sentence):
    for ele in range(len(filtered_sentence)-1):
        temp=[]
        temp
        bigmatrix.append(nltk.FreqDist(filtered_sentence))
print(bigmatrix)

punctuations = '''()-[]{};:'"\,<>/@#$%^&*_~'''
without=[]
withscount=0
onlywith=[]
for eles in content:
    if eles not in punctuations:
        without.append(eles)
    if eles in punctuations:
        withscount=withscount+1
        onlywith.append(eles)

calcfreq(without)