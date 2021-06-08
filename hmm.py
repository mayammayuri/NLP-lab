import nltk
import numpy as np
import pandas as pd
import random
from sklearn.model_selection import train_test_split
import pprint, time

class hmm:
    def omission(cpd_tagwords):
        print(cfd_tagwords)            
        print("The probability of an adjective (JJ) being 'new' is", cpd_tagwords["JJ"].prob("new"))
        print("The probability of a verb (VB) being 'duck' is", cpd_tagwords["VB"].prob("duck"))
    

brown_tags_words = [ ]
for sent in brown.tagged_sents():
    # sent is a list of word/tag pairs
    # add START/START at the beginning
    brown_tags_words.append( ("START", "START") )
    # then all the tag/word pairs for the word/tag pairs in the sentence.
    # shorten tags to 2 characters each
    brown_tags_words.extend([ (tag[:2], word) for (word, tag) in sent ])
    # then END/END
    brown_tags_words.append( ("END", "END") )

# conditional frequency distribution
cfd_tagwords = nltk.ConditionalFreqDist(brown_tags_words)
# conditional probability distribution
cpd_tagwords = nltk.ConditionalProbDist(cfd_tagwords, nltk.MLEProbDist)
hmm=hmm()
hmm.omission(cpd_tagwords)
