from appium import webdriver

desired_cap = {
    "platformName": "Android",
    # "deviceName": "emulator-5554",
    "deviceName": "b3f964e3",
    "appPackage": "com.taobao.taobao",
    "appActivity": "com.taobao.tao.TBMainActivity",
    "noReset": "true"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
driver.implicitly_wait(20)