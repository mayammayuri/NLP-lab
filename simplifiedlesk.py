from nltk.corpus import wordnet as wn
import time

sentence=['I','went','to','the','bank','to','deposit','money']
sense={}
word="bank"
sensenumber=0
for ss in wn.synsets('bank'):
    sensenumber=sensenumber+1
    sense[sensenumber]=ss.definition()
def GetMaxFlox(flows):
    return max((len(v), k) for k,v in flows.items())
def computeoverlap(sentence,sense):
    PINE={}
    PINE=sense
    CONE=sentence
    count={}
    inc=0
    incp=0
    con=0
    for pine in PINE.values():
        incp=incp+1
        pword=pine.split()
        for cword in CONE:
            inc=inc+1
            for elep in pword:
                for elec in cword:
                    con=con+1
                    if elep==elec:
                            count[str(incp)+"th sense in wordnet "+"and word " +str(cword)]=str(count.get(str(incp)+"of pine"+"and"+str(inc)+"of cone"))+"||"+elep+" "+elec
    return(GetMaxFlox(count))


def simplified_lesk(word,sentence,sense):
    best_sense=0
    max_overlap=0
    context=['bank','deposit','money']
    print(computeoverlap(sentence,sense))
    result=computeoverlap(sentence,sense)
    sensenumber=result[0]
    print("the sense from wordnet is",sense.get(int(sensenumber)))

start = time.time()

simplified_lesk(word,sentence,sense)
end = time.time()
print(f"Runtime of the program is {end - start}")
