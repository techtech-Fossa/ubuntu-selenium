#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

## geckodriverのパス指定
executable_path="/usr/local/bin/geckodriver"

## optionの設定
options = Options()

### ユーザーエージェントの設定
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'
options.add_argument('--user-agent=' + user_agent)

### ブラウザの言語設定を日本語にする
options.set_preference("intl.accept_languages", "jpn")

### その他optionsの指定
options.add_argument('--no-sandbox')  ## Sandboxの外でプロセスを動作させる
options.add_argument('--headless')  ## ブラウザを表示しない　CLIで起動する際は必須
options.add_argument('--disable-dev-shm-usage')  ## /dev/shmパーティションの使用を禁止し、パーティションが小さすぎることによる、クラッシュを回避する。

## driverの作成
service = FirefoxService(executable_path=executable_path)
driver = webdriver.Firefox(options=options,service=service)

url = 'https://www.yahoo.co.jp/'  ## Yahoo
driver.get(url)

print(driver.current_url)
print(driver.find_element(By.TAG_NAME,'h1').text)

driver.quit()
