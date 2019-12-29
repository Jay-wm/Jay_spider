import lxml.html
import requests

data = '''
<! DOCTYPE html>
    <html>
    <head lang="en">
    <meta charset="UTF-8">
    <title></title>
    </head>
    <body>
        <div id="test3">
            我左青龙，
            <span id="tiger">
                右白虎，
            <ul>上朱雀，
                <li>下玄武。</li>
            </ul>
            老牛在当中，
            </span>  
            龙头在胸口。    
        </div>
    </body>
    </html>
'''
html_data1 ='''
<html>
    <head>
    <title>测试</title>
    </head>
    <body>
        <div class="useful">
            <ul>
                <li class="info">我需要的信息1</li>
                <li class="info">我需要的信息2</li>
                <li class="info">我需要的信息3</li>
            </ul>       
        </div>
        <div class="useless">
            <ul>
                <li class="info">垃圾1</li>
                <li class="info">垃圾2</li>
            </ul>
        </div>
    </body>
</html>
'''
selector = lxml.html.fromstring(data)
content = selector.xpath('//div[@id="test3"]/text()')
#info_list = content[0].xpath('ul/li/text()')
for each in content:
    print(each)
