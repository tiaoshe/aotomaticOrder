# @time 2022/7/5 13:57
# @Author howell
# @File demo_13_pytesseract.PY
import pytesseract
from PIL import Image


def test_pytesseract():
    image = Image.open('123.png')
    text = pytesseract.image_to_string(image)
    print(text)
