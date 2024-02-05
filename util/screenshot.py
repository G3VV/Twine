from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import logging

post_dir = './data/post/'
comment_dir = './data/comment/'

def takePostScreenshot():
    with open(post_dir + 'post.json', 'r') as f:
        data = json.load(f)
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(data['url'])
    
    element = driver.find_element(By.TAG_NAME, "shreddit-post")
    element.screenshot(f"./data/screenshot/post.png")
    
    driver.quit()
    logging.info("Captured Post Successfully")

# code below is beautiful (not)
def takeCommentScreenshot():
    with open(post_dir + 'post.json', 'r') as f:
        post_data = json.load(f)
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(post_data['url'])
    
    comments = os.listdir(comment_dir)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        view_more_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "View more comments")]'))
        )
        view_more_button.click()
    except:
        pass

    for comment in comments:
        with open(comment_dir + comment, 'r') as f:
            data = json.load(f)
        
        try:
            element = driver.find_element(By.XPATH, f'//*[@thingid="t1_{data["id"]}"]')
        except:
            continue
        
        element.screenshot(f"./data/screenshot/{data['id']}.png")
        logging.info(f"Captured Comment {data['id']} Successfully")

    driver.quit()
