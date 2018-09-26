#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cgi
import cgitb
import pickle
import numpy as np
import pandas as pd
cgitb.enable()

# モデルのデシリアライズ
rf = pickle.load(open('cgi-bin/electnicPowerPredictor.pkl','rb'))

# 変数の取り込み
form = cgi.FieldStorage()
df = pd.DataFrame([form['temp'].value,form['time'].value,form['date'].value])
df_pred = pd.DataFrame([df.iloc[0,0]])

cols = ['0:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00',
       '17:00', '18:00', '19:00', '1:00', '20:00', '21:00', '22:00', '23:00',
       '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00']

yobi = ['土','日', '月', '木', '水', '火', '金']


for col in cols:
    if df.iloc[1,0] == col:
        df_pred[col] = 1
    else:
        df_pred[col] = 0


for y in yobi:
    if df.iloc[2,0] == y:
        df_pred[y] = 1

    else:
        df_pred[y] = 0



# 予測
result = rf.predict(X=df_pred)

print('Content-type: text/html; charset=UTF-8\r\n')
print('''
<!doctype'>
<html lang="ja">
<html>
<head>
<meta charset="UTF-8">
<title>電力需要予測</title>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
</head>
<body>
<br><br>
該当の時間帯の電力需要量の予測値は
<br>
''')
print(result[0])
print('''
<br>
です
</body>
</html>
''')


