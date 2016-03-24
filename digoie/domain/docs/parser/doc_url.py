
from urlparse import urlparse
from nltk.tokenize import word_tokenize


def parse(url):
    
    o = urlparse(url)
    url_path_elements = o.path.split('/')
    # word_tokenize(url_path_elements[2])

    print url_path_elements