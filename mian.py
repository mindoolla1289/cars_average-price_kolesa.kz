#Подключил необходимые библиотеки
import requests
from bs4 import BeautifulSoup
import json
import re

#заполнил headers из своего браузера он нам нужен для доступа к сайту
headers={
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
	"Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
	"Cache-Control":"ax-age=0",
	"Connection":"keep-alive",
	"Cookie":"_ga=GA1.2.501866573.1643284736; _gid=GA1.2.712851034.1643284736; ssaid=80ec7830-7f68-11ec-b8d1-8f7dc2432b0d; _ym_uid=1643284736201328451; _ym_d=1643284736; _ym_isad=2; _fbp=fb.1.1643284738239.700722887; __gads=ID=59adb936ae9056ee-2276623e2dcd00df:T=1643284737:S=ALNI_MZ7Pem54WXOa_yQaeGiROl2dXK0FA; is_returning=1; gh_show=1; dd_user.isReturning=true; dd__persistedKeys=[%22user.isReturning%22%2C%22custom.sessionViewedPages%22]; nps=viewed; dd__lastEventTimestamp=1643356076363; kl_cdn_host=//alakcell-kz.kcdn.online; klssid=ibptskd0rkoc2gbqapod4hcs0b; dd_custom.sessionViewedPages=1; __tld__=null; _gat=1; _ym_visorc=w",
	"Host":"kolesa.kz",
	"Sec-Fetch-Dest":"document",
	"Sec-Fetch-Mode":"navigate",
	"Sec-Fetch-Site":"none",
	"Sec-Fetch-User":"?1",
	"TE":"trailers",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
}

#подключаемься к kolesa.kz и для удобства и чтобы нас не блокнули из-за частого подключения, записываем главную страницу себе
#url="https://kolesa.kz/"
#req = requests.get(url,headers=headers)
#src = req.text

#with open("kolesa.html","w",encoding="utf-8") as file:
# 	file.write(src)



#Все, у нас есть файл kolesa.kz, дальше будем работать с ним. Делаем суп, скармливаем html файл BeautifulSoup
with open("kolesa.html", encoding="utf-8") as file:
 	src = file.read()

soup= BeautifulSoup(src,"lxml")


#нам нужны все марки машин


#находим нужный нам класс, где написаны марки машин 
car_brands=soup.find(class_="block-links-list row hide").find_all("a")
#соберем все марки и ссылки на них в в словарь 
cars_name_data={}
for brand in car_brands:
	car_brand=brand.text
	car_brand_link="https://kolesa.kz"+brand.get("href")
	cars_name_data[car_brand]=car_brand_link

#а сам словарь запишем и сохраним в json файл, тоже для удобства
with open("cars_name_data.json","w",encoding="utf-8") as file:
 	json.dump(cars_name_data, file, indent=4,ensure_ascii=False)