#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge import service
from selenium.webdriver.common.by import By

#driverの準備
executable_path=r"/usr/local/bin/msedgedriver"
edge_service = service.Service(executable_path=executable_path)
options = Options()

## ユーザーエージェントの指定
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36' 
options.add_argument('--user-agent=' + UA)  ## ユーザーエージェントの設定

### その他optionsの指定
options.add_argument('--no-sandbox')  ## Sandboxの外でプロセスを動作させる
options.add_argument('--headless')  ## ブラウザを表示しない　CLIで起動する際は必須
options.add_argument('--disable-dev-shm-usage')  ## /dev/shmパーティションの使用を禁止し、パーティションが小さすぎることによる、クラッシュを回避する。

driver = webdriver.Edge(service=edge_service, options=options)

url = 'https://www.yahoo.co.jp/'  ## Yahoo
driver.get(url)

print(driver.current_url)
print(driver.find_element(By.TAG_NAME,'h1').text)

driver.quit()