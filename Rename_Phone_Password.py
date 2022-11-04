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
driver.find_element(By.CSS_SELECTOR, ".avatar_link").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Безопасность и вход").click()
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "By.CSS.SELECTOR, .name").click()
driver.find_element(By.NAME, "phone").send_keys("name=phone")
driver.find_element(By.NAME, "phone").clear()
time.sleep(0.5)
driver.find_element(By.NAME, "phone").send_keys("9121234567")
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, ".img> img").click()
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, ".item:nth-child(2) .name").click()
time.sleep(1)
driver.find_element(By.ID, "oldPassword").send_keys("129535851")
time.sleep(1)
driver.find_element(By.ID, "newPassword").send_keys("129535851")
time.sleep(1)
driver.find_element(By.ID, "confirmPassword").send_keys("129535851")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".img> img").click()
time.sleep(2)
# ActionChains(driver).move_by_offset(75, 75).click().perform()
element = driver.find_element(By.CSS_SELECTOR, ".scrollmenu")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".logout").click()
