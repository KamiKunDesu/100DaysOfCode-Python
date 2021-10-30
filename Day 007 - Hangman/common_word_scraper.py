'''
This is just a quick webscraper I made to get a list of common words from a website I found online and store
them in a csv
'''
import requests
from bs4 import BeautifulSoup
import re
import csv

#request the page and make a soup object
webpage = requests.get('https://www.talkenglish.com/vocabulary/top-1500-nouns.aspx').content
soup = BeautifulSoup(webpage, "html.parser")

#leaving this line of code here commented out as an example for use later
#word_list = [link.text for link in soup.find_all(href=re.compile(r"/how-to-use/[a-zA-Z]+"))]

'''
This might seem a confusing but essentially first we use beautiful soup to access all of the td's that have words in them,
we enumerate so that we can skip the first td that matches because that's the column heading and we don't want it.
Then the text all has new lines and tabs etc so stripping out for those, stripped twice since one round wasn't enough.
Then it's all stored inside a list comprehension - which is then stored in a list (because that's how the csv writerows function likes it,
a list of lists.)
'''
word_list = [td.text.strip('\n').strip('\r').strip('\t').strip('\n').strip('\r').strip('\t') for count, td in enumerate(soup.find_all('td', {'width': '120'})) if count != 0]


#This just writes the words from word_list into a single column in a csv
with open('word_list.csv', 'w') as f:
    writer = csv.writer(f)
    for val in zip(word_list):
        writer.writerow(val)