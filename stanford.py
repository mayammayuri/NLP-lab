import nltk
from nltk import pos_tag, word_tokenize, RegexpParser
   

grammar= nltk.CFG.fromstring("""
S -> WH VP | WH NP ADJ | WH NP 
VP -> 'is' | VP NP
NP -> DT N | NP ADJ
ADJ -> 'dear'
DT -> 'your'
WH -> 'What' | WH VP
N -> 'name'

"""
)
# Example text
sample_text = ['What','is','your','name','dear']
parser=nltk.ChartParser(grammar)
for tree in parser.parse(sample_text):
    tree.draw()

