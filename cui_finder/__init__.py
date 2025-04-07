"""
cui_finder
==========
A spaCy-based Natural Language Processing package for identifying specific
topics in raw text.

This version focuses specifically on Personally Idenifiable Information (PII)
in the form of Names, Emails, and Phone Numbers.

This version also focuses on Controlled Unclassified Information (CUI) topics
based on guidance from https://www.archives.gov/cui.

CUI and PII detection in this package follows a structure of looking specifcally
for key words. Future iterations will include more linguistic features for
predicting when CUI may be mentioned in text that does not explicitly refer
to key words on the CUI category list.
"""

# from .scanner import scan_entry
# from .utils import cui_df, cui_dict
# from .pipeline import nlp
# from .batch_tester import run_test

from cui_finder.utils import load_data
from cui_finder.scanner import scan_entry
