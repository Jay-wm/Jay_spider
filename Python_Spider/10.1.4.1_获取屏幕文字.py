from uiautomator import Device

app_list = []
device = Device()

for i in range(2):
    if i !=0:
        device(scrollable=True).scroll.vert.forward()
    # get the app list of the current page
    app_download_ranking = device(index="0", className = "android.widget.Image")

    # print the app name of the current page
    for m in range(len(app_download_ranking)):
        if app_download_ranking[m] in app_list:
            
        else:
            app_list.append(app_download_ranking[m])
            
for a in app_list:
    print(a.text)


