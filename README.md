# `cui_finder`

`cui_finder` is open-source package for finding Controlled Unclassified Information (CUI) and Personally Identifiable Information (PII) in raw text. It is based on the [spaCy 3.0](https://spacy.io/usage/v3) ecosystem and creates custom patterns for [rule-based matching](https://spacy.io/usage/rule-based-matching) and [named entity recognition](https://spacy.io/usage/linguistic-features#named-entities).

## Contents

* `requirements.txt` for creating local or virtual environments with the required dependencies for `cui_finder` to function properly.
* `setup.py` for installing the package to your environment based on the dependencies in `requirements.txt`.
* `cui_finder/cui_finder` contains the library of scripts for creating the capability to scan for PII and CUI.

  * `patterns.py`: Contains the custom labels used for identifying PII and CUI in text. Includes the patterns used to identify PII and CUI based on [spaCy's rule-based matching process](https://spacy.io/usage/rule-based-matching).
  * `pipeline.py`: Contains the sequence for loading spaCy's pre-trained model and adding match patterns to it before applying the model to corpuses. Adds an entity_ruler module to the [spaCy pipeline](https://spacy.io/usage/processing-pipelines) before the Named Entity Recognizer.
  * `scanner.py`: The primary tool used in the `cui_finder` package. Defines the color coding parameters for words that are flagged for PII or CUI. Provides the syntax to be returned if a corpus or text sample is flagged for
  PII or CUI, including more details on the CUI subcategories, if preferred. (see module documentation for more)
  * `utils.py`:A set of tools and objects for use throughout the `cui_finder` package.


* `ref_data`: Contains the CSV file of CUI key words and their associated categories, subcategories, and descriptions based on policies published by the [National Archives and Records Administration](https://www.archives.gov/cui).
