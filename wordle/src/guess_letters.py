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

