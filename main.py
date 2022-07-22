from post import text, enter, tab
import random
from auth import login, password

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

options = Options()

options.headless = True

driver = webdriver.Firefox()
driver.get("https://www.facebook.com")
assert "Facebook - log in or sign up" in driver.title
print("Start Facebook.com")
time.sleep(1)
element = driver.find_element(By.XPATH, """//button[@title="Allow essential and optional cookies"]""")
element.click()
print("Done!")

print("Log In...")
input_email = driver.find_element(By.XPATH, """//*[@id="email"]""")
input_email.send_keys(login)

input_pass = driver.find_element(By.XPATH, """//*[@id="pass"]""")
input_pass.send_keys(password)

element = driver.find_element(By.XPATH, """//button[@name="login"]""")
element.click()
print("Done!")
time.sleep(1)
element = driver.find_element(By.CSS_SELECTOR,
                              """.sn7ne77z > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)""")
element.click()
sleep = random.randint(2, 5)
time.sleep(sleep)

i = 1
while True:
    sleep = random.randint(2, 4)
    time.sleep(sleep)
    print("Select group")
    element = driver.find_element(By.CSS_SELECTOR, """.rpm2j7zs > div:nth-child(1) > div:nth-child(""" + str(
        i + 4) + """) > a:nth-child(1) > div:nth-child(1)""")
    element.click()
    print("Done!")
    # ------------------------if block------------------------
    # ex_el = driver.find_element(By.CSS_SELECTOR)
    # try:
    #     element = driver.find_element(By.CSS_SELECTOR,"""div.gjzvkazv:nth-child(1) > div:nth-child(1) > div:nth-child(1)""")
    #     element.click()
    # except:
    #     print("Spam Block Not Found")
    # ------------------------if block------------------------
    print("Start add post")
    sleep = random.randint(2, 7)
    time.sleep(sleep)
    input_post = driver.find_element(By.CSS_SELECTOR,
                                     """div.h676nmdw:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)""")
    input_post.click()
    print("Done!")
    sleep = random.randint(2, 7)
    time.sleep(sleep)

    print("Text input")
    action = ActionChains(driver)
    action.send_keys(text)
    action.perform()
    print("Done!")
    sleep = random.randint(2, 3)
    time.sleep(sleep)
    print("Image input")
    img = driver.find_element(By.CSS_SELECTOR,
                              """div.dwxx2s2f:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > i:nth-child(1)""")
    img.send_keys(
        '/home/skivel/PycharmProjects/Selenium-bot/BKM.png')
    img.click()
    time.sleep(sleep)
    driver.find_element(By.CSS_SELECTOR,
                        '.ic9r50nj > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > i:nth-child(1)').send_keys(
        '/home/skivel/PycharmProjects/Selenium-bot/BKM.png')
    sleep = random.randint(2, 3)
    time.sleep(sleep)
    print("Done!")

    print("Post in group ", i, ".")
    input_post = driver.find_element(By.CSS_SELECTOR,
                                     """div.ihqw7lf3:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)""")
    input_post.click()
    print("Done!")
    sleep = random.randint(300, 600)
    if i % 2 != 0:
        print("Waiting", sleep, "s")
        time.sleep(sleep)
        i = i + 1
        continue
    if i % 2 == 0:
        sleep = random.randint(300, 600)
        print("Waiting", sleep, "s")
        time.sleep(sleep)
        i = i + 1
        continue
