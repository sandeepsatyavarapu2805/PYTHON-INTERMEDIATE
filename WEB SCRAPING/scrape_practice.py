import os
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, 'website.html')

with open(file_path,'r') as f:
    soup = BeautifulSoup(f,'lxml')

'''
print(soup)
print(soup.prettify()) # This formats the text in it into html indentation

match = soup.head # this gets the tag in the soup like TITLE, BODY etc

match = soup.div # this gets the first div in the soup

match = soup.head.text # this gets the text in the tags included

article = soup.find('div', class_ = 'article') # this is used to specifically get the first matching tag we can also use id and name without '_'
headline = article.h2.a.text
summary = article.p.text

'''

articles = soup.find_all('div', class_ = 'article') # this is used to specifically get all the tags in a list

for article in articles:
    headline = article.h2.text
    summary = article.p.text

    print(headline,summary,sep='\n')
    print()