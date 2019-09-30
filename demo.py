# -*- coding:utf-8 -*-
import requests,time,pymysql
from bs4 import BeautifulSoup

def get_html(url):
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
	r = requests.get(url=url, headers=headers, timeout=10)
	if r.status_code == 200:
		html = requests.get(url=url,headers=headers,timeout=10).text
		return html
	else:
		print('无法访问：{}'.format(url))

def main():
	for id in range(0, 226, 25):
		url = 'https://movie.douban.com/top250?start={}&filter='.format(id)
		html = get_html(url)
		soup = BeautifulSoup(html, 'lxml')
		div = soup.find_all('div', class_='item')
		for i in div:
			PaiMing = i.find('em').text
			MingCheng = i.find('div', class_='hd').find('span').text
			PingFen = i.find('span', class_="rating_num").text
			PingLunRenShu = i.find('div', class_='star').find_all('span')
			PingLunRenShu = PingLunRenShu[-1].text[0:-3]
			LianJieDiZhi = i.find('div', class_='hd').find('a').get('href')

			print('排名：{}'.format(PaiMing))
			print('名称：{}'.format(MingCheng))
			print('评分：{}'.format(PingFen))
			print('评论人数：{}'.format(PingLunRenShu))
			print('连接地址：{}'.format(LianJieDiZhi))
			print('--------------------------------------------------')
			time.sleep(0.1)

if __name__ == '__main__':
	main()
	input('')
