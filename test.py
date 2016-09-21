from haalpr import HAAlpr

alpr = HAAlpr()

with open("test.jpg", "rb") as fl_image:
    image = fl_image.read()

alpr.recognize_byte(image)
print("%s" % result)
loop.close()
