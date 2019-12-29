from uiautomator import Device

device = Device()
list = []
for i in range(10):
    list.append(i)
    # print(i)
    # print(device.dump())
    # device(scrollable=True).scroll.vert.forward()

for a in list:
    print(a)