# this code can be executed when the coreyms.com website is working

from bs4 import BeautifulSoup
import requests, csv, os

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

articles = soup.find_all('article')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, 'web_text.csv')
csv_file = open(file_path,'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in articles:

    headline = article.h2.a.text
    summary = article.find('div', class_= 'entry-content').p.text

    try:
        vid_source = article.find('iframe', class_= 'youtube-player')['src']
        vid_id = vid_source.split('/')[4].split('?')[0] # so this splitting is baseed on the requirement

        vid_link = f'https://youtube.com/watch?{vid_id}'

    except Exception as e:
        vid_link = None

    print(vid_link)
    print()

    csv_writer.writerow([headline, summary, vid_link])

csv_file.close()