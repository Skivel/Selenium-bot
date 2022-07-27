import os

import pyautogui as gui

from post import text
import random
from auth import login, password

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

options = Options()

options.headless = False

driver = webdriver.Firefox(options=options)
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
action = ActionChains(driver)

i = 1
while True:
    sleep = random.randint(2, 4)
    time.sleep(sleep)
    print("Select group")
    element = driver.find_element(By.CSS_SELECTOR, """.rpm2j7zs > div:nth-child(1) > div:nth-child(""" + str(
        i + 4) + """) > a:nth-child(1) > div:nth-child(1)""")
    element.location_once_scrolled_into_view
    time.sleep(1)
    action.move_to_element(element)
    action.pause(1)
    action.click()
    action.perform()
    print("Done!")

    print("Start add post")
    sleep = random.randint(2, 7)
    time.sleep(sleep)
    input_post = driver.find_element(By.CSS_SELECTOR,
                                     """div.h676nmdw:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)""")
    action.move_to_element(input_post).click().perform()
    print("Done!")

    sleep = random.randint(2, 7)
    time.sleep(sleep)

    print("Image input")
    img = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[1]")
    img.click()
    time.sleep(sleep)
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/div")
    print(os.getcwd()+"/BKM.png")
    element.click()
    gui.write(os.getcwd()+"/BKM.jpg")
    gui.press('enter')
    time.sleep(sleep)
    print("Done!")

    print("Text input")
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div")
    element.click()
    time.sleep(1)
    action.send_keys(text)
    action.perform()
    print("Done!")
    sleep = random.randint(2, 3)
    time.sleep(sleep)

    print("Post in group ", i, ".")
    input_post = driver.find_element(By.CSS_SELECTOR,
                                     """div.ihqw7lf3:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)""")
    action.move_to_element(input_post).click()
    action.perform()
    print("Done!")
    sleep = 560
    time.sleep(sleep)
    i += 1
    # if i % 2 != 0:
    #     print("Waiting", sleep, "s")
    #     time.sleep(sleep)
    #     i = i + 1
    #     continue
    # if i % 2 == 0:
    #     sleep = random.randint(300, 600)
    #     print("Waiting", sleep, "s")
    #     time.sleep(sleep)
    #     i = i + 1
    #     continue
