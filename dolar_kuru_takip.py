import requests

cookies = {
    '_ga': 'GA1.1.200664832.1711456901',
    'yrm': 'true',
    'ASPSESSIONIDCGSRBTCB': 'OLGBNKMAMOIHIMMGOPGFAKGN',
    'ASPSESSIONIDQUTRCTAA': 'ANHAMOABJDFBJEDAGEDKMAKK',
    '_ga_GRD9HD6XEV': 'GS1.1.1711456900.1.1.1711456932.28.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'tr-TR,tr;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '_ga=GA1.1.200664832.1711456901; yrm=true; ASPSESSIONIDCGSRBTCB=OLGBNKMAMOIHIMMGOPGFAKGN; ASPSESSIONIDQUTRCTAA=ANHAMOABJDFBJEDAGEDKMAKK; _ga_GRD9HD6XEV=GS1.1.1711456900.1.1.1711456932.28.0.0',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

from bs4 import BeautifulSoup
from datetime import datetime
import time as t
dolar = ""
while True:
    response = requests.get('https://yorum.altin.in/tum/dolar', cookies=cookies, headers=headers)
    if(response.status_code == 200):
        source = BeautifulSoup(response.content, "html.parser")
        dolar_kuru = source.find("div", attrs={"id":"dolar"}).find("h2").text
        if(dolar != dolar_kuru):
            dolar = dolar_kuru
            print(datetime.now().strftime("%d.%m.%Y %H:%M:%S") + " " + str(dolar_kuru) + " " + str(float(dolar_kuru)))
    else:
        print(datetime.now().strftime("%d.%m.%Y %H:%M:%S") + " " + "Sayfa engellemesi")
    t.sleep(0.000001)











# print(response.text)