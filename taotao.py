import os
from selenium import webdriver
import datetime
import time
from os import path
from selenium.webdriver.common.action_chains import ActionChains

d = path.dirname(__file__)
abspath = path.abspath(d)

driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.maximize_window()


def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    time.sleep(3)
    # 用find_element_by_link_text，方式定位，标签必须是 < a > < / a > 的元素
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()

    print("请在15秒内完成扫码")
    time.sleep(15)

    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    # 点击购物车里全选按钮
    # if driver.find_element_by_id("J_CheckBox_939775250537"):
    #  driver.find_element_by_id("J_CheckBox_939775250537").click()
    # if driver.find_element_by_id("J_CheckBox_939558169627"):
    #  driver.find_element_by_id("J_CheckBox_939558169627").click()
    # 获取id为J_SelectAll1的div（购物车全选按钮的id）如果有就点击
    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S:%f'))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print("当前时间" + now)
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
                # 点击结算按钮
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                driver.find_element_by_link_text('提交订单').click()
            except:
                time.sleep(0.1)
        print(now)
        time.sleep(0.1)


if __name__ == "__main__":
    # times = input("2020-03-10 07:40:00.000000")
    # 时间格式："2018-09-06 11:20:00.000000"
    login()
    buy("2020-03-10 07:45:00.000000")