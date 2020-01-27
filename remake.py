readlist=["test.txt"]
item="{0} {1}"
for read in readlist:
    outdata=[]
    with open(read, "r", encoding="utf-8")as file:
        count=1
        for line in file:
            if count < 10:
                outdata.append(" "+item.format(str(count),line))
            else:
                outdata.append(item.format(str(count),line))
            count+=1

    with open("out_"+read, "w", encoding="utf-8")as file:
        for i in outdata:
            file.write(i)