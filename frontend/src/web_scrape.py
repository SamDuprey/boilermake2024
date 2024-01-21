import time
import re
import subprocess
import sys
import string
def install_bs4():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "bs4"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

try:
    from bs4 import BeautifulSoup
except:
    install_bs4()
    from bs4 import BeautifulSoup
import requests
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

# Gets the link from what's scraped and returns a list of reddit story links
def parse(list):
    result = []
    for str in list:
        match = re.search(r'href="([^"]+)"', str)
        if match:
            href_value = match.group(1)
            result.append("https://www.reddit.com" + href_value)
    result.pop(0)
    return result

# Takes in a url and scrapes the website. Uses the parse() function to get a list of urls
def scrape(url):
    browser_options = ChromeOptions()
    browser_options.headless = True

    driver = Chrome(options=browser_options)
    driver.get(url)

    scrape_list = []
    time.sleep(1)
    SCROLL_PAUSE_TIME = 2

    last_height = driver.execute_script("return document.body.scrollHeight")
    count = 0
    while True:
        # INCREASE/DECREASE this depending on how many URLs you want
        if (count == 2):
            break
        count += 1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        result = driver.find_elements(By.CSS_SELECTOR, "a[slot='full-post-link']")
        for element in result:
            scrape_list.append(element.get_attribute("outerHTML"))

        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    return parse(scrape_list)

def scrape_story(urls):
    stories = []
    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html')
        sentences = []
        
        title_element = soup.find('h1', {'slot': 'title'})
        punctuation_chars = set(string.punctuation)
        if title_element:
            title_text = str(title_element.get_text(strip=True))
            if (title_text[-1] not in punctuation_chars):
                title_text += "."
            sentences.append(title_text)

        result = soup.find_all('p')
        result.pop(0)
        for i in range(len(result)):
            result[i] = str(result[i])
            edited = re.search(r'<p>(.*?)</p>', result[i], re.DOTALL)
            if edited:
                sentences.append(edited.group(1))
        big_string = ""
        for sent in sentences:
            big_string += sent.strip() + " "
        stories.append(big_string.strip())
    return stories

# takes in a URL from history.com article and returns the title + article intro string
def scrape_history(url):
    browser_options = ChromeOptions()
    browser_options.headless = True

    driver = Chrome(options=browser_options)
    driver.get(url)

    sentence = ""
    title_element = driver.find_element(By.CLASS_NAME, "page-header__title")
    title_element = title_element.text
    punctuation_chars = set(string.punctuation)
    if title_element:
        title_text = str(title_element)
        if title_text[-1] not in punctuation_chars:
            title_text += "."
        sentence += title_text + " "

    summary = driver.find_element(By.CLASS_NAME, "article-intro")
    summary = summary.get_attribute("outerHTML")
    soup = BeautifulSoup(summary, 'html.parser')
    summary = soup.find('div', class_='article-intro').find('p').get_text(strip=True)

    sentence += summary
    sentence.strip()
    driver.close()
    return sentence

