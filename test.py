import folium

num1 = float(input('위도:'))
num2 = float(input('경도:'))

center = [num1, num2]

m = folium.Map(location=center, zoom_start=10)

a=[num1, num2]
m=folium.Map(a)
g = folium.Marker(a)
g.add_to(m)
