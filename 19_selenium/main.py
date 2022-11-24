from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# chromedriver.exeをダウンロードして、パスが通っている場所に配置する
# https://chromedriver.chromium.org/downloads
service = Service(executable_path='./chromedriver')

# chromeが閉じないようにするためのオプション
options = Options()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(service=service, options=options)

# http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/
browser.get('https://www.seleniumeasy.com/')

search_input = browser.find_element(By.CSS_SELECTOR, "#edit-search-block-form--2")
search_button = browser.find_element(By.CSS_SELECTOR, "#search-block-form button")

assert "Search" in search_input.get_attribute("placeholder")

search_input.send_keys("Python")
search_button.click()

browser.implicitly_wait(3)

# なぜかこれは動かない
section_title = browser.find_element(By.CSS_SELECTOR, ".section_title")

print(section_title.get_attribute("innerText"))