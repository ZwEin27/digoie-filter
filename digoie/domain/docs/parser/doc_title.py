
from nltk.tokenize import word_tokenize
from digoie.core.nltk import stopword
from digoie.core.nltk import stem
import string
from digoie.utils import str_helper

import re

def parse(title):
    # print title
    # print word_tokenize(title)
    

    
    ans = []
    

    title_contents = []
    if isinstance(title, basestring):
        title_contents.append(title)
    else:
        title_contents = title

    stop = stopword.get_stopwords()
    tokens = []

    

    for content in title_contents:
        tmp = [stem.stemming(word) for word in word_tokenize(content.lower()) if word not in stop and not str_helper.hasNumbers(word)]
        tokens.extend(tmp)

    has_special = False
    for token in tokens:
        if str_helper.hasSpecial(token):
            if not has_special:
                ans.append('digoie_docs_title_contain_special')
                has_special = True
        else:
            """
            if not str_helper.hasPunctuation(token):
                ans.append(token)
            """
    print ans


def generate_topic_tokens():
    tokens = []
    return tokens


