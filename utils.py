from bs4 import BeautifulSoup
import requests

def obtain_html(url):
    return requests.get(url).text

def get_content(url):
    res = ""
    soup = BeautifulSoup(obtain_html(url), 'html.parser')
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        res += p.get_text() + "\n "
    return res

def format_newsapi_sources_str(sources_list):
    res = sources_list.join(",")
    