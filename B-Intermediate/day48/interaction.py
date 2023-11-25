from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:/Users/deneb/code/chromedriver.exe'

driver = webdriver.Chrome()

driver.get('https://es.wikipedia.org/wiki/Wikipedia:Portada')

count = driver.find_element(By.CSS_SELECTOR, '.main-top-articleCount a')

print(count.text)