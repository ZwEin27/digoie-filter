
"""

Features
1. if title contain special
2. if title contain number (usually phone number)

"""




from digoie.domain.docs.parser import doc_url
from digoie.domain.docs.parser import doc_title
from digoie.domain.docs.parser import doc_body

class Doc(object):

    # URL = None;
    # TITLE = None; 
    # BODY = None;
    

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
        # self. content needed for further process
        self.initialize()

    def initialize(self):
        """ initialize main conent of doc
        """
        # doc_url.parse(self.url)
        doc_title.parse(self.title)
        # if self.body:
        #     words, tags = doc_body.parse(self.body)

    def parse_title(self, title):
        pass

    def parse_body(self, body):
        pass

