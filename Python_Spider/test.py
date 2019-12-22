from uiautomator import Device
import time

star_time = time.time()

'''初始化设备与列表'''
app_list = []
device = Device()

'''获取排行榜前十APP'''
for i in range(5):
    # get the app list of the current page
    app_download_ranking = device(index="0", className = "android.widget.Image")
    b = 0
    # print the app name of the current page
    for m in range(len(app_download_ranking)):
        if len(app_list) < 20:
            app_list.append(app_download_ranking[m].text)
        else:
            b = 1
            break

    if b == 1:
        break
    device(scrollable=True).scroll.vert.forward()



end_time =time.time()
print(end_time - star_time)

for n in range(20):
    print(app_list[n])