import time

from selenium.webdriver.common.by import By

from common_function import scroll_down_until_element_visible_top, scroll_down_until_element_visible_bottom
from driver_config import driver

# x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r x126k92a 文章內容


driver.get('https://www.facebook.com/groups/1260448967306807')
driver.find_element(By.XPATH, "//*[@placeholder='電子郵件地址或手機號碼']").send_keys('puppylionmonkey')
time.sleep(10)  # 輸入密碼、登入
#

# driver.find_elements(By.XPATH, "//*[@class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")  # 文章element
# driver.find_element(By.XPATH, "//*[@data-visualcompletion='css-img' and contains(@style, '-242')]/parent::*/parent::*//span")  # 留言數
# for i in range(5):
while True:
    message_count_list = list()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)
    print('目前文章數:', len(driver.find_elements(By.XPATH, "//*[@class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")))
    message_count_element_list = driver.find_elements(By.XPATH, "//*[@class='x1n2onr6']//span[contains(text(), '則留言')]")  # 留言數
    print(message_count_element_list)
    for message_count_element in message_count_element_list:
        if message_count_element.text == '':
            continue
        else:
            message_count_list.append(int(message_count_element.text.replace('則留言', '')))
    if max(message_count_list) > 700:
        break
print(message_count_list)
max_message_count = max(message_count_list)
# 找到701留言的文章

message_count_xpath = "//*[@class='x1n2onr6']/parent::*/parent::*//span[text()='" + str(max_message_count) + "則留言']"
print(driver.find_element(By.XPATH, message_count_xpath + "/ancestor::*[@class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']//*[@class='x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r x126k92a']").text)
# # 點擊留言
scroll_down_until_element_visible_bottom(message_count_xpath)
driver.find_element(By.XPATH, message_count_xpath).click()
#
# driver.find_element(By.XPATH, "//*[contains(@class, '')]")
