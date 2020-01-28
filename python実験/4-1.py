import random # random モジュールの取り込み
year = "2015"
month = "Aug"

record_style = "{0}/{1}/{2:02d} {3:2.3f}" # {2:02d} と {3:2.3f} の間は ［TAB］

print("  年/月/日      気温[℃]") # ヘッダの表示


with open("temperature.dat", 'w') as w_file: # ファイルを書き込みモードでオープン
    for day in range (1, 32): # 1 ～ 31 までの繰り返し

        random.seed() # 乱数生成器の初期化
        temperature = random.uniform(30.0, 40.0) # 30.0 ～ 40.0 の乱数を生成

        w_file.write(record_style.format(year, month, day, temperature)+"\n")

        day = day + 1