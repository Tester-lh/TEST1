import json
import tushare as ts

df = ts.month_boxoffice()
print(df)
jdata = {}
for idx, row in df.iterrows():
    if idx < 5:
        i = str(idx)
        jdata[i] = {}
        jdata[i]['rank'] = str(row['Irank'])
        jdata[i]['name'] = row['MovieName']
        jdata[i]['avgprice'] = str(row['avgboxoffice'])
        jdata[i]['avgcount'] = str(row['avgshowcount'])
        jdata[i]['total'] = str(row['boxoffice'])
with open('movie.json', 'w+') as f:
    json.dump(jdata, f)
with open('movie.json', 'r') as f:
    jdata = json.load(f)
    print(jdata)

