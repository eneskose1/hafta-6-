from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

def fetch_sports_news(days=5):
    base_url = 'https://www.sabah.com.tr/spor/futbol/'
    today = datetime.today()
    
    for i in range(days):
        date = (today - timedelta(days=i)).strftime('%Y/%m/%d')
        url = f'{base_url}{date}'
        
        try:
            r = requests.get(url)
            r.raise_for_status()
            soup = BeautifulSoup(r.content, 'html.parser')
            
            news_list = soup.find_all("div", {"class": "category-content"})
            
            print(f'********** Haberler - {date} ({url}) **********')
            
            for news in news_list:
                for link in news.find_all('a'):
                    my_link = link.get('href')
                    if my_link.startswith("/"):
                        new_link = f'https://www.sabah.com.tr{my_link}'
                    else:
                        new_link = my_link
                    print(new_link)
        
        except requests.exceptions.RequestException as e:
            print(f'Hata oluştu ({date} - {url}): {e}')
            continue


fetch_sports_news(5)
