# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:33:29 2022

@author: bella
"""

import requests
from bs4 import BeautifulSoup
import time


cookies = {
    'eZSESSID': '7qegsknfetlovdelft8npiahg2',
    'atuserid': 'eyJuYW1lIjoiYXR1c2VyaWQiLCJ2YWwiOiI4MTVkMWEwNS1lYzIxLTQ2N2MtYTBkMS1mMjM3NmU2YWUwYTAiLCJvcHRpb25zIjp7ImVuZCI6IjIwMjMtMDctMDNUMTE6MjE6MzMuNTQxWiIsInBhdGgiOiIvIn19',
    'atauthority': 'eyJuYW1lIjoiYXRhdXRob3JpdHkiLCJ2YWwiOnsiYXV0aG9yaXR5X25hbWUiOiJjbmlsIiwidmlzaXRvcl9tb2RlIjoiZXhlbXB0In0sIm9wdGlvbnMiOnsiZW5kIjoiMjAyMy0wNy0wM1QxMTozMTowOS42MzRaIiwicGF0aCI6Ii8ifX0=',
}

headers = {
    'Host': 'www.herault.gouv.fr',
    # 'Content-Length': '60',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://www.herault.gouv.fr',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.herault.gouv.fr/booking/create/34210/0',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'close',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'eZSESSID=7qegsknfetlovdelft8npiahg2; atuserid=eyJuYW1lIjoiYXR1c2VyaWQiLCJ2YWwiOiI4MTVkMWEwNS1lYzIxLTQ2N2MtYTBkMS1mMjM3NmU2YWUwYTAiLCJvcHRpb25zIjp7ImVuZCI6IjIwMjMtMDctMDNUMTE6MjE6MzMuNTQxWiIsInBhdGgiOiIvIn19; atauthority=eyJuYW1lIjoiYXRhdXRob3JpdHkiLCJ2YWwiOnsiYXV0aG9yaXR5X25hbWUiOiJjbmlsIiwidmlzaXRvcl9tb2RlIjoiZXhlbXB0In0sIm9wdGlvbnMiOnsiZW5kIjoiMjAyMy0wNy0wM1QxMTozMTowOS42MzRaIiwicGF0aCI6Ii8ifX0=',
}

data = 'condition=on&nextButton=Effectuer+une+demande+de+rendez-vous'

while True:
    response = requests.post('https://www.herault.gouv.fr/booking/create/34210/0', cookies=cookies, headers=headers, data=data, verify=True)
    soup = BeautifulSoup(response.text, 'html.parser')
    c = soup.find_all('form', attrs={"class": "jqTransform FormValidate"})
    print("not disponible")
    print(response.text)
    time.sleep(30)
    # try:
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     c = soup.find_all('form', attrs={"class": "jqTransform FormValidate"})
    #     print("not disponible")
    # except:
    #     print("rendez vous est disponible maintenant")
    #     break
    
