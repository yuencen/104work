import requests
from bs4 import BeautifulSoup

url = 'https://www.104.com.tw/jobs/search/?ro=0&asc=0&page={}'

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}

page = 2

res = requests.get(url.format(page),headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
articleList = soup.select('article')
# print(article)

for article in articleList:
    try:
        Opening = article.select('a[class="js-job-link"]')[0].text
        CompanyName = article.select('ul[class="b-list-inline b-clearfix"] a')[0].text.lstrip()
        jobContent = article.select('p[class="job-list-item__info b-clearfix b-content"]')[0].text

        print(Opening)
        print(CompanyName)
        print(jobContent)
        print('='*50)
    except AttributeError as a:
        print(a)
    except IndexError as i:
        print(i)

page += 1