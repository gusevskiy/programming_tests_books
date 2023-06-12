from selenium import webdriver


browser = webdriver.Chrome(
    executable_path="chromedriver/chromedriver_linux64/chromedriver"
)
browser.get('http://localhost:8000')
assert 'To-Do' in browser.title
