from post_text import text
from auth import login, password

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://www.facebook.com")
assert "Facebook - log in or sign up" in driver.title
time.sleep(1)
element = driver.find_element(By.XPATH, """//button[@title="Allow essential and optional cookies"]""")
element.click()

input_email = driver.find_element(By.XPATH, """//*[@id="email"]""")
input_email.send_keys(login)

input_pass = driver.find_element(By.XPATH, """//*[@id="pass"]""")
input_pass.send_keys(password)

element = driver.find_element(By.XPATH, """//button[@name="login"]""")
element.click()

element = driver.find_element(By.XPATH,
                              """/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[2]/div/a/div[1]/div[2]/div/div/div/div/span/span""")
element.click()

time.sleep(2)

i = 5
while True:
    element = driver.find_element(By.CSS_SELECTOR, """.rpm2j7zs > div:nth-child(1) > div:nth-child(""" + str(
        i) + """) > a:nth-child(1) > div:nth-child(1)""")
    element.click()

    # ------------------------if block------------------------
    # ex_el = driver.find_element(By.CSS_SELECTOR)
    # try:
    #     element = driver.find_element(By.CSS_SELECTOR,"""div.gjzvkazv:nth-child(1) > div:nth-child(1) > div:nth-child(1)""")
    #     element.click()
    # except:
    #     print("Spam Block Not Found")
    # ------------------------if block------------------------
    # start add post
    time.sleep(1)
    input_post = driver.find_element(By.CSS_SELECTOR,
                                     """div.h676nmdw:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)""")
    input_post.click()
    # try:
    #     element = driver.find_element(By.CSS_SELECTOR, """div.t63ysoy8:nth-child(3) > div:nth-child(1) > div:nth-child(1)""")
    #     element.click()
    # except:
    #     print("Requirements not Found")
    # show theme
    time.sleep(3)
    input_post = driver.find_element(By.CSS_SELECTOR, """span.hop8lmos > img:nth-child(1)""")
    input_post.click()
    time.sleep(1)
    # show all_theme
    input_post = driver.find_element(By.CSS_SELECTOR, """div.mtkw9kbi:nth-child(3) > div:nth-child(1) > i:nth-child(1)""")
    input_post.click()
    # theme apply
    input_post = driver.find_element(By.CSS_SELECTOR, """div.qnrpqo6b:nth-child(55) > div:nth-child(1)""")
    input_post.click()
    time.sleep(0.5)
    action = ActionChains(driver)
    action.send_keys(text)
    action.perform()
    time.sleep(1)
    input_post = driver.find_element(By.CSS_SELECTOR, """div.ihqw7lf3:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)""")
    input_post.click()
    time.sleep(15)
    print("Post in group ", i - 4, ". Done!")
    i = i + 1
