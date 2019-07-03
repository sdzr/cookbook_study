# 从脚本中加载一个浏览器，并让他打开指定url

import webbrowser

print(webbrowser.open('https://www.baidu.com'))

#webbrowser.open_new('https://www.baidu.com')

#webbrowser.open_new_tab('https://www.baidu.com')

# 指定具体的浏览器,在https://docs.python.org/3/library/webbrowser.html中看一看到支持的浏览器
c =webbrowser.get('windows-default')
print(webbrowser.open('https://www.baidu.com'))