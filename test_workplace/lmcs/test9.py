# from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options
# from selenium import webdriver
#
#
# def main():
#     options = Options()
#     options.add_argument('-headless')
#     driver = webdriver.Firefox(options=options)
#     driver.get("https://www.baidu.com")
#     print(driver.page_source)
#     driver.close()
#
#
# if __name__ == '__main__':
#     main()


from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://smj.dev.jzwp.shop/admin/?#/offline/offlineProductList')
browser.maximize_window()
