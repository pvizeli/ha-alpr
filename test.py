from haalpr import HAAlpr

alpr = HAAlpr()

with open("test.jpg", "rb") as fl_image:
    image = fl_image.read()

result = alpr.recognize_byte(image)
print("%s" % result)
