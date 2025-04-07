"""
A set of tools and objects for use throughout the cui_finder package.
"""

# utils for recommendation_4
# site packages
import re
import json
import pandas as pd
import pkg_resources

def load_data():
    "Returns a dataframe containing keywords and descriptions from the CUI reference table."

    stream = pkg_resources.resource_stream(__name__, 'cui_ref.json')
    return pd.read_json(stream, orient = 'records')


def clean_list(row):
    """Function for removing whitespace from string values and converting to
    lowercase.

    Parameters
    ----------
    row : list
        Contains string values for cleaning

    Returns
    -------
    list
    """
    row2 = []
    for i in row:
        i = re.sub(r'^\s+', '', i)
        i = re.sub(r'\s+$', '', i)
        row2.append(i)
    row3 = [word.lower() for word in row2 if word != '']
    return row3

# cui_df = pd.read_json('cui_ref.json', orient = 'records')
# cui_df = pd.read_csv('cui_df.csv').fillna('')

def stage_cui(df):
    """Imports, cleans, and stages the CUI keywords from the CUI refernece table.

    Parameters
    ----------
    df : pandas DataFrame
        A DataFrame consisting of CUI categories, subcategories, descriptions
        and keywords.


    Returns
    -------
    pandas DataFrame

    """
    df['Key Words'] = df['Key Words'].str.split(',')
    df['Key Words'] = df['Key Words'].apply(lambda x: clean_list(x))
    df['other words'] = df['other words'].str.split(',')
    df['other words'] = df['other words'].apply(lambda x: clean_list(x))
    df['TSCA LIST'] = df['TSCA LIST'].str.split(',')
    df['TSCA LIST'] = df['TSCA LIST'].apply(lambda x: clean_list(x))
    df['final_words'] = df['Key Words']+df['other words']+df['TSCA LIST']

    df = df[
        [
            'Organizational Index Grouping',
            'CUI Category',
            'Category Description',
            'final_words'
            ]
        ]

    df = df.rename(
        columns = {
            'Organizational Index Grouping':'org_index',
            'CUI Category':'cui_cat',
            'Category Description':'cat_descript'
            }
        )

    return df

cui_df = load_data()
cui_df = stage_cui(cui_df)
cui_dict = cui_df.to_dict('records')
