import requests
from bs4 import BeautifulSoup

def get_all_pages():
    page_number=1
    for i in range(100):
        i=f'https://www.automobile.tn/fr/occasion/{page_number}'
        page_number += 1
        print(i)

get_all_pages()