# @time 2022/6/16 10:46
# @Author howell
# @File test_auto_ui.PY
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
import uiautomator2 as u2

# from hamcrest import *

capabilities = {}
# Android平台测试
capabilities['platformName'] = 'Android'
# 测试手机版本为5.0
capabilities['platformVersion'] = '7.1.2'
capabilities['deviceName'] = '127.0.0.1:21503'
# 系统手机中的联系人app的包名   adb shell "dumpsys window | grep mCurrentFocus"
capabilities['appPackage'] = 'com.smjcs.app'
# 系统手机中的联系人app的主入口activity
capabilities['appActivity'] = 'io.dcloud.PandoraEntryActivity'
capabilities['unicodeKeyboard'] = True
capabilities['resetKeyboard'] = False
capabilities['noReset'] = True
capabilities['automationName'] = 'uiautomator2'
driver = webdriver.Remote('http://127.0.0.1:4750/wd/hub', capabilities)
driver.implicitly_wait(60)


def test_click():
    # 连接测试机所在服务器服务器
    # el = driver.find_element_by_android_uiautomator(
    #     'new UiSelector().className(\"android.view.View\").textContains(\"取消\")')
    # el.click()
    # el = driver.find_element_by_android_uiautomator(
    #     'new UiSelector().className(\"android.view.View\").textContains(\"水果蔬菜\")')

    # # 获取confirm对象
    # alert = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
    #                          'new UiSelector().className(\"android.widget.FrameLayout\").textContains(\"取消\")')
    # # 点击取消（需要先获取对象）
    # alert.click()
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    time.sleep(2)
    click_y = int(y/5*3-30-3)
    driver.tap([(65, click_y)], 500)
    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                             'new UiSelector().className(\"android.view.View\").textContains(\"水果蔬菜\")')
    el.click()

    # # 打印confirm对象的提示信息
    # # print(alert.text)
    # # # 点击确认
    # # alert.accept()

    # print("1111")
    # time.sleep(2)
    # driver.find_element_by_android_uiautomator('text(\"水果蔬菜\")').click()
    # print("2222")


# time.sleep(2)
# 断开连接
if __name__ == '__main__':
    test_click()
