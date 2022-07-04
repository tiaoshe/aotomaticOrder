# @time 2022/6/13 16:49
# @Author howell
# @File demo_05.PY
# file_name: test_abc.py
from bs4 import BeautifulSoup


def test_BeautifulSoup():
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """

    # 创建 Beautiful Soup 对象
    soup = BeautifulSoup(html)

    # 打开本地 HTML 文件的方式来创建对象
    # soup = BeautifulSoup(open('index.html'))

    # # 格式化输出 soup 对象的内容
    # print(soup.prettify())
    #
    print(soup.name)
    print(soup.a.name)
    print(soup.a.string)
    print(soup.p.attrs)
    soup.p['class'] = "newClass"
    print(soup.p)
    print(soup.body.contents)


if __name__ == '__main__':
    test_BeautifulSoup()
