import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://smartstore.naver.com/mydea/products/4758287994?n_media=27758&n_query=%EB%A7%A5%EB%B6%81%EC%BC%80%EC%9D%B4%EC%8A%A4&n_rank=2&n_ad_group=grp-a001-02-000000015889693&n_ad=nad-a001-02-000000097237244&n_campaign_type=2&n_mall_pid=4758287994&n_ad_group_type=2&NaPm=ct%3Dkobbxgpk%7Cci%3D0yy0000lrD9uvFxKOL3j%7Ctr%3Dpla%7Chk%3D135ab8952aa7fca1479bbf532ec53d978fc6a513')
soup = BeautifulSoup(response, 'html.parser')

for anchor in soup.select("span._3eMaa46Quy"):
    print(anchor)



#     data = str(i) + "위 : " + anchor.get_text() + "\n"
#     i = i + 1
#     f.write(data)
# f.close()

# f.read()
