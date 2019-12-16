from uiautomator import Device

app_list = []
device = Device()



for i in range(2):
    if i !=0:
        device(scrollable=True).scroll.vert.forward()
    # get the app list of the current page
    app_download_ranking = device(index="0", className = "android.widget.Image")

    # print the app name of the current page
    for app in app_download_ranking:
        if app not in app_list:
            app_list.append(app)
            print(app.text)
    #
    # for a in app_list:
    #     print(a.text)


