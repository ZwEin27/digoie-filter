from nltk.tokenize import word_tokenize
from digoie.core.nltk import stopword
from digoie.core.nltk import stem
import string
from digoie.utils import str_helper
import re


DTFTR_SPECIAL = 'DDTCS'  # digoie_docs_title_contain_special
DTFTR_DIGIT = 'DDTCD'    # digoie_docs_title_contain_digit

TITLE_FEATURES =    [
                        DTFTR_SPECIAL,
                        DTFTR_DIGIT
                    ]


def parse(title):
    print '\n\n\n'
    print title
    # print word_tokenize(title)
    
    ans = []
    features = generate_title_feature()
    # print features
    title_contents = []
    if isinstance(title, basestring):
        title_contents.append(title)
    else:
        title_contents = title

    stop = stopword.get_stopwords()
    tokens = []

    for content in title_contents:
        tokens.extend([stem.stemming(word) for word in word_tokenize(content.lower()) if word not in stop])

    for token in tokens:
        if str_helper.hasSpecial(token) and not features[DTFTR_SPECIAL]:
            # ans.append(DTFTR_SPECIAL)
            features[DTFTR_SPECIAL] = True
        if str_helper.hasNumbers(token) and not features[DTFTR_DIGIT]:
            # ans.append(DTFTR_SPECIAL)
            print token
            features[DTFTR_DIGIT] = True
        # else:
            """
            if not str_helper.hasPunctuation(token):
                ans.append(token)
            """

    print [k.lower() for (k,v) in features.items() if v]

    # print tokens


def generate_title_feature():
    features = {}
    for feature in TITLE_FEATURES:
        features.setdefault(feature, False)
    return features


