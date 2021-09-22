from appium import webdriver

desired_cap = {
    "platformName": "Android",
    # "deviceName": "emulator-5554",
    "deviceName": "b3f964e3",
    "appPackage": "tv.danmaku.bili",
    "appActivity": ".MainActivityV2",
    "noReset": "true"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
driver.implicitly_wait(20)

el1 = driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc=\"热门\"]/android.widget.TextView")
el1.click()
el2 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.ImageView")
el2.click()
# driver.quit()
