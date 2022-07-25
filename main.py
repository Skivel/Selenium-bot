import random
from auth import login, password

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from post import text, enter, tab

options = Options()

options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)
options.headless = False

driver = webdriver.chrome.webdriver.WebDriver(options=options, executable_path='C:\webdrivers\chromedriver.exe')
driver.get("https://www.facebook.com")
driver.maximize_window()

print("Start Facebook.com")
time.sleep(1)
element = driver.find_element(By.XPATH, """//*[@title="Дозволити основні та необов'язкові файли cookie"]""")
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

    print("Start add post")
    sleep = random.randint(2, 7)
    time.sleep(sleep)
    input_post = driver.find_element(By.CSS_SELECTOR,
                                     """div.h676nmdw:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)""")
    input_post.click()
    sleep = random.randint(2, 7)
    time.sleep(sleep)
    print("Done!")

    # print("Image input")
    action = ActionChains(driver)
    # action.send_keys("""![](BKM.png)""")
    # action.perform()
    #
    # sleep = random.randint(2, 3)
    # time.sleep(sleep)
    # print("Done!")

    print("Text input")
    action.send_keys(text)
    action.perform()
    sleep = random.randint(2, 7)
    time.sleep(sleep)
    print("Done!")

    time.sleep(sleep)
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
