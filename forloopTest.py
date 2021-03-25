import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

folderName = '104job/'
if not os.path.exists(folderName):
    os.mkdir(folderName)

url = 'https://www.104.com.tw/jobs/search/?ro=0&asc=0&page={}'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}

page = 1

all_job_datas = []

for trun in range(0, 2):
    res = requests.get(url.format(page), headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    articleList = soup.select('article')
    # print(article)

    for article in articleList:
        try:

            Opening = article.select('a[class="js-job-link"]')[0].text
            joburl = 'https:' + article.select('a[class="js-job-link"]')[0]['href']
            CompanyName = article.select('ul[class="b-list-inline b-clearfix"] a')[0].text.lstrip()
            jobContent = article.select('p[class="job-list-item__info b-clearfix b-content"]')[0].text

            job_data = {

                '職缺': Opening,
                '公司名稱': CompanyName,
                '網址': joburl,
                '工作內容': jobContent

            }

            all_job_datas.append(job_data)

        except AttributeError as a:
            print(a)
        except IndexError as i:
            print(i)
        except FileNotFoundError as o:
            print(o)
        except OSError:
            pass

df = pd.DataFrame(all_job_datas)

