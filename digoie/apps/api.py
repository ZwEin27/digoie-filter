""" 
Steps

1. parse json file for docs user selected, and get doc's url, title, and body content

2. get top words for the docs user selected in original form with POS tags

3. select few top words to elastic search server and conduct sigificant terms aggregation to get more uncommonly common docs

4. based on these docs data from elastic search, apply one class classification 

5. use the trained classifier to filter result of DIG
"""





import numpy as np
import os

from digoie.domain.docs.base import *

def main():
    doc_parser()


