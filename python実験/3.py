import datetime
before1 = input("開始日(YYYY/MM/DD) :")
after1 = datetime.datetime.strptime(before1, '%Y/%m/%d')
before2 = input("終了日(YYYY/MM/DD) :")
after2 = datetime.datetime.strptime(before2, '%Y/%m/%d')


out = after2-after1
print("日数差: {0} 日".format(out.days))

