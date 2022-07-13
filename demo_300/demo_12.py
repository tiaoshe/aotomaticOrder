# @time 2022/7/5 10:01
# @Author howell
# @File demo_12.PY
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_action():
    # 如果没有在环境变量指定PhantomJS位置
    driver = webdriver.PhantomJS(executable_path=r"D:\【宫殿】\100工具\phantomjs-2.1.1-windows\bin\phantomjs.exe")

    # get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
    driver.get("http://www.baidu.com/")
    # # 鼠标移动到 ac 位置
    # ac = driver.find_element_by_xpath('element')
    # ActionChains(driver).move_to_element(ac).perform()
