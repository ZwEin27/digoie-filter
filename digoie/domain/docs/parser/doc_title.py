
from nltk.tokenize import word_tokenize
from digoie.core.nltk import stopword
from digoie.core.nltk import stem
from digoie.utils import string
# import string as pstr
# import re

def parse(title):
    # print title
    # print word_tokenize(title)
    
    # puncs = pstr.punctuation
    stop = stopword.get_stopwords()
    tokens = [stem.stemming(word) for word in word_tokenize(title.lower()) if word not in stop and not string.hasNumbers(word)]


