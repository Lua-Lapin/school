read="title_list.csv"
out = "title_dd.html"

tmp = "<dt>{0[1]}({0[0]})</dt><dd>{0[2]}</dd>\n"

with open(read, 'r') as r_file:
    list=[]
    for line_data in r_file: # ファイルの終わりまで読み込みを繰り返す
        list.append(line_data.strip('\n').split(','))

for data in list:
    print(data,end="")

with open(out, 'w', encoding='utf-8') as w_file:
    w_file.write("<dl>\n")
    for data in list:
        w_file.write(tmp.format(data))
    w_file.write("</dl>")