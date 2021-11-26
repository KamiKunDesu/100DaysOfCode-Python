from bs4 import BeautifulSoup
import requests

def return_search(word):
    html = f"https://jisho.org/word/{word}"
    webpage = requests.get(html).content
    soup = BeautifulSoup(webpage, "html.parser")
    meanings_list = []
    meanings = soup.find_all(attrs = {"class": "meaning-meaning"})

    for count, item in enumerate(meanings):
        meanings_list.append(f"{count+1}) {item.get_text()}")

    meanings_list = '\n\n'.join(meanings_list)

    return meanings_list
