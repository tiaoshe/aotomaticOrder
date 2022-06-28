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
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
driver.implicitly_wait(10)


def test_click():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    time.sleep(2)
    click_y = int(y / 5 * 3 - 30 - 3)
    driver.tap([(x * 0.09, click_y)], 500)
    for i in range(50):
        # 选择分类
        el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().className(\"android.view.View\").textContains(\"测试标签\")')
        el.click()
        # 选择规格
        el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().className(\"android.view.View\").textContains(\"选规格\")')
        el.click()
        time.sleep(1)
        driver.tap([(x * 0.5, y - 30)], 500)
        # 结算
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().className(\"android.view.View\").textContains(\"结算\")').click()
        try:
            # 提交订单
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                'new UiSelector().className(\"android.view.View\").textContains(\"提交订单\")').click()
        except Exception as e:
            print(e)
            # name = str(i) + "error.png"
            # driver.save_screenshot(name)
            # 结算
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                'new UiSelector().className(\"android.view.View\").textContains(\"结算\")').click()
            # 提交订单
            el2 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                      'new UiSelector().className(\"android.view.View\").textContains(\"提交订单\")')
            el2.click()

        # driver.find_element_by_android_uiautomator(
        #     'new UiSelector().className(\"android.view.View\").textContains(\"结算\")').click()
        # 支付
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().className(\"android.view.View\").textContains(\"确认支付\")').click()
        # 返回首页
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().className(\"android.view.View\").textContains(\"返回首页\")').click()


if __name__ == '__main__':
    test_click(5)
