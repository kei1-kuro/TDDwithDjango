from selenium import webdriver

chrome_options =webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(chrome_options=chrome_options) 
browser.get('http://localhost:8000')

assert 'Django' in browser.title