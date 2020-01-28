import os.path

n = 0 # 日数のカウンタ
total = 0.0 # 気温の合計
max = 0.0 # 最高気温
min = 10000000.0#最低気温
average = 0.0 # 平均気温

if(os.path.isfile("temperature.dat") == False):
    print("temperature.dat: No such file or directory.")
    exit(1)

with open("temperature.dat", 'r') as r_file: # ファイルを読み込みモードでオープン
    for line_data in r_file: # ファイルの終わりまで読み込みを繰り返す
        daily_data = line_data.split() # リストに変換
        if daily_data[1] == "気温［℃］": # ヘッダは変換できないのでスキップ
            continue
        temperature = float(daily_data[1]) # 気温データを文字型 -> 数値型に変換
        if max < temperature: # 最高気温か比較
            max = temperature # 最高気温を更新
            date1 = daily_data[0] # 最高気温日を更新
        if min > temperature: # 最高気温か比較
            min = temperature # 最高気温を更新
            date2 = daily_data[0] # 最高気温日を更新
        total = total + temperature # 気温の合計
        n = n + 1

average = total / n # 平均気温
average='{:.3f}'.format(average)

print("日時:", date1, "，最高気温:", max, "℃")
print("日時:", date2, "，最低気温:", min, "℃")
print("平均気温:", average, "℃\n")

with open("average.dat", 'w', encoding='utf-8') as w_file: # ファイルを書き込みモードでオープン
    w_file.write("日時：" + date1 + "，最高気温：" + str(max) + " ℃\n")
    w_file.write("平均気温：" + str(average) + " ℃\n")