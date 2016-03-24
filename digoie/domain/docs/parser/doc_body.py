
from nltk.tokenize import sent_tokenize
from digoie.utils import str_helper
from nltk.tokenize import word_tokenize
from digoie.core.nltk import stopword
from digoie.core.nltk import stem
from nltk.tag import pos_tag

def parse(body):
    
    contents = []
    if isinstance(body, basestring):
        contents.append(body)
    else:
        contents = body

    sentences = []
    for content in contents:
        sentences.extend([sentence for sentence in sent_tokenize(content) if not str_helper.hasHTMLTag(sentence)])
        
    stop = stopword.get_stopwords()
    tokens = {}

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word not in stop and not str_helper.hasNumbers(word) and not str_helper.hasPunctuation(word):
                word = stem.stemming(word)
                tokens.setdefault(word, 0)
                tokens[word] += 1

    wp = pos_tag(tokens.keys())
    words = [row[0] for row in wp]
    tags = [row[1] for row in wp]

    return words, tags

