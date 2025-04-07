"""The primary tool used in the cui_finder package.

Defines the color coding parameters for words that are flagged for PII or CUI.
Provides the syntax to be returned if a corpus or text sample is flagged for
PII or CUI, including more details on the CUI subcategories, if preferred.
"""

# site packages
from spacy import displacy

# local packages
from cui_finder import utils, pipeline, patterns

# import the CUI reference dictionary
bank = utils.cui_dict

# set the custom parameters for the HTML display
colors = {
    "PERSON": "#F6EA83",
    "PHONE": "#F6EA83",
    "EMAIL": "#F6EA83",
    "CUI": "#F8A997"
    }

options = {
    'ents': ['PERSON', 'PHONE', 'EMAIL', 'CUI'],
    'colors':colors
    }

pii_warn1 = "CAUTION: This entry may contain Personally Identifiable Information (PII).\nPlease review the following items to ensure they do not contain PII:\n"
cui_warn1 = "CAUTION: This entry may contain Controlled Unclassified Information (CUI).\nPlease review the following items to ensure you are not disclosing CUI:\n"
cui_warn2 = "For more information on CUI, please visit https://www.archives.gov/cui\n"

pii_crit = ['PHONE', 'PERSON', 'EMAIL']
cui_crit = ['CUI']

def scan_entry(text, display = False, description = False):
    """

    Parameters
    ----------
    text : string
        Raw text to be scanned for PII and CUI.

    display : bool, optional
        If true, displays an HTML-based output of the raw text, with flagged
        words higlighted based on their PII or CUI association.
        (Default value = False)

    description : bool, optional
        If true, displays additional information on the CUI category detected
        in the raw text. (Default value = False)

    Returns
    -------

    """
    # process the award description through the pre-defined NLP pipeline
    doc = pipeline.nlp(text)

    # collect the raw text and entity label for each PII flag
    pii_hits = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in pii_crit]

    # collect the raw text and entity label for each CUI flag
    cui_hits = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in cui_crit]

    # reduce flags down to sets of unique values and set on index
    pii_set = list(set(pii_hits))
    cui_set = list(set(cui_hits))

    # what happens if there are either PII or CUI flags?
    if len(pii_set) or len(cui_set) > 0:
        if display == True:
            displacy.render(doc, style = 'ent', options = options)

    # do hits contain PII?
    if len(pii_set) > 0:
        print(pii_warn1)
        for item in pii_set:
            print("\t", item[0])
        print('\n')

    # do hits contain CUI?
    if len(cui_set) > 0:
        print(cui_warn1)
        for item in cui_set:
            for entry in bank:
                if item[0].lower() in entry['final_words']:
                    print('ITEM: {}'.format(item[0]))
                    print('CUI REFERENCE: {} - {}'.format(entry['org_index'], entry['cui_cat']))

                    # do you want to see more information related to the CUI reference?
                    if description == True:
                        print('CATEGORY DESCRIPTION: {}\n'.format(entry['cat_descript']))
                    else:
                        print('')
