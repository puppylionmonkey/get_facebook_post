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

record_list = list()
i = -1
while True:
    i += 1
    driver.find_elements(By.XPATH, "//*[@class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")
    name_element_list = driver.find_elements(By.XPATH, "//*[@class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']//*[@class='xu06os2 x1ok221b']//*[@class='xt0psk2']")  # 發文人名
    name_list = [name_element.text for name_element in name_element_list]
    name = name_list[i]
    post_xpath = "//*[@class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']//*[@class='xu06os2 x1ok221b']//*[@class='xt0psk2']//*[text()='" + name + "']/ancestor::*[@class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']"
    # 點開留言
    scroll_down_until_element_visible_bottom(post_xpath + "//*[@class='x1n2onr6']//span[contains(text(), '則留言')]")
    driver.find_element(By.XPATH, post_xpath + "//*[@class='x1n2onr6']//span[contains(text(), '則留言')]").click()

    # content
    new_post_xpath = "//*[text()='" + name + "的貼文']/ancestor::*[@class='x78zum5 xdt5ytf x1iyjqo2 x1n2onr6 x1jxyteu x1mfppf3 xqbnct6 xga75y6']"
    show_more_content_xpath = new_post_xpath + "//*[text()='顯示更多']"

    if len(driver.find_elements(By.XPATH, show_more_content_xpath)) > 0:
        scroll_down_until_element_visible_bottom(show_more_content_xpath)
        driver.find_element(By.XPATH, show_more_content_xpath).click()
    content_xpath = new_post_xpath + "//*[@class='x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r x126k92a']"
    content = driver.find_element(By.XPATH, content_xpath).text
    print(content)
    # todo: 顯示更多
    # message
    driver.find_element(By.XPATH, "//*[text()='最相關留言']").click()
    driver.find_element(By.XPATH, "//*[text()='所有留言']").click()

    while True:
        if len(driver.find_elements(By.XPATH, "//*[contains(text(), '先前的留言')]")) > 0:
            try:
                driver.find_element(By.XPATH, "//*[contains(text(), '先前的留言')]").click()
            except:
                break
        else:
            break

    # driver.find_element(By.XPATH, "//*[@class='x1n2onr6']/parent::*/parent::*//span[text()='" + str(max_message_count) + "則留言']/ancestor::*[@class='xwya9rg x11i5rnm x1e56ztr x1mh8g0r xh8yej3']//h3[text()='留言']/parent::*/ul")
    # li_list = driver.find_elements(By.XPATH, "//*[@class='x1n2onr6']/parent::*/parent::*//span[text()='" + str(max_message_count) + "則留言']/ancestor::*[@class='xwya9rg x11i5rnm x1e56ztr x1mh8g0r xh8yej3']//h3[text()='留言']/parent::*/ul/li")
    # str_id = 0
    # message_list = list()
    # message = ''
    # for li in li_list:
    #     message_text = li.text
    #     message_split_list = message_text.split('\n')
    #     # print(message_split_list)
    #     for i in range(len(message_split_list)):
    #         if '回覆分享' in message_split_list[i - 1] or '則回覆' in message_split_list[i - 1]:
    #             continue
    #         if '則回覆' in message_split_list[i] or '回覆分享' in message_split_list[i]:
    #             continue
    #         if message_split_list[i] != '讚':
    #             message += message_split_list[i]
    #         if message_split_list[i] == '讚':
    #             message_list.append(message)
    #             message = ''
    driver.find_element(By.XPATH, "//*[@aria-label='關閉']").click()
    # print(message_list)
