import pandas as pd
import os

csv_list = {}
f = open('result.txt', 'w')
for dirname, _, filenames in os.walk("C:/Users/songj/Desktop/kshield/dataset/kisa"):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        df = pd.read_csv(os.path.join(dirname, filename), delimiter=",", encoding='utf-8', error_bad_lines=False)
        f.write(os.path.join(dirname, filename))
        columns = df.columns
        for column in columns:
            f.write(column)
            list_all = list(df[column])
            list_unique = list(set(list_all))
            for i in list_unique:
                data = str(i) + '\t\t' + str(list_all.count(i)) + '\n'
                f.write(data)
