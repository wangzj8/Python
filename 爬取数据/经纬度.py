#!/usr/bin/env python3
lat_1 = 24.390894
lon_1 = 102.174112
lat_2 = 26.548645
lon_2 = 103.678942 #坐标范围
las = 1 #给las一个值1
lat_count = int((lat_2-lat_1)/las+1)
lon_count = int((lon_2-lon_1)/las+1)
for lat_c in range(0,lat_count):	
	lat_b1=lat_1+las*lat_c
	for lon_c in range(0,lon_count):	
		lon_b1=lon_1+las*lon_c
		#for i in range(0,20):
		#	page_num = str(i)
		#	url = ('http：//api.map.baidu.com/place/v2/search?query=医院&bounds='+str(lat_b1)+','+str(lon_b1)+','+str(lat_b1+las)+','+str(lon_b1+las)+'&page_size=20&page_num='+str(page_num)+'&output=json&ak=1hoAALdzHGlkrW06gMwKdkrthKXhcA649X')
		#	print(url)
		print (str(lat_b1)+','+str(lon_b1)+','+str(lat_b1+las)+','+str(lon_b1+las)+','+str(page_num))