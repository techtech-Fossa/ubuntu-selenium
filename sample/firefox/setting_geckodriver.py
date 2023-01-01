#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup
import re

## geckodriverの最新版の64ビット用のtar.gzのダウンロードリンクを取得
res = requests.get('https://github.com/mozilla/geckodriver/releases')
soup = BeautifulSoup(res.content,'html.parser')
href = soup.find('a',{'href':re.compile('.*linux64.tar.gz')}).get('href')

## 取得するhrefは/mozillaからになっているのでプロトコルとドメインを追加
base = 'https://github.com'

## ダウンロードリンク
link = base + href

os.system(f'wget {link}')
os.system('tar -zxvf *.tar.gz')
os.system('sudo chmod +x geckodriver')
os.system('sudo mv geckodriver /usr/local/bin')
