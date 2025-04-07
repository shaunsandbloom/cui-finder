"""
Contains the sequence for loading spaCy's pre-trained model and adding match
match patterns to it before applying the model to corpuses.

Adds an entity_ruler module to the pipeline before the Named Entity Recognizer.
For more information on the spaCy NLP pipeline visit:
https://spacy.io/usage/processing-pipelines
"""
# site packages
import pickle
import spacy
import pandas as pd
from spacy.tokens import Span
from spacy.matcher import Matcher

# local packages
from cui_finder import patterns

# loading the large pre-trained spaCy English model
nlp = spacy.load('en_core_web_lg')

# `entity_ruler` is not a default component of the pipeline
# adding `entity_ruler` so the pipeline can look for custom matches
ruler = nlp.add_pipe('entity_ruler', before = 'ner')

# adding custom matches to `entity_ruler`
# note: patterns being added to `entity_ruler` are defined in patterns.py
ruler.add_patterns(patterns.pii_patterns)
ruler.add_patterns(patterns.cui_patterns)
