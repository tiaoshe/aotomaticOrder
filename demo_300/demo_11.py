# @time 2022/6/13 16:49
# @Author howell
# @File demo_05.PY
# file_name: test_abc.py

# 导入 webdriver
from selenium import webdriver

# 调用键盘按键操作时需要引入的Keys包
from selenium.webdriver.common.keys import Keys


def test_webdriver():
    # 调用环境变量指定的PhantomJS浏览器创建浏览器对象
    # driver = webdriver.PhantomJS()

    # 如果没有在环境变量指定PhantomJS位置
    driver = webdriver.PhantomJS(executable_path=r"D:\【宫殿】\100工具\phantomjs-2.1.1-windows\bin\phantomjs.exe")

    # get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
    driver.get("http://www.baidu.com/")

    # 获取页面名为 wrapper的id标签的文本内容
    data = driver.find_element_by_id("wrapper").text

    # 打印数据内容
    print(data)
    driver.save_screenshot("baidu.png")
    print(driver.page_source)
    # id="kw"是百度搜索输入框，输入字符串"长城"
    driver.find_element_by_id("kw").send_keys(u"长城")

    # id="su"是百度搜索按钮，click() 是模拟点击
    driver.find_element_by_id("su").click()

    # 获取新的页面快照
    driver.save_screenshot("长城.png")
    # driver.close()
    driver.quit()


if __name__ == '__main__':
    test_webdriver()
