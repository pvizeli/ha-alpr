import asyncio
from haalpr import HAAlpr

if sys.platform == "win32":
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)
else:
    loop = asyncio.get_event_loop()

alpr = HAAlpr()

with open("test.jpg", "rb") as fl_image:
    image = fl_image.read()

result = loop.run_until_complete(alpr.recognize_byte(image))
print("%s" % result)
loop.close()
