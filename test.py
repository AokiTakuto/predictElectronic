#!/usr/bin/env python
# coding=utf-8

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
<header>
気温データと時間、曜日からその時間帯の電力需用量を予測します。
<br>
下記の項目にデータを入力してください。
<br>
<form method="post" action="sample.py">
<br>
曜日：<select name="date">
   <option>月</option>
   <option>火</option>
   <option>水</option>
   <option>木</option>
   <option>金</option>
   <option>土</option>
   <option>日</option>
 </select>
<br>
時間：<select name="time">
   <option>0:00</option>
   <option>1:00</option>
   <option>2:00</option>
   <option>3:00</option>
   <option>4:00</option>
   <option>5:00</option>
   <option>6:00</option>
   <option>7:00</option>
   <option>8:00</option>
   <option>9:00</option>
   <option>10:00</option>
   <option>11:00</option>
   <option>12:00</option>
   <option>13:00</option>
   <option>14:00</option>
   <option>15:00</option>
   <option>16:00</option>
   <option>17:00</option>
   <option>18:00</option>
   <option>19:00</option>
   <option>20:00</option>
   <option>21:00</option>
   <option>22:00</option>
   <option>23:00</option>
   <option>24:00</option>
</select>
<br>
気温：<input type="text" name="temp"/>
<br>
<input type="submit" value="送信" >
</form>
</body>
</html>
''')
