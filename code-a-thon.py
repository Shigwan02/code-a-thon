from bs4 import BeautifulSoup
import requests
import json
import re
url = 'https://www.amazon.in/l/21570135031/ref=s9_acss_bw_cg_LFENPC_4a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=WHVGHKCBRDDK28V1266W&pf_rd_t=101&pf_rd_p=8de60e3c-e172-4965-a5cc-cec2c9fc7fc3&pf_rd_i=21532970031'
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data)
#print(soup)

for aa in soup.findAll('div',{'class':'s-item-container'}):
    for ss in aa.findAll('div',{'class':'a-row a-spacing-none sx-line-clamp-4'}):
        for dd in ss.findAll('a'):
            print('URL:',dd.get('href'))
            print('TITLE:',dd.get('title'))
            abc=dd.get('href')
            page1 = requests.get(abc)
            data1 = page1.text
            soup1 = BeautifulSoup(data1)
            for aa in soup1.findAll('div', {'id': 'imgTagWrapperId'}):
                for ss in aa.findAll('img'):
                    print('image:', ss.get('src'))
            for gg in soup1.findAll('span', {'id': 'priceblock_ourprice'}):
                try:
                    print('price:', gg.text)
                except:
                    print('price:','missing')
            for hh in soup1.findAll('div', {'id': 'merchant-info'}):
                print('seller:', hh.text.strip())
                a=dd.get('href')
                b=dd.get('title')
                c=ss.get('src')
                d=gg.text
                e=hh.text.strip()
                list=[{a,b,c,d,e}]
                print(list)
