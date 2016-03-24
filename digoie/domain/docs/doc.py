
from digoie.domain.docs.parser import doc_url
from digoie.domain.docs.parser import doc_title

class Doc(object):

    # URL = None;
    # TITLE = None; 
    # BODY = None;
    

    def __init__(self, url=None, title=None, body=None):
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

    def parse_title(self, title):
        pass

    def parse_body(self, body):
        pass

