
import json
import os

from digoie.domain.docs.doc import Doc
from digoie.conf.storage import __elastic_search_dir__

ES_DOC_SOURCE = '_source'
ES_DOC_URL = 'url'
ES_DOC_TITLE = 'hasTitlePart'
ES_DOC_BODY = 'hasBodyPart'
ES_DOC_TEXT = 'text'
    
def doc_parser(path=None):
    # filename = 'san-francisco-maria-sample.json'
    filename = 'san-francisco-maria.json'
    path = os.path.join(__elastic_search_dir__, filename)
    pn_file = open(path, 'rU')
    raw = json.load(pn_file)
    pn_file.close()
    hits = raw['hits']['hits']
    docs = []
    test = 1
    for hit in hits:
        try:
            source = hit[ES_DOC_SOURCE]

            if ES_DOC_SOURCE not in hit:
                # this contain nothing
                continue

            if ES_DOC_URL in source:
                doc_url = source[ES_DOC_URL]

            if ES_DOC_TITLE in source:
                doc_title = source[ES_DOC_TITLE][ES_DOC_TEXT]

            if ES_DOC_BODY in source:
                doc_body = source[ES_DOC_BODY][ES_DOC_TEXT]


            doc = Doc(doc_url, doc_title, doc_body)
            docs.append(doc)
            # break   # test one doc this time
            test += 1
            if test == 50:
                break

        except Exception as e: 
            print "ERROR: " + str(e)
            # print hit
            print 'hasBodyPart' in source

    return docs

