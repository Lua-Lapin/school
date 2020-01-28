# read_list=["overlap.dat","unique.dat"]
# out = "wc.txt"

inread = input()
read_list = []
while inread != "wc.txt":
    read_list.append(inread)
    inread = input()
else:
    out=inread

out_list=[]
text = "{} : {} 文字, {} 語, {} 行"
for read in read_list:
    char=0
    word=0
    line=0

    with open(read, 'r') as r_file:
        for line_data in r_file: # ファイルの終わりまで読み込みを繰り返す
            char += len(line_data)
            word += len(line_data.split())
            line += 1

    out_list.append(text.format(read,char,word,line))

with open(out, 'w', encoding='utf-8') as w_file:
    for out in out_list:
        w_file.write(out+"\n")
        print(out)