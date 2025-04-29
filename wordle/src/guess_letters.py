'''
A workflow that:
    1. gets all words that have come in Wordle
    2. all 5 letter words
    3. Takes words in the group 2 minus 1 and then analyzes the remaining words, giving the first 3 most commonly used letters.

'''

# imports
from bs4 import BeautifulSoup
import datetime
import pandas as pd
from pathlib import Path
import requests

def clean_all_words(filepath: Path) -> pd.DataFrame:

    with open(filepath, 'r') as file:
        # read all words as a string
        all_words_string = file.read()

    # remove newlines
    all_words = all_words_string.strip('\n').split('\n')

    return all_words


def get_used_words(past_words_url: str,
                   heading_to_find: str,
                   heading_tag: str) -> pd.DataFrame:
    '''
    Description: This code is specifically written for the https://www.rockpapershotgun.com/wordle-past-answers website that has
                 all past words that have already come in Wordle.
    Args:
        past_words_url = str, url of the website https://www.rockpapershotgun.com/wordle-past-answers
        heading_to_find = str, the subheading that is situated right before the list of words.
                          This will serve as a starting point to locate the actual list of words
        heading_tag = str, the html tag level eg. 'h2' associated with the heading_to_find
        heading_to_find and heading_tag can be confirmed/found by opening the website in the browser and 'View page source'
    Returns:
        a df with all the words in a column and a date column to indicate how updated the df is
    '''

    # send an HTTP request to the webpage, # timeout after 10 seconds
    try:
        response = requests.get(past_words_url, timeout=10)
        response.raise_for_status()

    except requests.exceptions.RequestException as error:
        print(f'Failed request: {error}')

    # Parse the content using BeautifulSoup object
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')

    # find all h2 and collect the h2 tags in a list
    # this will not be a list of strings but a list of tag objects
    all_headings = soup.find_all(heading_tag)

    # tag objects have a string attribute which holds the text at that level
    heading_of_interest = None
    for heading in all_headings:
        if heading_to_find in heading.text.lower():
            heading_of_interest = heading

    # once the right heading tag is extracted, use it to find the ul (unordered list) tag at the same level as the h2 tag
    ul_tag = heading_of_interest.find_next_sibling('ul')

    # within the ul tag, get all list items <li>
    all_list_tags = ul_tag.find_all('li')

    # collect all words that already came before in Wordle, convert to lowercase
    all_words = [tag.text.lower() for tag in all_list_tags if tag.text is not None]

    df = pd.DataFrame({'word': all_words})

    # add a date column indicating when the workflow was run and when words were collected

    df['updated'] = pd.Timestamp.now().date().strftime('%Y-%m-%d')

    return df

