"""
Contains the custom labels used for identifying PII and CUI in text. Includes
the patterns used to identify PII and CUI based on spaCy's rule-based matching
process.

For more information on rule-based matching, visit:
https://spacy.io/usage/rule-based-matching

labels
------
    'PHONE': matches 10-digit U.S.-based phone numbers.
    'EMAIL': matches email addressses following standard email syntax structure.
    'PERSON': this is spaCy's entity label based on their pre-trained models.
    'CUI': matches any of the key words found in the CUI reference table.
    (see utils.py for more information on the CUI reference table)
"""

# site packages
import re

# local packages
from cui_finder import utils

# pattern: email through regex
email_pattern = [{'TEXT': {'REGEX': '[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+'}}]

# pattern: ddd-ddd-dddd
phone_pattern1 = [
    {"SHAPE":"ddd"},
    {"ORTH":"-"},
    {"SHAPE":"ddd"},
    {"ORTH":"-"},
    {"SHAPE":"dddd"}
    ]

# pattern: (ddd) ddd-dddd
phone_pattern2 = [
    {"ORTH":"("},
    {"SHAPE":"ddd"},
    {"ORTH":")"},
    {"SHAPE":"ddd"},
    {"ORTH":"-"},
    {"SHAPE":"dddd"}
    ]

# pattern: ddd.ddd.dddd
phone_pattern3 = [
    {"SHAPE": "ddd.ddd.dddd"}
    ]

# pattern: (ddd)ddd-dddd
phone_pattern4 = [
    {"ORTH":"("},
    {"SHAPE":"ddd)ddd"},
    {"ORTH":"-"},
    {"SHAPE":"dddd"}
    ]

# collect all PII patterns
pii_patterns = [
    {
        "label": "EMAIL",
        "pattern":email_pattern
        },
    {
        "label": "PHONE",
        "pattern":phone_pattern1
        },
    {
        "label": "PHONE",
        "pattern":phone_pattern2
        },
    {
        "label": "PHONE",
        "pattern":phone_pattern3
        },
    {
        "label": "PHONE",
        "pattern":phone_pattern4
        }
    ]

# collect all CUI patterns
cui_list = [y for x in utils.cui_dict for y in x['final_words']]
cui_patterns = []
for item in cui_list:
    item2 = []
    for word in item.split(' '):
        item2.append({'LOWER': word})
    cui_patterns.append({'label':'CUI', 'pattern':item2})
