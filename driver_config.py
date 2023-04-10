import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

current_directory = os.path.dirname(os.path.abspath(__file__))
# print(current_directory)
project_path = current_directory + '/'
chromedriver_path = project_path + 'chromedriver.exe'

# path1 = chrome_path + "user data"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument(r"user-data-dir=" + path1)  # 不能同時開兩個

# 關閉允許通知視窗
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(chromedriver_path, options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
actions = ActionChains(driver)
