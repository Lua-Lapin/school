import re

read="title_dd.html"
out = "title_list_2.csv"

tmp = "{0[1]},{0[0]},{0[2]}\n"

with open(read, 'r', encoding='utf-8') as r_file:
    list=[]
    for line_data in r_file: # ファイルの終わりまで読み込みを繰り返す
        if line_data.find("<dl>") != -1:
            continue
        elif line_data.find("</dl>") != -1:
            continue
        else:
            list.append([i for i in re.split('<dt>|\(|\)</dt><dd>|</dd>',line_data) if i != ''])

for data in list:
    print(data,end="")

with open(out, 'w', encoding='utf-8') as w_file:
    for data in list:
        w_file.write(tmp.format(data))