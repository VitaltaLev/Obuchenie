import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


s = Service('C:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Open site
driver.get("https://qa.neapro.site/login")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("vitalya.lev@mail.ru")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("129535851")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(3)

element = driver.find_element(By.CSS_SELECTOR, ".scrollmenu")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".logout").click()