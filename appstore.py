#_*_coding=utf-8_*_

import urllib
import json
import xlsxwriter
import sys
reload(sys)
sys.setdefaultencoding('utf8')
page = 1
appid = 873474116
workbook = xlsxwriter.Workbook('app评论.xlsx')
worksheet = workbook.add_worksheet()
format=workbook.add_format()
format.set_border(1)
format.set_border(1)
format_title = workbook.add_format()
format_title.set_border(1)
format_title.set_bg_color('#cccccc')
format_title.set_align('left')
format_title.set_bold()
title=['昵称','标题','评论内容']
worksheet.write_row('A1',title,format_title)
row=1
col=0

# 默认一次抓取一页,根据自己需求抓取多少页,最多50页
while page < 2:  # 默认循环10次

    myurl = "https://itunes.apple.com/rss/customerreviews/page=" + str(page) + "/id=" + str(
        appid) + "/sortby=mostrecent/json?l=en&&cc=cn"
    response = urllib.urlopen(myurl)
    # print(response.read())
    myjson = json.loads(response.read().decode('utf8'))
    print(myjson)
    print("正在生成数据文件，请稍后......" + str(page * 10) + "%")
    del (myjson["feed"]["entry"][0])
    for i in myjson["feed"]["entry"]:
        worksheet.write(row, col, i["author"]["name"]["label"], format)
        row = row + 1
    row = 1 + (page - 1) * 50
    for i in myjson["feed"]["entry"]:
        worksheet.write(row, col + 1, i["title"]["label"], format)
        row = row + 1
    row = 1 + (page - 1) * 50
    for i in myjson["feed"]["entry"]:
        worksheet.write(row, col + 2, i["content"]["label"], format)
        row = row + 1
    page = page + 1
    row = (page - 1) * 50 + 1
print("生成完毕，请查阅相关文件")
workbook.close()
