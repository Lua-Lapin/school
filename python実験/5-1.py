read="overlap.dat"
out = "unique.dat"
with open(read, 'r') as r_file:
    list=[]
    for line_data in r_file: # ファイルの終わりまで読み込みを繰り返す
        if line_data not in list:
            list.append(line_data)

# for data in list:
#     print(data,end="")

with open(out, 'w', encoding='utf-8') as w_file:
    for data in list:
        w_file.write(data)