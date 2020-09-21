import pandas as pd
import folium

# データフレームを読み込む
df = pd.read_csv("prefecture.csv")

# 店舗のある地点（緯度、経度）と店舗名をリスト化する
store = df[["緯度","経度","所在地"]].values

# 地図を作って書き出す
m = folium.Map(location=[35.68944,135], zoom_start=5.5)
for data in store:
  	folium.Marker([data[0], data[1]], tooltip=data[2]).add_to(m)

m.save('prefecture.html')
